from mongoengine import Document, StringField


class Memorial(Document):
    memorial_id = StringField(primary_key=True)
    creator_email = StringField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    description = StringField(max_length=140)

    def to_json(self, *args, **kwargs):
        return {
            "memorial_id" : self.memorial_id,
            "creator_email" : self.creator_email,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "description" : self.description
        }
    #Todo: Memories - Need to find out more componenets
    # that will be required