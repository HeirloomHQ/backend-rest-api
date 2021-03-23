from app.memoir.utils import create_memoir, get_memoir, same_user
from app.memorial.repos import RoleTypes, RoleRepo


def add_memoir(memorial_id, user_id, text, time):
    if not text or not time:
        return {"msg": "Missing text/time parameter"}, 400

    new_memoir = {
        "memorial": memorial_id,
        "creator": user_id,
        "text": text,
        "creation_date": time,
        "last_updated": time
    }

    created_memoir = create_memoir(**new_memoir)

    return created_memoir.to_json(), 201


def edit_memoir(memorial_id, memoir_id, text, time):
    memoir = get_memoir(memorial_id, memoir_id)
    if memoir is None:
        return {"msg": "Memoir doesn't exist in memorial"}

    memoir.text = text
    memoir.last_updated = time

    memoir.save()

    return memoir.to_json(), 201


def remove_memoir(memorial_id, memoir_id, user_id):
    # Check if the user deleting the memoir is owner/manager
    check_admin_role = RoleRepo.get_by_id(user_id)
    # Check if the user deleting the memoir is author
    check_author = same_user(memoir_id, user_id)

    if check_author is None or check_admin_role.role is RoleTypes.MEMBER:
        return {"msg": "User doesn't have permission to delete this memoir"}

    memoir = get_memoir(memorial_id, memoir_id)
    if memoir is None:
        return {"msg": "Memoir doesn't exist in memorial"}, 400

