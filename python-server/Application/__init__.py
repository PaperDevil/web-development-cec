from flask import Flask, jsonify, request
from Application.models import TodoItem

todos = []

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return jsonify([todo.serialize() for todo in todos])

    @app.route('/', methods=['POST'])
    def add():
        data = request.get_json()
        item = TodoItem(text=data['text'], index=len(todos))
        todos.append(item)
        return "200"

    return app