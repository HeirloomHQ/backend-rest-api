from app.infra.models.memorial import Memorial
from app.infra.models.role import Role


# Class to organize operations related to a user
class MemorialRepo:

    @staticmethod
    def save(memorial_id, first_name, last_name, description) -> Memorial:
        memorial = Memorial(memorial_id=memorial_id, first_name=first_name,
                            last_name=last_name, description=description)
        memorial.save()
        return memorial

    @staticmethod
    def get_by_id(memorial_id) -> [Memorial]:
        return Memorial.objects(memorial_id=memorial_id)[0]

    @staticmethod
    def get_by_user_id(user_id):
        roles = Role.objects(user_id=user_id)

        memorial_ids = [role.memorial_id for role in roles]
        memorials = Memorial.objects(memorial_id__in=memorial_ids)

        return memorials, roles

    @staticmethod
    def get_by_user_memorial_ids(user_id, memorial_id):
        role = Role.objects(user_id=user_id, memorial_id=memorial_id)[0]

        memorial_id = role.memorial_id
        memorial = Memorial.objects(memorial_id=memorial_id)

        return memorial, role

from app.infra.models.memorial import Memorial
from mongoengine.queryset.visitor import Q


# Class to organize roles
class RoleRepo:

    @staticmethod
    def get_by_user_id(id) -> Role:
        return Role.objects(user_id=id)[0]

    @staticmethod
    def save(role_id, role, user_id) -> Role:
        role = Role(role_id, role, user_id)
        role.save()
        return role
