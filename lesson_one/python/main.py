import json

from flask import Flask, jsonify


app = Flask(__name__)  # Создание экземпляра приложения

@app.route("/", methods=['GET'])
def index() -> str:
    """Стартовая страница приложения"""
    return "Привет мир!"

@app.route("/user/<username>", methods=['GET'])
def get_user(username: str) -> str:
    """Страница приветствия Юзера"""
    return f"Привет, {username}!"

@app.route("/user/<username>/get", methods=['GET'])
def get_json_user(username: str) -> str:
    """Получение JSON с именем юзера"""
    return jsonify({
        "username": username
    })

@app.route("/user/<username>/update", methods=['POST'])
def update_user(username: str) -> str:
    """Метод, к которому мы не получим доступ"""
    return "Какое-то действие с юзером"


if __name__ == "__main__":
    app.run("127.0.0.1", 8000, debug=True)