from flask import Blueprint, request
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity
from app.memorial.controllers import display
from app.memorial.controllers.create import create

memorial_bp = Blueprint('memorial', __name__, url_prefix="/memorials")

@memorial_bp.route('/<memorial_id>', methods=['GET'])
@jwt_optional
def memorials(memorial_id):
    user_id = get_jwt_identity()
    response, code = display.display_single_memorial_for_user(user_id, memorial_id)

    if code != 200:
        return {"msg": response}, code

    memorial, role= response

    return {"memorial": memorial, "role": role}, 200

@memorial_bp.route('', methods=['GET', 'POST'])
@jwt_required
def memorial():
    if request.method == "GET":
        user_id = get_jwt_identity()
        response, code = display.display_all_user_memorials(user_id)

        if code != 200:
            return {"msg": response}, code

        memorials, roles = response

        return {"memorials": memorials, "roles": roles}, 200

    else:
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400

        kwargs = {
            "creator_id": get_jwt_identity(),
            "first_name": request.json.get("firstName", None),
            "last_name": request.json.get("lastName", None),
            "description": request.json.get("description", None),
        }

        response, code = create(**kwargs)

        if code != 200:
            return {"msg": response}, code

        return {"memorial": response}, 200
