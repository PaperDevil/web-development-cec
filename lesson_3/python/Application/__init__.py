from flask import Flask

from Application.hashmap import hashmap_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(hashmap_bp)

    return app