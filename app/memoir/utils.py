from app.infra.models.memoir import Memoir
from app.memorial.repos import RoleRepo


# Create a new memoir in memorial
def create_memoir(memorial, creator, text, creation_date, last_updated, media_url) -> Memoir:
    memoir = Memoir(memorial=memorial, creator=creator, text=text, creation_date=creation_date, last_updated=last_updated, media_url=media_url)
    memoir.save()
    return memoir


# Get a specific memoir from a memorial
def get_memoir(memorial, memoir) -> [Memoir]:
    memoir_list = Memoir.objects(id=memoir, memorial=memorial)
    return memoir_list[0] if len(memoir_list) > 0 else None


# Retrieve all memoirs in a single memorial
def get_all_memoirs(memorial) -> [Memoir]:
    memoir_list = Memoir.objects(memorial=memorial)
    return [memoir.to_json() for memoir in memoir_list]


# Checks if the current user is same as the one who created the memoir
def same_user(memoir, user) -> bool:
    memoir_list = Memoir.objects(id=memoir, creator=user)
    if len(memoir_list) > 0:
        return str(user) == str(memoir_list[0].creator)

    return False


# Checks if person deleting is owner or manager
def is_admin(memorial, user) -> bool:
    user_role = RoleRepo.get_by_user_memorial_id(user, memorial)
    if user_role is None:
        return False

    user_role = str(user_role.role)

    return user_role == "OWNER" or user_role == "MANAGER"

