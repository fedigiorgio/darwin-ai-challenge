from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import MONEY

Base = declarative_base()


class ExpensesModel(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String)
    amount = Column(MONEY)
    category = Column(String)
    added_at = Column(DateTime)


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String)
    expenses = relationship('ExpensesModel', backref='expenses', cascade='all, delete-orphan')

