import logging

from flask import Flask

from src.routes.expenses_routes import bp

app = Flask(__name__)
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run()
