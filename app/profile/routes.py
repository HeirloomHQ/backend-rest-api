from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.profile import controllers

user_bp = Blueprint('user', __name__, url_prefix='/profile')


@user_bp.route('', methods=['GET'])
@jwt_required
def user():
    user_id = get_jwt_identity()
    response, code = controllers.display(user_id)

    if code != 200:
        return jsonify({"msg": response}), code

    return jsonify({"user": response}), 200
