import json

from flask import Flask


app = Flask(__name__)

@app.route("/")
def index() -> str:
    """Стартовая страница приложения"""
    return "Привет мир!"

@app.route("/user/<username>")
def get_user(username: str) -> str:
    """Страница приветствия Юзера"""
    return f"Привет, {username}!"

@app.route("/user/get/<username>")
def get_json_user(username: str) -> str:
    """Получение JSON с именем юзера"""
    return json.dumps({
        "username": username
    })

@app.route("/user/update/<username>", methods=['POST'])
def update_user(username: str) -> str:
    """Метод, к которому мы не получим доступ"""
    return "Какое-то действие с юзером"


if __name__ == "__main__":
    app.run("127.0.0.1", 8000, debug=True)