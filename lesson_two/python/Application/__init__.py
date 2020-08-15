from flask import Flask
from Application.routes import router
from Application.todos import todos_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(router)
    app.register_blueprint(todos_bp)

    return app