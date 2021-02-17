from mongoengine import Document, EmbeddedDocument, StringField, EmbeddedDocumentField


class PageSettings(EmbeddedDocument):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    description = StringField(max_length=140)

    def to_json(self, *args, **kwargs):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "description": self.description
        }


class PrivacySettings(EmbeddedDocument):
    can_post = StringField(default="CREATOR")
    can_view = StringField(default="CREATOR")
    can_manage = StringField(default="CREATOR")
    can_edit_privacy = StringField(default="CREATOR")

    def to_json(self, *args, **kwargs):
        return {
            "canPost": self.can_post,
            "canView": self.can_view,
            "canManage": self.can_manage,
            "canEditPrivacy": self.can_edit_privacy
        }


class Memorial(Document):
    page_settings = EmbeddedDocumentField(PageSettings)
    privacy_settings = EmbeddedDocumentField(PrivacySettings)

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "pageSettings": self.page_settings.to_json(),
            "privacySettings": self.privacy_settings.to_json()
        }
