from flask import Flask

app = Flask(__name__)

from src.routes import expenses_routes