from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.memorial.controllers import display, create, edit

memorial_bp = Blueprint('memorial', __name__, url_prefix="/memorials")


@memorial_bp.route('/<memorial_id>', methods=['GET'])
@jwt_required(optional=True)
def memorials(memorial_id):
    user_id = get_jwt_identity()
    response, code = display.display_single_memorial_for_user(user_id, memorial_id)

    if code != 200:
        return {"msg": response}, code

    memorial, role = response

    return {"memorial": memorial, "role": role}, 200


@memorial_bp.route('', methods=['GET', 'POST'])
@jwt_required()
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
            "born": request.json.get("born", None),
            "died": request.json.get("died", None),
            "bio": request.json.get("bio", None),
            "home_town": request.json.get("homeTown", None),
            "cover_photo": request.json.get("coverPhoto", None),
            "page_theme": request.json.get("pageTheme", None),
        }

        response, code = create.create(**kwargs)

        if code != 201:
            return {"msg": response}, code

        return {"memorial": response}, 201


@memorial_bp.route('/<memorial_id>/settings', methods=['PUT'])
@jwt_required()
def settings(memorial_id):
    user_id = get_jwt_identity()
    kwargs = {
        "first_name": request.json.get("firstName", None),
        "last_name": request.json.get("lastName", None),
        "description": request.json.get("description", None),
        "born": request.json.get("born", None),
        "died": request.json.get("died", None),
        "bio": request.json.get("bio", None),
        "home_town": request.json.get("homeTown", None),
        "cover_photo": request.json.get("coverPhoto", None),
        "page_theme": request.json.get("pageTheme", None),
        "can_post": request.json.get("canPost", None),
        "can_view": request.json.get("canView", None),
        "can_manage": request.json.get("canManage", None),
        "can_delete": request.json.get("canDelete", None)
    }
    response, code = edit.edit_memorial(user_id, memorial_id, **kwargs)

    if code != 200:
        return {"msg": response}, code

    return {"memorial": response}, 200


@memorial_bp.route('/members/<memorial_id>', methods=['GET'])
@jwt_required(optional=True)
def members(memorial_id):
    user_id = get_jwt_identity()
    response, code = display.display_members_for_single_memorial(user_id, memorial_id)
    members_response = response
    return {"Members": members_response}, 200
