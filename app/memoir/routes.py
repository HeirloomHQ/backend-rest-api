from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.memoir import controllers, utils
from datetime import datetime
from app.memorial.repos import MemorialRepo
import json

memoir_bp = Blueprint('memoir', __name__, url_prefix="/memoir")


# Get all memoirs in a memorial
@memoir_bp.route('/<memorial_id>/get', methods=["GET"])
@jwt_required()
def get_all(memorial_id):
    memorial_doc = MemorialRepo.get_by_id(memorial_id)
    if memorial_doc is None:
        return "Memorial not found", 404

    memoirs = utils.get_all_memoirs(memorial_id)

    return {"memoirs": memoirs}, 200


# Get a specific memoir in a memorial
@memoir_bp.route('/<memorial_id>/<memoir_id>/get', methods=["GET"])
@jwt_required()
def get(memorial_id, memoir_id):
    memorial_doc = MemorialRepo.get_by_id(memorial_id)
    if memorial_doc is None:
        return "Memorial not found", 404

    memoir = utils.get_memoir(memorial_id, memoir_id)

    if memoir is None:
        return "Memoir not found", 404

    return memoir.to_json(), 201


@memoir_bp.route('/<memorial_id>/add', methods=["GET"])
@jwt_required()
def add(memorial_id):
    user_id = get_jwt_identity()

    memorial_doc = MemorialRepo.get_by_id(memorial_id)
    if memorial_doc is None:
        return "Memorial not found", 404

    kwargs = {
        "memorial_id": memorial_id,
        "user_id": user_id,
        "text": request.json.get("text", None),
        "time": str(datetime.now())
    }
    response, code = controllers.add_memoir(**kwargs)

    if code != 201:
        return {"msg": response}, code

    return {"memoir": response}, 201


@memoir_bp.route('/<memorial_id>/<memoir_id>/edit', methods=["PUT"])
@jwt_required()
def edit(memorial_id, memoir_id):
    memorial_doc = MemorialRepo.get_by_id(memorial_id)
    if memorial_doc is None:
        return "Memorial not found", 404

    memoir = utils.get_memoir(memorial_id, memoir_id)
    if memoir is None:
        return "Memoir not found", 404

    user_id = get_jwt_identity()
    user = utils.same_user(memoir_id, user_id)
    if user is None:
        return "User isn't creator", 404

    kwargs = {
        "memorial_id": memorial_id,
        "memoir_id": memoir_id,
        "text": request.json.get("text", None),
        "time": str(datetime.now())
    }
    response, code = controllers.edit_memoir(**kwargs)

    if code != 201:
        return {"msg": response}, code

    return {"memoir": response}, 201


@memoir_bp.route('/<memorial_id>/<memoir_id>/remove', methods=["DELETE"])
@jwt_required()
def remove(memorial_id, memoir_id):
    memorial_doc = MemorialRepo.get_by_id(memorial_id)
    if memorial_doc is None:
        return "Memorial not found", 404

    memoir = utils.get_memoir(memorial_id, memoir_id)
    if memoir is None:
        return "Memoir not found", 404
    user_id = get_jwt_identity()

    response, code = controllers.remove_memoir(memorial_id, memoir_id, user_id)

    if code != 201:
        return {"msg": response}, code

    return {"msg": "Memoir has been deleted"}, 201
