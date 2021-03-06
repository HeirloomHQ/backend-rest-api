from app.memorial.repos import MemorialRepo, RoleRepo
from app.services.permission import Action, can_user_execute
from app.profile.repos import UserRepo


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


def display_members_for_single_memorial(user_id, memorial_id):
    # Validate that the memorial Id exists
    if not memorial_id:
        return {"msg": "Missing memorialID parameter"}, 400

    # Retrieves user_id role type for permissions method
    role_id = RoleRepo.get_by_user_id(user_id) if user_id is not None else None

    # Retrieves memorial used to fetch members
    memorial_doc = MemorialRepo.get_by_id(memorial_id)

    # Retrieves all roles that correspond to given memorial
    role_docs = RoleRepo.get_by_memorial_id(memorial_id) if memorial_id is not None else None

    # Validates that a role exist
    if role_docs is None:
        return "No role information found", 404

    # Stores user_id for all roles connected to given memorial
    user_ids = []
    for role_doc in role_docs:
        user_ids.append(str(role_doc.user))

    # Retrieves all user documentation from user_ids provided
    user_doc = UserRepo.get_users_by_ids(user_ids)

    if user_doc is None:
        return "No user information found", 404

    if memorial_doc is None:
        return "Memorial not found", 404

    members = []
    user_roles = {}

    # Stores user role types for json display
    for role_type in role_docs:
        user_roles[str(role_type.user)] = role_type.role

    # Creates a JSON response displayed when api route is called
    for mem in user_doc:
        member = mem.to_json()
        member["role"] = user_roles[str(mem.id)]
        members.append(member)

    # Checks user permission for validation that action can be exceuted
    allowed = can_user_execute(Action.VIEW, role_id, memorial_doc)
    if not allowed:
        return "User does not have access to view the heirloom", 403

    return members, 200
