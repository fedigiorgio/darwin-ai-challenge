import json
import logging
from decimal import Decimal

from openai import OpenAI

from src.core.domain.expenses import ExpensesService, Expenses, Category, NotExpensesException, \
    InvalidExpensesValuesException


class OpenAIExpensesService(ExpensesService):
    def __init__(self, client: OpenAI):
        self._client = client

    def create(self, message: str) -> Expenses:
        prompt = self._build_prompt(message)
        content = self._execute_chat_prompt(prompt)
        return self._map_to_expenses(content)

    def _execute_chat_prompt(self, prompt):
        chat_completion = self._client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt
        )
        content = chat_completion.choices[0].message.content
        logging.info(f'Received gpt chat completion response: {content}')
        return content

    @staticmethod
    def _build_prompt(message: str):
        return [{
            'role': 'system',
            'content': 'You will receive a description of an expense. Your task is to parse the '
                       'description and return a JSON object with the extracted information. If the expense is valid, '
                       'include the description, amount, and category, and set "result" to "OK". If the message does '
                       'not seem to be an expense,'
                       'set "result" to "ERROR". Here are the predefined categories: FOOD, UTILITIES, '
                       'INSURANCE, MEDICAL/HEALTHCARE, SAVINGS, EDUCATION, ENTERTAINMENT, and OTHER.'},
            {'role': 'user', 'content': 'Pizza 20 bucks'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "Pizza", "amount": 20.0, "category": "FOOD"}, "result": "OK"}'},
            {'role': 'user', 'content': 'AC/DC Concert the last weekend, it cost 55.5 usd'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "AC/DC Concert", "amount": 55.5, "category": "ENTERTAINMENT"},'
                        '"result": "OK"}'},
            {'role': 'user', 'content': 'Hello, how are you?'},
            {'role': 'assistant', 'content': '{"result": "ERROR"}'},
            {'role': 'user', 'content': 'electricity bill, 5 bucks'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "Electricity Bill", "amount": 5.0, "category": "UTILITIES"}, "result": "OK"}'},
            {'role': 'user', 'content': 'Steak five dollars'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "Steak", "amount": 5.0, "category": "FOOD"}, "result": "OK"}'},
            {'role': 'user', 'content': 'toothbrushes $2'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "Toothbrushes", "amount": 2.0, "category": "MEDICAL/HEALTHCARE"}, "result": "OK"}'},
            {'role': 'user', 'content': 'Soap 0.5 usd'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "Soap", "amount": 0.5, "category": "MEDICAL/HEALTHCARE"}, "result": "OK"}'},
            {'role': 'user', 'content': 'five dollars in videogames'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "VideoGames", "amount": 5.0, "category": "ENTERTAINMENT"}, "result": "OK"}'},
            {'role': 'user', 'content': 'beers 2.5'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "Beer", "amount": 2.5, "category": "FOOD"}, "result": "OK"}'},
            {'role': 'user', 'content': 'Keyboard 6 bucks'},
            {'role': 'assistant',
             'content': '{"expenses": {"description": "Keyboard", "amount": 6.0, "category": "OTHER"}, "result": "OK"}'},
            {'role': 'user', 'content': message}
        ]

    def _map_to_expenses(self, content: str) -> Expenses:
        json_content = json.loads(content)
        self._check_is_ok(json_content)
        try:
            expenses_json_content = json_content['expenses']
            description = expenses_json_content['description']
            amount = Decimal(expenses_json_content['amount'])
            category = Category.of(expenses_json_content['category'])
            return Expenses.new(description, amount, category)
        except Exception as ex:
            raise InvalidExpensesValuesException(ex, json_content)

    @staticmethod
    def _check_is_ok(json_content):
        if json_content['result'].upper() != 'OK':
            raise NotExpensesException()
