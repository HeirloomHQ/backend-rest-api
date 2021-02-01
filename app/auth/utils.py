import re

EMAIL_REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def is_email(email):
    if (re.search(EMAIL_REGEX, email)):
        return True
    return False