from mongoengine import Document, StringField, ObjectIdField


class Memoir(Document):
    memorial = ObjectIdField()
    creator = ObjectIdField(null=True)
    text = StringField()
    creation_date = StringField()
    last_updated = StringField()

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "memorial": str(self.memorial),
            "creator": str(self.creator),
            "text": str(self.text),
            "creation_date": str(self.creation_date),
            "last_updated": str(self.last_updated)
        }
