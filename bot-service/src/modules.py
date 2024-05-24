import os

from openai import OpenAI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.infrastructure.openai.open_ai_expenses_service import OpenAIExpensesService
from src.core.infrastructure.sql.sql_users_repository import SqlUsersRepository
from src.core.use_cases.add_expenses import AddExpenses
from src.core.use_cases.add_user import AddUser
from src.core.use_cases.get_expenses import GetExpenses

open_ai_api_key = os.getenv('OPEN_API_API_KEY')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

POSTGRESQL_URL = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(POSTGRESQL_URL, echo=True)
session_maker = sessionmaker(bind=engine)
users_repository = SqlUsersRepository(session_maker())
open_ai_expenses = OpenAIExpensesService(OpenAI(api_key=open_ai_api_key))
add_expenses = AddExpenses(users_repository, open_ai_expenses)
get_expenses = GetExpenses(users_repository)
add_user = AddUser(users_repository)