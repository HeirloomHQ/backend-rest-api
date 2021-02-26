from app.memorial.repos import MemorialRepo, RoleRepo
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

    if not can_user_execute(Action.EDIT_PRIVACY, RoleRepo.get_by_user_id(user_id), memorial):
        return {"msg": "Invalid permission"}, 400

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
        if value:
            memorial[field] = value

    memorial.save()

    return memorial.to_json(), 200
