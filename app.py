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


def create_app():
    app = Flask(__name__)
    bp = create_bp("/api")
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.debug = True
    app.run()