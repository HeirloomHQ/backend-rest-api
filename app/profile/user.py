from app.infra.models.user import User


class UserInfo:
    @staticmethod
    def get_user_by_id(id) -> User:
        user = User.objects(id=id)[0]
        return user

    @staticmethod
    def get_user_by_email(email) -> User:
        user = User.objects(email=email)
        return user[0] if len(user) else None

    @staticmethod
    def save(user_id, email, first_name, last_name, password_hash, salt) -> User:
        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name,
                    password_hash=password_hash, salt=salt)
        user.save()
        return user
