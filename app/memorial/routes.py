from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.memorial import controllers

memorial_bp = Blueprint('memorial', __name__)


@memorial_bp.route('/memorial/view/<creator_email>', methods=['GET'])
def memorials(creator_email):
    # if not request.is_json:
    #     return {"msg": "Missing JSON in request"}, 400
    response, code = controllers.display(creator_email)

    if code != 200:
        return jsonify({"msg": response}), code

        # Todo: Need to figure out authentication requirements
        # # Identity can be any data that is json serializable
        # access_token = create_access_token(identity=kwargs["email"])
        # return jsonify({"access_token": access_token, "user": response}), 200

    return jsonify({"memorial": response}), 200

@memorial_bp.route('/memorial/create', methods=["POST"])
def index():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    kwargs = {
        "creator_email": request.json.get("creator_email", None),
        "first_name": request.json.get("first_name", None),
        "last_name": request.json.get( "last_name", None),
        "description": request.json.get("description", None),
    }

    response, code = controllers.create(**kwargs)

    if code != 200:
        return jsonify({"msg": response}), code

    # Todo: Need to figure out authentication requirements
    # # Identity can be any data that is json serializable
    # access_token = create_access_token(identity=kwargs["email"])
    # return jsonify({"access_token": access_token, "user": response}), 200

    return jsonify({"memorial": response}), 200
