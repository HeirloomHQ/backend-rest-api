from app.infra.models.memoir import Memoir


def create_memoir(memorial, creator, text, creation_date, last_updated) -> Memoir:
    memoir = Memoir(memorial=memorial, creator=creator, text=text, creation_date=creation_date,
                    last_updatd=last_updated)
    memoir.save()
    return memoir


def get_memoir(memorial, memoir) -> [Memoir]:
    memoir_list = Memoir.objects(id=memoir, memorial=memorial)
    return memoir_list[0] if len(memoir_list) > 0 else None


def get_all_memoirs(memorial) -> [Memoir]:
    memoir_list = Memoir.objects(memorial=memorial)
    return memoir_list
