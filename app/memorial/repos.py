from app.infra.models.memorial import Memorial


# Class to organize operations related to a user
class MemorialRepo:

    @staticmethod
    def get_memorial_by_id(id) -> Memorial:
        memorial = Memorial.objects(id=id)[0]
        return memorial

    @staticmethod
    def get_memorial_by_email(creator_email) -> Memorial:
        memorials = Memorial.objects(creator_email=creator_email)
        return memorials[0] if len(memorials) else None
    # Todo: Need a way to retrieve multiple memorials

    @staticmethod
    def save(memorial_id, creator_email, first_name, last_name, description) -> Memorial:
        memorial = Memorial(memorial_id=memorial_id, creator_email=creator_email, first_name=first_name,
                            last_name=last_name, description=description )
        memorial.save()
        return memorial

