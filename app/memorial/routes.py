from flask import Blueprint, request, jsonify, Flask
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.auth import controllers

memorial_bp = Blueprint('memorial', __name__, url_prefix="/memorial")
#
mem_list = [
    {
        "id": 0,
        "Creator": "Buchi O",
        "Info": "Jane Doe",
        "Date": "February 3, 2021"
    },
    {
        "id": 1,
        "Creator": "Andrew M",
        "Info": "John Doe",
        "Date": "February 1, 2021"
    },
    {
        "id": 2,
        "Creator": "Mark P",
        "Info": "Jimmy Doe",
        "Date": "January 3, 2021"
    },
]


#
#
@memorial_bp.route('/memorials', methods=['GET', 'POST'])
def memorials():
    # if not request.is_json:
    #     return {"msg": "Missing JSON in request"}, 400

    if request.method == 'GET':
        if len(mem_list) > 0:
            return jsonify(mem_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        ID = mem_list[-1]['id'] + 1
        new_creator = request.form['Creator']
        new_info = request.form['Info']
        new_date = request.form['Date']

        new_obj = {
            "id": ID,
            "Creator": new_creator,
            "Info": new_info,
            "Date": new_date
        }

        mem_list.append(new_obj)
        return jsonify(mem_list), 201

