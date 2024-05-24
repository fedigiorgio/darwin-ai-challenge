from abc import abstractmethod
from dataclasses import dataclass

from src.core.domain.expenses import Expenses


@dataclass
class User:
    user_id: int
    telegram_id: str
    expenses: list[Expenses]

    def add_expenses(self, expense: Expenses):
        self.expenses.append(expense)


class UsersRepository:
    @abstractmethod
    def get(self, telegram_id: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User):
        pass
