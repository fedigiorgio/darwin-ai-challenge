from http import HTTPStatus

from flask import request, jsonify

from src import app
from src.core.domain.expenses import Expenses, Category
from src.modules import add_expenses


@app.route('/api/expenses', methods=['POST'])
def add_expenses_route():
    body = request.get_json()

    telegram_id = body['telegram_id']
    message = body['message']

    expenses = add_expenses.execute(telegram_id, message)
    return to_response(expenses)


def to_response(expenses: Expenses):
    response_body = {
        'description': expenses.description,
        'amount': expenses.amount,
        'category': expenses.category.value[0]
    }
    return jsonify(response_body), HTTPStatus.OK
