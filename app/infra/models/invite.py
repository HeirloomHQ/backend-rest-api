from mongoengine import Document, StringField, ObjectIdField


class Invite(Document):
    memorial = ObjectIdField()
    inviter_id = ObjectIdField()
    invitee_email = StringField()
    token = StringField()
    user = ObjectIdField(null=True)

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "inviterId": str(self.inviter_id),
            "inviteeEmail": str(self.invitee_email),
            "memorial": str(self.memorial)
        }
