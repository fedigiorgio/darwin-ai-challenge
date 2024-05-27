import logging

from flask import Flask

from src.routes.expenses_routes import bp

app = Flask(__name__)
app.register_blueprint(bp)

logging.basicConfig(level='INFO', format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    app.run()
