from enum import Enum, auto
from app.infra.models.memorial import Memorial
from app.infra.models.role import Role


# Class to organize operations related to a user
class MemorialRepo:

    @staticmethod
    def save(first_name, last_name, description) -> Memorial:
        memorial = Memorial(first_name=first_name, last_name=last_name, description=description)
        memorial.save()
        return memorial

    @staticmethod
    def get_by_id(memorial_id) -> [Memorial]:
        return Memorial.objects(id=memorial_id)[0]

    @staticmethod
    def get_by_user_id(user_id):
        roles = Role.objects(user=user_id)

        memorial_ids = [role.memorial for role in roles]
        memorials = Memorial.objects(id__in=memorial_ids)

        return memorials, roles


class RoleTypes(Enum):
    CREATOR = auto()
    MANAGER = auto()
    MEMBER = auto()


# Class to organize roles
class RoleRepo:

    @staticmethod
    def get_by_user_id(id) -> Role:
        return Role.objects(user=id)[0]

    @staticmethod
    def save(role, user, memorial) -> Role:
        role = Role(role=role, user=user, memorial=memorial)
        role.save()
        return role
