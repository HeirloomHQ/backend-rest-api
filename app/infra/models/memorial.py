from mongoengine import Document, StringField


class Memorial(Document):
    memorial_id = StringField(primary_key=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    description = StringField(max_length=140)
