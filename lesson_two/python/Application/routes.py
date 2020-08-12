from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/")
def index():
    return "Привет Мир!"