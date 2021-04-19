from app.memorial.repos import MemorialRepo, RoleRepo
from app.services.permission import Action, can_user_execute


def delete_memorial(memorial_id, user_id):
    memorial = MemorialRepo.get_by_id(memorial_id)
    if not can_user_execute(Action.DELETE, RoleRepo.get_by_user_memorial_id(user_id, memorial_id), memorial):
        return {"msg": "Invalid permission"}, 403

    memorial.delete()

    return {"msg": "Memorial has been deleted"}, 201
