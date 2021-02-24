import bcrypt
import uuid
from app.profile.repos import UserRepo
from app.auth import utils


def signup(email, password, first_name, last_name):
    # validate input
    user = {"email": email, "password": password}
    for field, value in user.items():
        if value is None:
            return "Missing {} parameter".format(field), 400

    if not utils.is_email(email):
        return "Email must be an actual email", 400

    # reject if user email exists
    already_exists = UserRepo.get_user_by_email(email)
    if already_exists != None:
        return "User with email {} already exists".format(email), 400

    # lets hash this boi
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    user_to_save = {
        "email": email, "first_name": first_name, "last_name": last_name,
        "password_hash": password_hash, "salt": salt
    }

    # create user
    saved_user = UserRepo.create(**user_to_save)
    return saved_user.to_json(), 200


def login(email, password):
    if not email:
        return {"msg": "Missing email parameter"}, 400
    if not password:
        return {"msg": "Missing password parameter"}, 400

    user = UserRepo.get_user_by_email(email)
    if user == None:
        return "Wrong email or password", 401

    does_password_match = bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8'))
    if not does_password_match:
        return "Wrong email or password", 401

    return user.to_json(), 200
