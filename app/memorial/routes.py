from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.memorial import controllers

memorial_bp = Blueprint('memorial', __name__)


@memorial_bp.route('/memorial/<creator_email>', methods=['GET'])
@jwt_required
def memorials(creator_email):
    response, code = controllers.display(creator_email)

    if code != 200:
        return jsonify({"msg": response}), code

        # Todo: Need to figure out authentication requirements

    return jsonify({"memorial": response}), 200

@memorial_bp.route('/memorial', methods=["POST"])
@jwt_required
def create_memorials():
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

    return jsonify({"memorial": response}), 200
