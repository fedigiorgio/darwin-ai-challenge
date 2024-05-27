from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class InvalidExpensesValuesException(Exception):
    def __int__(self, inner: Exception, content):
        self.inner = inner
        self.content = content
        self.message = f'Could not create expenses with values: {content}, inner exception {inner}'
        super().__init__(self.message)


class NotExpensesException(Exception):
    def __init__(self):
        super().__init__(f'The message is not a valid expense')


class Category(Enum):
    HOUSING = 'HOUSING',
    TRANSPORTATION = 'TRANSPORTATION'
    FOOD = 'FOOD'
    UTILITIES = 'UTILITIES'
    INSURANCE = 'INSURANCE'
    MEDICAL_HEALTHCARE = 'MEDICAL/HEALTHCARE'
    SAVINGS = 'SAVINGS'
    DEBT = 'DEBT'
    EDUCATION = 'EDUCATION'
    ENTERTAINMENT = 'ENTERTAINMENT'
    OTHER = 'OTHER'

    @classmethod
    def of(cls, value):
        value = value.upper()
        for category in Category:
            if category.value == value:
                return category

        raise Exception(f'{value} is not a valid category')


@dataclass
class Expenses:
    expenses_id: int
    description: str
    amount: float
    category: Category
    added_at: datetime

    @classmethod
    def new(cls, description: str, amount: float, category: Category):
        return cls(None, description, amount, category, datetime.now())


class ExpensesService:
    @abstractmethod
    def create(self, message: str) -> Expenses:
        pass
