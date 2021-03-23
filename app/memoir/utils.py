from app.infra.models.memoir import Memoir


# Create a new memoir in memorial
def create_memoir(memorial, creator, text, creation_date, last_updated) -> Memoir:
    memoir = Memoir(memorial=memorial, creator=creator, text=text, creation_date=creation_date, last_updated=last_updated)
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
    return memoir_list[0] if len(memoir_list) > 0 else None
