from src.core.domain.expenses import Expenses, ExpensesService
from src.core.domain.user import UsersRepository


class AddExpenses:
    def __init__(self, users_repository: UsersRepository,
                 expenses_service: ExpensesService):
        self._users_repository = users_repository
        self._expenses_service = expenses_service

    def execute(self, telegram_id: str, message: str) -> Expenses:
        user = self._users_repository.get(telegram_id)
        expenses = self._expenses_service.create(message)

        user.add_expenses(expenses)
        self._users_repository.save(user)

        return expenses
