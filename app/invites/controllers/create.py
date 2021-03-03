from app.auth.utils import is_email
from app.profile.repos import UserRepo
from app.constants import CLIENT, INVITE_DAYS_TTL
from app.memorial.repos import MemorialRepo, RoleRepo
from app.invites.repos import InviteRepo
from app.services import email as email_service, permission
from uuid import uuid4
from datetime import  datetime, timedelta


def invite(inviter_id, memorial_id, emails: [str]):
    # arg validation
    if memorial_id is None:
        return "Missing memorial", 400

    for email in emails:
        if not is_email(email):
            return "{} is not a proper email".format(email), 400

    # check permissions
    role = RoleRepo.get_by_user_id(inviter_id)
    memorial = MemorialRepo.get_by_id(memorial_id)

    allowed = permission.can_user_execute(permission.Action.MANAGE, role, memorial)
    if not allowed:
        return "User cannot send invites", 403

    # create invites
    inviter = UserRepo.get_user_by_id(inviter_id)
    invites = []

    expiration_date = str(datetime.utcnow() + timedelta(days=INVITE_DAYS_TTL))
    for email in emails:
        invite = {
            "inviter_id": inviter_id,
            "invitee_email": email,
            "token":str(uuid4()),
            "memorial": memorial_id,
            "expiration_date": expiration_date
        }
        invites.append(invite)

    # save invites
    invite_documents = InviteRepo.create_many(invites)

    # send emails
    for invite in invite_documents:
        email_service.send_invitation_email(
            invite.invitee_email,
            inviter.first_name,
            CLIENT + "/api/invites/{}/activation?token={}".format(str(invite.id), invite.token)
        )

    return "Invites sent", 202
