from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum


class InvalidExpensesValues(Exception):
    def __int__(self, inner: Exception, content):
        self.inner = inner
        self.content = content
        super().__init__(f'Could not create expenses with values: {content}, inner exception {inner}')


class NotExpensesException(Exception):
    def __init__(self):
        super().__init__(f'The message is not a valid expense')


class Category(Enum):
    FOOD = 'FOOD',
    UTILITIES = 'UTILITIES',
    INSURANCE = 'INSURANCE',
    MEDICAL_HEALTHCARE = 'MEDICAL/HEALTHCARE',
    SAVINGS = 'SAVINGS',
    EDUCATION = 'EDUCATION',
    ENTERTAINMENT = 'ENTERTAINMENT',
    OTHER = 'OTHER'

    @classmethod
    def of(cls, value):
        value = value.upper()
        for category in Category:
            if category.value[0] == value:
                return category

        raise Exception(f'f{value} is not a valid category')


@dataclass
class Expenses:
    description: str
    amount: Decimal
    category: Category
    added_at: datetime

    @classmethod
    def new(cls, description: str, amount: Decimal, category: Category):
        return cls(description, amount, category, datetime.now())


class ExpensesService:
    @abstractmethod
    def create(self, message: str) -> Expenses:
        pass
