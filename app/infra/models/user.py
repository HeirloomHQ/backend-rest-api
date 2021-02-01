from mongoengine import Document, StringField


class User(Document):
    user_id = StringField(primary_key=True)
    email = StringField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    password_hash = StringField(required=True)
    salt = StringField(required=True)

    def to_json(self, *args, **kwargs):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
