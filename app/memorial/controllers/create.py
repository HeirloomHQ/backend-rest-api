from app.memorial.repos import MemorialRepo, RoleRepo, RoleTypes
from app.auth.utils import is_email
from app.auth.repos import UserRepo
from app.services import email as email_service, permission


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
        "role": RoleTypes.OWNER.name,
        "user": creator_id,
        "memorial": str(created_memorial.id)
    }
    print(role)
    RoleRepo.create(**role)

    return created_memorial.to_json(), 201


def create_invite(inviter_id, memorial_id, emails):
    # arg validation
    for email in emails:
        if not is_email(email):
            return "{} is not a proper email".format(email), 400

    role = RoleRepo.get_by_user_id(inviter_id)
    memorial = MemorialRepo.get_by_id(memorial_id)

    allowed = permission.can_user_execute(permission.Action.MANAGE, role, memorial)

    if not allowed:
        return "User cannot send invites", 403

    # create invites here

    user = UserRepo.get_user_by_id(inviter_id)
    email_service.send_invitation_email(emails, user.first_name, "link")

    return "Invites sent", 202