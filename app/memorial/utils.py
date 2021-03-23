from app.memorial.repos import RoleTypes, RoleRepo


def create_owner_role(user_id, memorial_id):
    # create role
    role = {
        "role": RoleTypes.OWNER.name,
        "user": user_id,
        "memorial": memorial_id
    }
    RoleRepo.create(**role)


def create_manager_role(user_id, memorial_id):
    # create role
    role = {
        "role": RoleTypes.MANAGER.name,
        "user": user_id,
        "memorial": memorial_id
    }
    RoleRepo.create(**role)


def create_member_role(user_id, memorial_id):
    # create role
    role = {
        "role": RoleTypes.MEMBER.name,
        "user": user_id,
        "memorial": memorial_id
    }
    RoleRepo.create(**role)
