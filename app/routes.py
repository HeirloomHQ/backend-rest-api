from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.memorial.utils import allowed_file
from app.constants import ALLOWED_EXTENSIONS
from app.services import aws


bp = Blueprint('root', __name__)


@bp.route('/', methods=["GET"])
def index():
    return { "message": "Hello, World!" }


@bp.route('/image', methods=['POST'])
@jwt_required()
def upload():
    if "img" not in request.files:
        return {"msg": "image was not present in body"}, 400

    file = request.files["img"]
    if file.filename == "":
        return {"msg": "no selected file"}, 400
    if not allowed_file(file.filename):
        return {"msg": "img must be of type: " + str(ALLOWED_EXTENSIONS)}, 400

    # save to aws
    img_url = aws.upload_file(file.filename, file)
    if img_url is None:
        return {"msg": "server error"}, 500

    return {"imageURL": img_url}, 201

