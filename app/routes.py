from flask import Blueprint

bp = Blueprint('root', __name__)

@bp.route('/', methods=["GET"])
def index():
    return { "message": "Hello, World!" }

@bp.route('/<name>', methods=["GET"])
def hello_name(name):
    return { "message": "Hello, {0}!".format(name) }
