from mongoengine import (
     Document, EmbeddedDocument,
     StringField, EmbeddedDocumentField
)
import datetime


class PageSettings(EmbeddedDocument):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    description = StringField(max_length=140)
    born = StringField(max_length=80)
    died = StringField(max_length=80)
    bio = StringField(max_length=80)
    home_town = StringField(max_length=50)
    cover_photo = StringField(max_length=80)
    page_theme = StringField(max_length=10)

    def to_json(self, *args, **kwargs):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "description": self.description,
            "born": self.born,
            "died": self.died,
            "bio": self.bio,
            "homeTown": self.home_town,
            "coverPhoto": self.cover_photo,
            "pageTheme": self.page_theme
        }


class PrivacySettings(EmbeddedDocument):
    can_post = StringField(default="MANAGER")          # posting memories
    can_view = StringField(default="MANAGER")          # viewing a memorial (also used for taking online/offline)
    can_manage = StringField(default="MANAGER")        # managing a memorial's page settings
    can_edit_privacy = StringField(default="MANAGER")  # can edit privacy settings
    can_delete = StringField(default="OWNER")          # can delete an heirloom

    def to_json(self, *args, **kwargs):
        return {
            "canPost": self.can_post,
            "canView": self.can_view,
            "canManage": self.can_manage,
            "canEditPrivacy": self.can_edit_privacy,
            "canDelete": self.can_delete,
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
