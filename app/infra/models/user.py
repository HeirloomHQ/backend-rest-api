from mongoengine import Document, StringField


class User(Document):
    email = StringField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    password_hash = StringField(required=True)
    salt = StringField(required=True)

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "email": self.email,
            "firstName": self.first_name,
            "lastName": self.last_name
        }
