from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('root', __name__)

@bp.route('/', methods=["GET"])
def index():
    return { "message": "Hello, World!" }

@bp.route('/<name>', methods=["GET"])
@jwt_required
def hello_name(name):
    user_id = get_jwt_identity()
    return { "message": "Hello, {0}, your user id is {1}!".format(name, user_id) }
