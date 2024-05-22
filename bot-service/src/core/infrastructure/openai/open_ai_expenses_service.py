from datetime import datetime
from decimal import Decimal

from src.core.domain.expenses import ExpensesService, Expenses


class OpenAIExpensesService(ExpensesService):
    def create(self, message: str) -> Expenses:
        return Expenses("Nintendo Switch", Decimal('500'), "VideoGames", datetime.now())