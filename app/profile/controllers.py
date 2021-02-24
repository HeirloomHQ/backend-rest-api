import uuid
from app.profile.repos import UserRepo
from app.auth import utils


def display(user_id):
    return UserRepo.get_user_by_id(user_id)
