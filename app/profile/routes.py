from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.profile import controllers

user_bp = Blueprint('user', __name__, url_prefix='/profile')


@user_bp.route('', methods=['GET'])
@jwt_required()
def user():
    user_id = get_jwt_identity()
    response, code = controllers.display(user_id)

    if code != 200:
        return {"msg": response}, code

    return {"user": response}, 200
