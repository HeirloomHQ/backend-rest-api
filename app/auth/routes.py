from flask import Blueprint, abort
from ..infra.models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")


@auth_bp.route('/login', methods=["POST"])
def index():
    try:
        user = User.objects.get(email="manzanero.andrew@gmail.com")
    except:
        abort(404)
    return {"user": user}

@auth_bp.route('/signup', methods=["POST"])
def index():
    return {"user": None}
