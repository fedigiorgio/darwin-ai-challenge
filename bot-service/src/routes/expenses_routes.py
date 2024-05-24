import logging
from http import HTTPStatus

from flask import request, jsonify

from src import app
from src.core.domain.expenses import Expenses, NotExpensesException
from src.core.domain.user import UserNotExistsException
from src.modules import add_expenses


@app.route('/api/telegram-users/<telegram_id>/expenses', methods=['POST'])
def add_expenses_route(telegram_id):
    message = request.get_json()['message']

    try:
        logging.info(f'Received message: {message} from telegram_id: {telegram_id}')
        expenses = add_expenses.execute(telegram_id, message)
        return to_response(expenses)
    except UserNotExistsException as e:
        return handle_not_exists(e)
    except NotExpensesException:
        return handle_not_expenses(message, telegram_id)
    except Exception as e:
        return handle_unexpected_exception(e)


def handle_not_exists(e: UserNotExistsException):
    logging.warning(e)
    return jsonify({'error:': 'User is not authorized'}), HTTPStatus.UNAUTHORIZED


def handle_unexpected_exception(e):
    logging.error(e)
    return jsonify({'error:': 'Unexpected error'}), HTTPStatus.INTERNAL_SERVER_ERROR


def handle_not_expenses(message, telegram_id):
    logging.warning(f'Message {message} from telegram_id: {telegram_id} is not an expense.')
    return jsonify({'error:': f'Message {message} is not an expense'}), HTTPStatus.BAD_REQUEST


def to_response(expenses: Expenses):
    response_body = {
        'description': expenses.description,
        'amount': expenses.amount,
        'category': expenses.category.value
    }
    return jsonify(response_body), HTTPStatus.OK
