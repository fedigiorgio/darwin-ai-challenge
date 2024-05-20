from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class User:
    user_id: int
    telegram_id: str


@dataclass
class Expenses:
    description: str
    amount: Decimal
    category: str
    added_at: datetime
