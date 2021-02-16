from app.memorial.repos import MemorialRepo, RoleRepo


def display_all_user_memorials(user_id):
    if not user_id:
        return {"msg": "Missing email parameter"}, 400

    memorial_docs, role_docs = MemorialRepo.get_by_user_id(user_id)

    if len(memorial_docs) == 0:
        return "No memorials for user", 404

    memorials = [memorial_doc.to_json() for memorial_doc in memorial_docs]
    roles = [role_doc.to_json() for role_doc in role_docs]

    # build a dict of memorial ids to role for the user
    role_response = {}
    for role in roles:
        role_response[role["memorial"]] = role["role"]

    return (memorials, role_response), 200

def display_single_memorial_for_user(user_id, memorial_id):
    if not user_id:
        return {"msg": "Missing userID parameter"}, 400
    if not memorial_id:
        return {"msg": "Missing memorialID parameter"}, 400


    memorial_doc = MemorialRepo.get_by_id(memorial_id)
    role_doc = RoleRepo.get_by_user_id(user_id)

    if memorial_doc == None:
        return "No memorials for user", 404

    return (memorial_doc.to_json(), role_doc.to_json()), 200