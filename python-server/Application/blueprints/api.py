from flask import Blueprint, request, jsonify
from Application.models import TodoItem

bp = Blueprint('todo', __name__)


@bp.route('/', methods=['GET'])
def health():
    return "OK", 200  # Этот метод предназначен для проверки активности сервера


@bp.route('/create', methods=['POST'])
def create_todo():
    data = request.get_json()
    item = TodoItem(text=data['text'])
    item.save()
    return jsonify({
        'text': item.text,
        'datetime': item.datetime_of_creation,
        'is_complete': item.is_complete,
        'is_delete': item.is_delete
    }), 200


@bp.route('/list', methods=['GET'])
def get_list_of_items():
    res = []
    for item in TodoItem.select():
        res.append({
            "id": item.id,
            "text": item.text,
            "datetime": item.datetime_of_creation,
            "is_complete": item.is_complete,
            "is_delete": item.is_delete
        })
    return jsonify(res), 200


@bp.route('/<int:index>', methods=['GET'])
def get_item_from_index(index: int):
    if index <= 0: return "Index must be bigger than zero!", 403
    try:
        item = TodoItem.select().where(TodoItem.id == index).get()
    except Exception: return f"Item with index {index} not found", 404
    return jsonify({
        'text': item.text,
        'datetime': item.datetime_of_creation,
        'is_complete': item.is_complete,
        'is_delete': item.is_delete
    }), 200


@bp.route('/complete/<int:index>', methods=['POST'])
def set_item_complete(index: int):
    if index <= 0: return "Index must be bigger than zero!", 403
    try:
        item = TodoItem.select().where(TodoItem.id == index).get()
    except Exception: return f"Item with index {index} not found", 404
    item.is_complete = not item.is_complete
    item.save()
    return jsonify({
        'text': item.text,
        'datetime': item.datetime_of_creation,
        'is_complete': item.is_complete,
        'is_delete': item.is_delete
    }), 200


@bp.route('/delete/<int:index>', methods=['DELETE'])
def set_item_delete(index: int):
    if index <= 0: return "Index must be bigger than zero!", 403
    try:
        item = TodoItem.select().where(TodoItem.id == index).get()
    except Exception: return f"Item with index {index} not found", 404
    item.is_delete = not item.is_delete
    item.save()
    return jsonify({
        'text': item.text,
        'datetime': item.datetime_of_creation,
        'is_complete': item.is_complete,
        'is_delete': item.is_delete
    }), 200
