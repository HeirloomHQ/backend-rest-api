from mongoengine import Document, StringField, ObjectIdField


class Role(Document):
    memorial = ObjectIdField()
    user = ObjectIdField()
    role = StringField()

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "memorial": str(self.memorial),
            "user": str(self.user),
            "role": self.role
        }
