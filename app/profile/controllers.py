from app.profile.repos import UserRepo


def display(user_id):
    user = UserRepo.get_user_by_id(user_id)
    return user.to_json(), 200
