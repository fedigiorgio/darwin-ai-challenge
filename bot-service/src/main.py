import logging

from src import app

logging.basicConfig(level='INFO', format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':

    app.run(debug=True)
