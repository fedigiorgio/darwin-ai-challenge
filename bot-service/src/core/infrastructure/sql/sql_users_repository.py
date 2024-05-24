from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import joinedload

from src.core.domain.expenses import Expenses, Category
from src.core.domain.user import UsersRepository, User, UserNotExistsException
from src.core.infrastructure.sql.models import UserModel, ExpensesModel


class SqlUsersRepository(UsersRepository):
    def __init__(self, session):
        self._session = session

    def get(self, telegram_id: str) -> User:
        try:
            user_model = self._session.query(UserModel).options(joinedload(UserModel.expenses)).filter(
                UserModel.telegram_id == telegram_id).one()
            return self._model_to_domain_user(user_model)
        except NoResultFound:
            raise UserNotExistsException(telegram_id)

    def save(self, user: User):
        user_model = self._domain_to_model_user(user)
        self._session.merge(user_model)
        self._session.commit()

    @staticmethod
    def _domain_to_model_user(user: User) -> UserModel:
        return UserModel(
            id=user.user_id,
            telegram_id=user.telegram_id,
            expenses=[ExpensesModel(
                id=expense.expenses_id,
                user_id=user.user_id,
                description=expense.description,
                amount=expense.amount,
                category=expense.category.value,
                added_at=expense.added_at
            ) for expense in user.expenses]
        )

    def _model_to_domain_user(self, user_model: UserModel) -> User:
        return User(
            user_id=user_model.id,
            telegram_id=user_model.telegram_id,
            expenses=[Expenses(
                expenses_id=expense.id,
                description=expense.description,
                amount=self._to_float(expense.amount),
                category=Category.of(expense.category),
                added_at=expense.added_at
            ) for expense in user_model.expenses]
        )

    @staticmethod
    def _to_float(value):
        return float(''.join(c for c in value if c.isdigit() or c == '.'))
