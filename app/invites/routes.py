from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.invites.controllers import create

invite_bp = Blueprint('invites', __name__, url_prefix="/invites")


@invite_bp.route('/<invite_id>/activation', methods=['GET'])
@jwt_required()
def activate_invite():
    # do activate invite stuff

    return {"msg": "good to go"}, 200


@invite_bp.route('', methods=['POST'])
@jwt_required()
def send_invite():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    kwargs = {
        "inviter_id": get_jwt_identity(),
        "memorial_id": request.args.get("memorial", None),
        "emails": request.json.get("emails", []),
    }

    response, code = create.invite(**kwargs)

    if code != 202:
        return {"msg": response}, code

    return {"msg": response}, 202
