from flask import Blueprint, request, jsonify
import json

bp = Blueprint('root', __name__)

@bp.route('/', methods=["GET"])
def index():
    return { "message": "Hello, World!" }

@bp.route('/<name>', methods=["GET"])
def hello_name(name):
    return { "message": "Hello, {0}!".format(name) }

#Playing with routing calls Source: https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request

#Login route
@bp.route('/auth/login',methods=["POST"])
def login():
    data = request.json
    return jsonify(data)

#Signup route
@bp.route('/auth/signup',methods=["POST"])
def signup():
    data = request.json
    return jsonify(data)

#validate e-mail route
@bp.route('/auth/validateEmail', methods=["POST"])
def validate():
    data = request.json
    if data:
        #do some validation here for existing emails later.
        if (data['email'] == 'jgaldamez102@gmail.com'):
            return "used"
        else:
            return "unused"