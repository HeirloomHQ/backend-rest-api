from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.profile import controllers

user_bp = Blueprint('user', __name__)

@user_bp.route('/auth/profile', methods=['GET'])
@jwt_required
def user(user_email):
    response, code = controllers.display(user_email)

    if code != 200:
        return jsonify({"msg": response}), code

    return jsonify({"user": response}), 200