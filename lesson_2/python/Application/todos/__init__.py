from flask import Blueprint, jsonify, request

todos_bp = Blueprint("todos", __name__, url_prefix="/todo")

class Todo:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def serialize(self):
        return {
            'title': self.title, 
            'description': self.description,
        }

todos = []

@todos_bp.route("/add", methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = Todo (
        title = data['title'],
        description = data['description']
    )
    todos.append(todo)
    return jsonify(todo.serialize())

@todos_bp.route("/", methods=['GET'])
def show_todos():
    return jsonify([todo.serialize() for todo in todos])