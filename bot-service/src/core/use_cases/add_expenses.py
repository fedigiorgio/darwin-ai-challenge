from datetime import datetime
from decimal import Decimal

from src.core.domain.models import Expenses


def add_expenses(telegram_id: str, message: str) -> Expenses:
    print(f'telegram_id {telegram_id}, message {message}')
    return Expenses("Nintendo Switch", Decimal('500'), "VideoGames", datetime.now())
