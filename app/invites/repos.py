from app.infra.models.invite import Invite


class InviteRepo():

    @staticmethod
    def get_by_id(invite_id) -> Invite:
        invites = Invite.objects(id=invite_id)
        return invites[0] if len(invites) else None

    @staticmethod
    def get_by_invitee_email(email) -> Invite:
        return Invite.objects(invitee_email=email)

    @staticmethod
    def create_many(invites):
        invite_models = [Invite(**invite) for invite in invites]
        Invite.objects.insert(invite_models)
        return invite_models
