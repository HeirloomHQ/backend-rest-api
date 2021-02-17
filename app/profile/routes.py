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

# need to decide route for creating account (?)
@user_bp.route('', methods=["POST"])
@jwt_required
def create_account():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    kwargs = {
        "email": request.json.get("email", None),
        "first_name": request.json.get("first_name", None),
        "last_name": request.json.get("last_name", None),
        "password_hash": request.json.get("password_hash", None),
        "salt": request.json.get("salt", None),
    }

    response, code = controllers.create(**kwargs)

    if code != 200:
        return jsonify({"msg", response}), code

    return jsonify({"user": response}), 200