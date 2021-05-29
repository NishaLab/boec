from enum import unique, Enum

@unique
class UserRole(Enum):
    CUSTOMER = 1
    ADMIN = 2