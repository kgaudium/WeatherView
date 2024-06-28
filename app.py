from flask import Flask
from waitress import serve
import os
from dotenv import load_dotenv

app = Flask(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')


def load_project_dotenv():
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    serve(app, host="127.0.0.1", port=5000)
