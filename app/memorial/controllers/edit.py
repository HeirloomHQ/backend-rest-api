from app.memorial.repos import MemorialRepo, RoleRepo, RoleTypes
from app.services.permission import Action, can_user_execute


def edit_memorial(user_id, memorial_id, first_name, last_name, description, born, died, bio, home_town, cover_photo,
                  page_theme, can_post, can_view, can_manage, can_delete):
    # 1. Check valid user
    # 2. Display all user memorials based on user_id
    # 3. Actual memorial_id
    # 4. Change memorial based on user_id and memorial_id
    # 5. Change the content based on memorial

    if not user_id:
        return {"msg": "Missing user"}, 400

    memorial = MemorialRepo.get_by_id(memorial_id)

    if not can_user_execute(Action.MANAGE, RoleRepo.get_by_user_memorial_id(user_id, memorial_id), memorial):
        return {"msg": "Invalid permission"}, 403

    new_memorial = {"description": description,
                "first_name": first_name,
                "last_name": last_name,
                "born": born, "died": died,
                "bio": bio, "home_town": home_town,
                "cover_photo": cover_photo,
                "page_theme": page_theme,
                "can_post": can_post,
                "can_view": can_view,
                "can_manage": can_manage,
                "can_delete": can_delete
                }

    # update the original memorial only if there are inputs
    for field, value in new_memorial.items():
        if value is not None:
            memorial[field] = value

    memorial.save()

    return memorial.to_json(), 200

def edit_role(requester_id, memorial_id, role_id, new_role):
    if not role_id:
        return {"msg": "Missing roleId"}, 400

    if new_role is None:
        return {"msg": "Missing new role"}, 400

    try:
        new_role_type = RoleTypes[new_role]
    except:
        return {"msg": "New role not recognized"}, 400

    memorial = MemorialRepo.get_by_id(memorial_id)
    if memorial is None:
        return {"msg": "Memorial not found"}, 404

    requester_role = RoleRepo.get_by_user_memorial_id(requester_id, memorial_id)
    if requester_role is None:
        return {"msg": "Role not found"}, 404

    if not can_user_execute(Action.MANAGE, requester_role, memorial):
        return {"msg": "Not allowed to perform action"}, 403

    role_to_change = RoleRepo.get_by_user_memorial_id(role_id, memorial_id)
    if role_to_change is None:
        return {"msg": "Role not found"}, 404

    if role_to_change.role == RoleTypes.OWNER.name:
        return {"msg": "Can't change owner's role"}, 403

    role_to_change.role = new_role_type.name

    role_to_change.save()

    return "Succeeded in editing role", 200