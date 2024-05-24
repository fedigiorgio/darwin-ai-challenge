from src.core.domain.user import UsersRepository, User


class AddUser:
    def __init__(self, users_repository: UsersRepository):
        self._users_repository = users_repository

    def execute(self, telegram_id: str):
        user = User.new(telegram_id)
        self._users_repository.add(user)