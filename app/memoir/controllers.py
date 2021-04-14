from app.memoir.utils import create_memoir, get_memoir


def add_memoir(memorial_id, user_id, text, time, media_url):
    if not text or not time:
        return {"msg": "Missing text/time parameter"}, 400

    new_memoir = {
        "memorial": memorial_id,
        "creator": user_id,
        "text": text,
        "creation_date": time,
        "last_updated": time,
        "media_url": media_url
    }

    created_memoir = create_memoir(**new_memoir)

    return created_memoir.to_json(), 201


def edit_memoir(memorial_id, memoir_id, text, time, media_url):
    memoir = get_memoir(memorial_id, memoir_id)
    if memoir is None:
        return {"msg": "Memoir doesn't exist in memorial"}

    new_memoir = {
        "text": text,
        "last_updated": time,
        "media_url": media_url
    }

    # update the original memoir only if there are inputs
    for field, value in new_memoir.items():
        if value is not None:
            memoir[field] = value

    memoir.save()

    return memoir.to_json(), 201


def remove_memoir(memorial_id, memoir_id):
    memoir = get_memoir(memorial_id, memoir_id)
    if memoir is None:
        return {"msg": "Memoir doesn't exist in memorial"}

    memoir.delete()

    return "Successfully deleted", 201
