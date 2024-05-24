import os

from openai import OpenAI

from src.core.infrastructure.openai.open_ai_expenses_service import OpenAIExpensesService
from src.core.infrastructure.sql.sql_users_repository import SqlUsersRepository
from src.core.use_cases.add_expenses import AddExpenses

open_ai_api_key = os.getenv('OPEN_API_API_KEY')
users_repository = SqlUsersRepository()
open_ai_expenses = OpenAIExpensesService(OpenAI(api_key=open_ai_api_key))
add_expenses = AddExpenses(users_repository, open_ai_expenses)
