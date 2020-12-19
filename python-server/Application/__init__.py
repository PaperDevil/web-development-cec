from flask import Flask, jsonify, request
from flask_cors import CORS
from Application.models import TodoItem

todos = []

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/', methods=['GET'])
    def index():
        return jsonify([todo.serialize() for todo in todos])

    @app.route('/', methods=['POST'])
    def add():
        data = request.get_json()
        print(data)
        item = TodoItem(text=data['text'], index=len(todos), is_complete = False)
        todos.append(item)
        return "200"

    @app.route('/<number>', methods=['POST'])
    def return_todo(number):
        todos[number].is_complete = !todos[number].is_complete
        return "200"

    return app