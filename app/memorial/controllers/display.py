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

def display_members_for_single_memorial(memorial_id):
        if not memorial_id:
            return {"msg": "Missing memorialID parameter"}, 400

        memorial_doc = MemorialRepo.get_by_id(memorial_id)
        print("Mem doc:", "/n")
        role_docs = RoleRepo.get_by_memorial_id(memorial_id) if memorial_id != None else None
        print("role doc:","/n")
        if role_docs == None:
            return "No role information found", 404

        user_ids = []
        for role_doc in role_docs:
            # print("Roles Doc\n", role_doc.user)
            # print("Roles mem\n", role_doc.memorial)
            # print("Roles id\n", role_doc.id)
            user_ids.append(str(role_doc.user))
        # print("Users\n", user_ids)
        user_doc = UserRepo.get_users_by_ids(user_ids)
        # print("user doc:","/n")

        if user_doc == None:
            return "No user information found", 404

        if memorial_doc == None:
            return "Memorial not found", 404

        role_response = []
        for roles in role_docs:
            role_response.append(roles.to_json())

        user_response = []
        for user in user_doc:
            user_response.append(user.to_json())
            # memorials_response.append(memorial.to_json())
        # Permission will come later
        # return (memorial_doc.to_json(), role_response if role_response != None else None, user_response), 200

        # build a dict of memorial ids to role for the user
        role_map = {}
        for role in role_docs:
            m_id = str(role.memorial)
            role_map[m_id] = role

        # this is to make sure that a user still has view permission
        # just bc user has a role doesn't mean they can view
        # memorials_response = []
        # role_response = {}
        # for memorial in memorial_docs:
        #     m_id = str(memorial.id)
        #     role = role_map[m_id]
        #     can_view = can_user_execute(Action.VIEW, role, memorial)
        #
        #     if can_view:
        #         memorials_response.append(memorial.to_json())
        #         role_response[m_id] = role.role

        # This is for members
        # {
        #       email: "test@test.com",
        #       firstName: "Jim",
        #       id: "60353086ebd856702a803f50",
        #       profilePicture: "https://randomuser.me/api/portraits/women/81.jpg",
        #       lastName: "Gobright",
        #       role: "MANAGER",
        # #     },
        member_response = []
        members = {}
        for role_type in role_docs:
            user_role = str(role_type.role)

        for mem in user_doc:
            members["email"] = mem.email
            members["firstName"] = mem.first_name
            members["id"] = str(mem.id)
            members["lastName"] = mem.last_name
            members["role"] = user_role
        print(members)
        return (members), 200

# def display_members_for_single_memorial(memorial_id):
#     # 1. Check to see that the memorial exists
#     # 2. Get the memorial by its id
#     # 3. Print the information provided
#
#     # allowed = can_user_execute(Action.VIEW, role_doc, memorial_doc)
#     # if not allowed:
#     #     return "User does not have access to view the heirloom", 403
#
#     if not memorial_id:
#         return {"msg": "Missing memorialID parameter"}, 400
#
#     memorial_doc = MemorialRepo.get_by_id(memorial_id)
#     print("Mem doc:", "/n")
#     role_docs = RoleRepo.get_by_memorial_id(memorial_id) if memorial_id != None else None
#     print("role doc:", "/n")
#     if role_docs == None:
#         return "No role information found", 404
#
#     # Rolerepo get_by_memorial_id(memorial_is) -> role_docs
#
#     # First option
#     # Loop through all and call uerRepo get_by_id(using role_docs)
#     # Second Option
#     # New user method called get_by_ids(list of user ids which will be coming from the role docs -> role_doc.user)
#     # Inside of the for loop
#     #     user_ids.append(role_doc.user)
#     # Construct a list role_doc.users
#     # UserRepo.get_users_by_ids(user_ids)
#
#     user_ids = []
#     for role_doc in role_docs:
#         print("Roles Doc\n", role_doc.user)
#         print("Roles mem\n", role_doc.memorial)
#         print("Roles id\n", role_doc.id)
#         user_ids.append(str(role_doc.user))
#     print("Users\n", user_ids)
#     user_doc = UserRepo.get_users_by_ids(user_ids)
#     # user_doc = UserRepo.get_users_by_ids(role_docs[0].user)
#     print("user doc:", "/n")
#
#     if user_doc == None:
#         return "No user information found", 404
#     # return user.to_json(), 200
#
#     # When getting user back, make sure to get the right role from the user
#     # call .to_json and add in role
#     if memorial_doc == None:
#         return "Memorial not found", 404
#
#     # Permission will come later
#     # return (user_doc.to_json()), 200
#     return (memorial_doc.to_json(), role_doc.to_json() if role_doc != None else None, user_doc.to_json()), 200
#
