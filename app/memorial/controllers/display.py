from app.memorial.repos import MemorialRepo, RoleRepo
from app.services.permission import Action, can_user_execute


def display_all_user_memorials(user_id):
    if not user_id:
        return {"msg": "Missing email parameter"}, 400

    memorial_docs, role_docs = MemorialRepo.get_by_user_id(user_id)

    if len(memorial_docs) == 0:
        return "No memorials found for the authenticated user", 404

    # build a dict of memorial ids to role for the user
    role_map = {}
    for role in role_docs:
        m_id = str(role.memorial)
        role_map[m_id] = role

    # this is to make sure that a user still has view permission
    # just bc user has a role doesn't mean they can view
    memorials_response = []
    role_response = {}
    for memorial in memorial_docs:
        m_id = str(memorial.id)
        role = role_map[m_id]
        can_view = can_user_execute(Action.VIEW, role, memorial)

        if can_view:
            memorials_response.append(memorial.to_json())
            role_response[m_id] = role.role

    return (memorials_response, role_response), 200


def display_single_memorial_for_user(user_id, memorial_id):
    if not memorial_id:
        return {"msg": "Missing memorialID parameter"}, 400

    memorial_doc = MemorialRepo.get_by_id(memorial_id)
    role_doc = RoleRepo.get_by_user_id(user_id) if user_id != None else None

    if memorial_doc == None:
        return "Memorial not found", 404

    allowed = can_user_execute(Action.VIEW, role_doc, memorial_doc)
    if not allowed:
        return "User does not have access to view the heirloom", 403

    return (memorial_doc.to_json(), role_doc.to_json() if role_doc != None else None), 200

def display_members_for_single_memorial(memorial_id):
    # 1. Check to see that the memorial exists
    # 2. Get the memorial by its id
    # 3. Print the information provided
    if not memorial_id:
        return {"msg": "Missing memorialID parameter"}, 400

    memorial_doc = MemorialRepo.get_by_id(memorial_id)

    if memorial_doc == None:
        return "Memorial not found", 404

    #Permission will come later
    return (memorial_doc.to_json()), 200




