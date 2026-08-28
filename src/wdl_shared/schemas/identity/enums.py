from enum import StrEnum


class AccountSubject(StrEnum):
    USER = "user"
    SERVICE = "service"


class AccountStatus(StrEnum):
    PENDING = "pending"
    ACTIVE = "active"
    DEACTIVATED = "deactivated"
    SUSPENDED = "suspended"
