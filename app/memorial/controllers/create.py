from app.memorial.repos import MemorialRepo, RoleRepo, RoleTypes
from app.memorial.utils import create_owner_role


def create(creator_id, description, first_name,
           last_name, born, died,
           bio, home_town,
           cover_photo, page_theme,
           can_view, can_post):
    """
    This controller
    * creates a new memorial
    * assigns the creator a creator role
    """

    # validate input
    memorial = {"description": description,
                "first_name": first_name,
                "last_name": last_name,
                "born": born, "died": died,
                "bio": bio, "home_town": home_town,
                "cover_photo": cover_photo,
                "page_theme": page_theme,
                "can_post": can_post, "can_view": can_view,
                }
    for field, value in memorial.items():
        if value is None:
            return "Missing {} parameter".format(field), 400

    # create memorial
    memorial_to_create = {
        "first_name": first_name,
        "last_name": last_name,
        "description": description,
        "born": born, "died": died,
        "bio": bio, "home_town": home_town,
        "cover_photo": cover_photo,
        "page_theme": page_theme,
        "can_post": can_post, "can_view": can_view,
    }
    created_memorial = MemorialRepo.create(**memorial_to_create)

    # create role
    create_owner_role(creator_id, created_memorial.id)

    return created_memorial.to_json(), 201
