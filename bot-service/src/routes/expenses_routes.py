from http import HTTPStatus

from flask import jsonify, request

from src.core.use_cases.add_expenses import add_expenses
from src.main import app


@app.route('/api/expenses', methods=['POST'])
def add_expenses_route():
    body = request.get_json()
    telegram_id = body['telegram_id']
    message = body['message']
    test_expenses = add_expenses(telegram_id, message)
    return jsonify(test_expenses), HTTPStatus.CREATED
