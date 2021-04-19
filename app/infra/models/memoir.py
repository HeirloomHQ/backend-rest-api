from mongoengine import Document, StringField, ObjectIdField


class Memoir(Document):
    memorial = ObjectIdField()
    creator = ObjectIdField(null=True)
    text = StringField()
    creation_date = StringField()
    last_updated = StringField()
    media_url = StringField()

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "memorial": str(self.memorial),
            "creator": str(self.creator),
            "text": str(self.text),
            "creationDate": str(self.creation_date),
            "lastUpdated": str(self.last_updated),
            "mediaUrl": str(self.media_url)
        }
