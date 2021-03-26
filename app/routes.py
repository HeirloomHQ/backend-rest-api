from flask import Blueprint, request
from app.memorial.utils import allowed_file
from app.constants import ALLOWED_EXTENSIONS, IMG_TMP_UPLOAD
from os import path


bp = Blueprint('root', __name__)

@bp.route('/', methods=["GET"])
def index():
    return { "message": "Hello, World!" }

@bp.route('/image', methods=['POST'])
def upload():
    if "img" not in request.files:
        return {"msg": "image was not present in body"}, 400

    file = request.files["img"]
    if file.filename == "":
        return {"msg": "no selected file"}, 400
    if not allowed_file(file.filename):
        return {"msg": "img must be of type: " + str(ALLOWED_EXTENSIONS)}, 400

    # save file to temp folder
    img_url = path.join(IMG_TMP_UPLOAD, file.filename)
    file.save(img_url)

    return {"imageURL": img_url}, 201

