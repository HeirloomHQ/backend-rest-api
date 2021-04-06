from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    set_access_cookies, set_refresh_cookies, unset_jwt_cookies,
    jwt_required, get_jwt_identity
)
from app.auth import controllers
from app.constants import MAX_REFRESH

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
        "accept_invite": request.json.get('acceptInvite', None)
    }

    controller_response, code = controllers.signup(**kwargs)

    if code != 200:
        return {"msg": controller_response}, code

    api_response = jsonify({"user": controller_response})

    # Identity can be any data that is json serializable
    identity = controller_response["id"]
    access_token = create_access_token(identity=identity)
    refresh_token = create_refresh_token(identity=identity)

    set_access_cookies(api_response, access_token)
    set_refresh_cookies(api_response, refresh_token, max_age=MAX_REFRESH)

    return api_response, 200


@auth_bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    controller_response, code = controllers.login(email, password)
    if code != 200:
        return {"msg": controller_response}, code

    api_response = jsonify({"user": controller_response})

    # Identity can be any data that is json serializable
    identity = controller_response["id"]
    access_token = create_access_token(identity=identity)
    refresh_token = create_refresh_token(identity=identity)

    set_access_cookies(api_response, access_token)
    set_refresh_cookies(api_response, refresh_token, max_age=MAX_REFRESH)
    return api_response, 200

@auth_bp.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh():
    # Create the new access token
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id)

    # Set the access JWT and CSRF double submit protection cookies
    # in this response
    resp = jsonify({'refresh': True})
    set_access_cookies(resp, access_token)
    return resp, 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200
