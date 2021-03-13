from flask import Flask, jsonify

try:
    from server.api import API
    from server.bp_api import create_bp
    from server.db import configure
except Exception as erro:
    print("Erro em import: {}".format(erro))
    from .server.api import API
    from .server.bp_api import create_bp
    from .server.db import configure

from os import getpid
from pprint import pprint
from time import sleep
from random import random
from multiprocessing import Pool


def func(n):
    print(f"Processo {n}")
    sleep(random() / 10)
    return {n + 1: getpid()}


def create_app():
    app = Flask(__name__)
    bp = create_bp("/api")
    app.register_blueprint(bp)

    @app.route("/<name>:str")
    def nome(name):
        print(name)
        return jsonify(name)

    @app.route("/<n>")
    def home(n):
        n = int(n)
        workers = Pool(3)
        response = workers.map(func, range(n))
        pprint(response)
        print("Dentro da funcao")
        return jsonify({"nome": response})

    return app


if __name__ == "__main__":
    app = create_app()
    app.debug = True
    app.run()