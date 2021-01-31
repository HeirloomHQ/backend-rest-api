from mongoengine import Document, StringField

class User(Document):
    user_id = StringField(primary_key=True)
    email = StringField(required=True, unique=True)
    password_hash = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
