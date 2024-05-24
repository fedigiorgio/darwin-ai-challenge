from sqlalchemy.orm import joinedload

from src.core.domain.expenses import Expenses, Category
from src.core.domain.user import UsersRepository, User
from src.core.infrastructure.sql.models import UserModel, ExpensesModel


class SqlUsersRepository(UsersRepository):
    def __init__(self, session):
        self._session = session

    def get(self, telegram_id: str) -> User:
        user_model = self._session.query(UserModel).options(joinedload(UserModel.items)).filter(
            UserModel.telegram_id == telegram_id).one()
        return self._model_to_domain_user(user_model)

    def save(self, user: User):
        user_model = self._domain_to_model_user(user)
        self._session.merge(user_model)
        self._session.commit()

    @staticmethod
    def _domain_to_model_user(user: User) -> UserModel:
        return UserModel(
            id=user.user_id,
            telegram_id=user.telegram_id,
            items=[ExpensesModel(
                id=expense.expenses_id,
                user_id=user.user_id,
                description=expense.description,
                amount=float(expense.amount),
                category=expense.category.value,
                added_at=expense.added_at
            ) for expense in user.expenses]
        )

    @staticmethod
    def _model_to_domain_user(user_model: UserModel) -> User:
        return User(
            user_id=user_model.id,
            telegram_id=user_model.telegram_id,
            expenses=[Expenses(
                expenses_id=expense.id,
                description=expense.description,
                amount=expense.amount,
                category=Category.of(expense.category),
                added_at=expense.created_at
            ) for expense in user_model.items]
        )
