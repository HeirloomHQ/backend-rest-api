from app.invites.repos import InviteRepo
from app.profile.repos import UserRepo
from app.memorial.repos import RoleRepo, RoleTypes
from app.constants import CLIENT
from app.invites import utils
from urllib import parse


def get_activation(invite_id, token):
    if token is None:
        return CLIENT + "/fourofour", 404

    invite = InviteRepo.get_by_id(invite_id)

    if invite is None:
        return CLIENT + "/fourofour", 404

    if not utils.is_valid_invite(invite):
        return CLIENT + "/fourofour", 404

    if token != invite.token:
        return CLIENT + "/fourofour", 404

    # send user to the memorial they are invited to if they do exist
    user = UserRepo.get_user_by_email(invite.invitee_email)
    if user:
        invite.accepted = True
        invite.user = user.id
        invite.save()
        RoleRepo.create(role=RoleTypes.MEMBER.name, user=user.id, memorial=invite.memorial)
        return CLIENT + "/memorial/{}".format(str(invite.memorial)), 302

    # if the user doesn't exist send them to the signup page
    # and we will accept the invite at signup
    return CLIENT + "?signup=" + parse.quote(invite.invitee_email) + "&acceptInvite=true", 302
