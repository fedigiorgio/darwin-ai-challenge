from src.core.domain.user import UsersRepository, User


class SqlUsersRepository(UsersRepository):
    def get(self, telegram_id: str) -> User:
        return User(1, "my_telegram_id", [])

    def save(self, user: User):
        pass
