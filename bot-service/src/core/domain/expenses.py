from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Expenses:
    description: str
    amount: Decimal
    category: str
    added_at: datetime


class ExpensesService:
    @abstractmethod
    def create(self, message: str) -> Expenses:
        pass
