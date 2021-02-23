from app.infra.models.invite import Invite


class InviteRepo():

    @staticmethod
    def create_many(invites):
        invite_models = [Invite(**invite) for invite in invites]
        Invite.objects.insert(invite_models)
        return invite_models