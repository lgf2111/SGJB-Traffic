from flask import Flask
from threading import Thread


app = Flask(__name__)

from webapp import routes


def run():
    app.run(host="0.0.0.0", port=8080)


def flask_run():
    t = Thread(target=run)
    t.start()
