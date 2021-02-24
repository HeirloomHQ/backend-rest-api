from enum import Enum, auto
from app.infra.models.memorial import Memorial
from app.infra.models.role import Role


# Class to organize operations related to a user
class MemorialRepo:

    @staticmethod
    def create(first_name, last_name, description,
               born, died,
               bio, home_town,
               cover_photo, page_theme
               ) -> Memorial:
        memorial = Memorial(
            first_name=first_name,
            last_name=last_name,
            description=description,
            born=born, died=died,
            bio=bio, home_town=home_town,
            cover_photo=cover_photo,
            page_theme=page_theme
        )
        memorial.save()
        return memorial

    @staticmethod
    def get_by_id(memorial_id) -> [Memorial]:
        memorial_list = Memorial.objects(id=memorial_id)
        return memorial_list[0] if len(memorial_list) > 0 else None

    @staticmethod
    def get_by_user_id(user_id) -> ([Memorial], [Role]):
        roles = Role.objects(user=user_id)

        memorial_ids = [role.memorial for role in roles]
        memorials = Memorial.objects(id__in=memorial_ids)

        return memorials, roles


class RoleTypes(Enum):
    """
    This class represents the roles for a user in a memorial
    * CREATOR = highest permission level
    * MEMBER = lowest permission level
    """
    OWNER = auto()
    MANAGER = auto()
    MEMBER = auto()


# Class to organize roles
class RoleRepo:

    @staticmethod
    def get_by_user_id(id) -> Role:
        role_list = Role.objects(user=id)
        return role_list[0] if len(role_list) > 0 else None

    @staticmethod
    def create(role, user, memorial) -> Role:
        role = Role(role=role, user=user, memorial=memorial)
        role.save()
        return role
