from abc import abstractmethod
from dataclasses import dataclass

from src.core.domain.expenses import Expenses


class UserNotExistsException(Exception):
    def __init__(self, telegram_id: str):
        super().__init__(f'User with telegram_id {telegram_id} doest not exists')


class UserAlreadyExistsException(Exception):
    def __init__(self, telegram_id: str):
        super().__init__(f'User with telegram_id {telegram_id} already exists')


@dataclass
class User:
    user_id: int
    telegram_id: str
    expenses: list[Expenses]

    def add_expenses(self, expense: Expenses):
        self.expenses.append(expense)

    @classmethod
    def new(cls, telegram_id):
        return cls(None, telegram_id, [])


class UsersRepository:
    @abstractmethod
    def exists(self, telegram_id: str) -> bool:
        pass

    @abstractmethod
    def get(self, telegram_id: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def add(self, user: User):
        pass
