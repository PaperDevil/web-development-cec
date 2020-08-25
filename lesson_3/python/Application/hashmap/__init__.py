from flask import Blueprint, jsonify, request


hashmap_bp = Blueprint('recipes', __name__, url_prefix='/hashmap')

vault = {}

@hashmap_bp.route('/set', methods=['POST'])
def set_item():
    data = request.get_json()
    vault[data['key']] = data['value']
    return jsonify({
        "key": data['key'],
        "value": data['value']
    })

@hashmap_bp.route('/get', methods=['GET'])
def get_item():
    data = request.get_json()
    return jsonify(
        vault[data['key']]
    )

@hashmap_bp.route('/items', methods=['GET'])
def get_items():
    return jsonify(vault)