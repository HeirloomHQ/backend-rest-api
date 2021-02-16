from mongoengine import Document, StringField, ObjectIdField, EnumField


class Role(Document):
    role_id = StringField(primary_key=True)
    memorial = ObjectIdField()
    user = ObjectIdField()
    role = EnumField([
        "creator",
        "manager",
        "member",
    ])
