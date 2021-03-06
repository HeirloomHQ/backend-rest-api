from app.infra.models.user import User


# Class to organize operations related to a user
class UserRepo:

    @staticmethod
    def get_user_by_id(id) -> User:
        users = User.objects(id=id)
        return users[0] if len(users) else None

    @staticmethod
    def get_user_by_email(email) -> User:
        users = User.objects(email=email)
        return users[0] if len(users) else None

    @staticmethod
    def create(email, first_name, last_name, password_hash, salt) -> User:
        user = User(email=email, first_name=first_name, last_name=last_name,
                    password_hash=password_hash, salt=salt)
        user.save()
        return user

# Create get by ids which takes in user ids and returns a list of users
    @staticmethod
    def get_users_by_ids(ids) -> [User]:
        users = User.objects(id__in=ids)
        return users
