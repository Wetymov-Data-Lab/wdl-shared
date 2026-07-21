from enum import StrEnum


class RealmStatus(StrEnum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DISABLED = "disabled"


class RealmVisibility(StrEnum):
    PRIVATE = "private"
    INTERNAL = "internal"
    PUBLIC = "public"
