from src.core.domain.expenses import Expenses
from src.core.domain.user import UsersRepository


class GetExpenses:
    def __init__(self, users_repository: UsersRepository):
        self._users_repository = users_repository

    def execute(self, telegram_id: str) -> list[Expenses]:
        user = self._users_repository.get(telegram_id)
        return user.expenses
