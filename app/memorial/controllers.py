import uuid
from app.memorial.repos import MemorialRepo
from app.auth import utils


def display(creator_email):
    if not creator_email:
        return {"msg": "Missing email parameter"}, 400

    memorial = MemorialRepo.get_memorial_by_email(creator_email)

    if memorial == None:
        return "No email associated", 401

    return memorial.to_json(), 200

# Todo: Currently not able to append memorials. Only one email can be attached to a memorial
def create(creator_email, description, first_name, last_name):
    # validate input
    memorial = {"creator_email": creator_email, "description": description,
                "first_name": first_name, "last_name": last_name}
    for field, value in memorial.items():
        if value is None:
            return "Missing {} parameter".format(field), 400

    if not utils.is_email(creator_email):
        return "Email must be an actual email", 400

    #Todo: Implement capabilites to allow or reject for multiple memorials for one email

    memorial_to_create = {
        "memorial_id": str(uuid.uuid4()),
        "creator_email": creator_email,
        "first_name": first_name,
        "last_name": last_name,
        "description": description
        }

    # create memorial
    created_memorial = MemorialRepo.save(**memorial_to_create)

    return created_memorial.to_json(), 200



