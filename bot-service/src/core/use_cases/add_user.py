from src.core.domain.user import UsersRepository, User


class AddUser:
    def __init__(self, users_repository: UsersRepository):
        self._users_repository = users_repository

    def execute(self, telegram_id: str):
        self._check_user_not_exists(telegram_id)
        user = User.new(telegram_id)
        self._users_repository.add(user)

    def _check_user_not_exists(self, telegram_id):
        if self._users_repository.exists(telegram_id):
            raise UserAlreadyExistsException(telegram_id)
