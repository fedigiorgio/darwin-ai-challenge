import logging
import os
from contextlib import contextmanager

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

engine = create_engine(POSTGRESQL_URL,
                       echo=True,
                       pool_size=10,
                       pool_recycle=1800,
                       pool_pre_ping=True)

session_maker = sessionmaker(autoflush=True, bind=engine)

logging.basicConfig(level='INFO', format='%(asctime)s - %(levelname)s - %(message)s')


@contextmanager
def session_scope():
    session = session_maker()
    try:
        logging.info("New session open")
        yield session
    except Exception as e:
        session.rollback()
        logging.error(f"Error occurred in SQL session: {e}", exc_info=True)
        raise
    finally:
        logging.info("Closing session")
        session.close()
        logging.info("Session closed")


def users_repository():
    with session_scope() as session:
        return SqlUsersRepository(session)


open_ai_expenses = OpenAIExpensesService(OpenAI(api_key=open_ai_api_key))


def add_expenses():
    return AddExpenses(users_repository(), open_ai_expenses)


def get_expenses():
    return GetExpenses(users_repository())


def add_user():
    return AddUser(users_repository())
