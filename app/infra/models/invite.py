from mongoengine import Document, StringField, ObjectIdField, BooleanField


class Invite(Document):
    memorial = ObjectIdField()
    inviter_id = ObjectIdField()
    invitee_email = StringField()
    token = StringField()
    user = ObjectIdField(null=True)

    expiration_date = StringField()
    accepted = BooleanField(default=False)

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "inviterId": str(self.inviter_id),
            "inviteeEmail": str(self.invitee_email),
            "memorial": str(self.memorial),
            "expirationDate": self.expiration_date,
            "accepted": self.accepted
        }
