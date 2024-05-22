from src.core.infrastructure.openai.open_ai_expenses_service import OpenAIExpensesService
from src.core.infrastructure.sql.sql_users_repository import SqlUsersRepository
from src.core.use_cases.add_expenses import AddExpenses

users_repository = SqlUsersRepository()
open_ai_expenses = OpenAIExpensesService()
add_expenses = AddExpenses(users_repository, open_ai_expenses)
