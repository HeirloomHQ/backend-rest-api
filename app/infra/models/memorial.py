from mongoengine import Document, StringField


class Memorial(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    description = StringField(max_length=140)

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "firstName": self.first_name,
            "lastName": self.last_name,
            "description": self.description
        }