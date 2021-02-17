from enum import Enum
from app.infra.models.memorial import Memorial
from app.infra.models.role import Role
from app.memorial.repos import RoleTypes


class Action(Enum):
    VIEW = "canView"
    MANAGE = "canManage"
    POST = "canPost"
    EDIT_PRIVACY = "canEditPrivacy"
    DELETE = "canDelete"


def can_user_execute(action: Action, role: Role, memorial: Memorial):
    if type(action) != Action:
        raise ValueError("action must be of enum type Action")
    if type(role) != Role and role != None:
        raise ValueError("role must be of type Role")
    if type(memorial) != Memorial:
        raise ValueError("memorial must be of type Memorial")

    privacy_settings = memorial.privacy_settings.to_json()

    anyone_can_execute = privacy_settings[action.value] == ""

    # if anyone can execute, then no need to proceed
    if anyone_can_execute:
        return True

    # must have a role at this point
    if role is None:
        return False

    # this code checks to see if the role the user has is within the required permission for the action
    role_enum = RoleTypes[role.role]
    max_role = RoleTypes[privacy_settings[action.value]]

    return role_enum.value <= max_role.value
