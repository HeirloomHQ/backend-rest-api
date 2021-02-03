from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.auth import controllers

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")


@auth_bp.route('/signup', methods=["POST"])
def index():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    kwargs = {
        "email": request.json.get('email', None),
        "password": request.json.get('password', None),
        "first_name": request.json.get('firstName', None),
        "last_name": request.json.get('lastName', None),
    }

    response, code = controllers.signup(**kwargs)

    if code != 200:
        return jsonify({"msg": response}), code

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=response["user_id"])
    return jsonify({"access_token": access_token, "user": response}), 200


@auth_bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    response, code = controllers.login(email, password)
    if code != 200:
        return jsonify({"msg": response}), code

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=response["user_id"])
    return jsonify({"access_token": access_token, "user": response}), 200
