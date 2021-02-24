from datetime import datetime
from app.infra.models.invite import Invite


def is_valid_invite(invite: Invite) -> bool:
    # check if invite is still valid
    expiration_date = datetime.fromisoformat(invite.expiration_date)
    now = datetime.utcnow()
    return not (invite.accepted or now > expiration_date)