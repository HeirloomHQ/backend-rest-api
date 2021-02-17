from app.memorial.repos import MemorialRepo, RoleRepo, RoleTypes


def create(creator_id, description, first_name, last_name):
    """
    This controller
    * creates a new memorial
    * assigns the creator a creator role
    """

    # validate input
    memorial = {"description": description,
                "first_name": first_name, "last_name": last_name}
    for field, value in memorial.items():
        if value is None:
            return "Missing {} parameter".format(field), 400

    # create memorial
    memorial_to_create = {
        "first_name": first_name,
        "last_name": last_name,
        "description": description
    }
    created_memorial = MemorialRepo.create(**memorial_to_create)

    # create role
    role = {
        "role": RoleTypes.CREATOR.name,
        "user": creator_id,
        "memorial": str(created_memorial.id)
    }
    print(role)
    RoleRepo.create(**role)

    return created_memorial.to_json(), 201
