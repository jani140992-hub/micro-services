import enum
from typing import Dict, List, Set

class Role(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    CUSTOMER = "CUSTOMER"
    SERVICE_CLIENT = "SERVICE_CLIENT"

class Permission(str, enum.Enum):
    USERS_READ = "users:read"
    USERS_WRITE = "users:write"
    CATALOG_READ = "catalog:read"
    CATALOG_WRITE = "catalog:write"
    INVENTORY_READ = "inventory:read"
    INVENTORY_WRITE = "inventory:write"
    ORDERS_READ = "orders:read"
    ORDERS_WRITE = "orders:write"
    PAYMENTS_PROCESS = "payments:process"
    SHIPPING_MANAGE = "shipping:manage"
    ANALYTICS_VIEW = "analytics:view"

class PermissionMatrix:
    _ROLE_PERMISSIONS: Dict[Role, Set[Permission]] = {
        Role.ADMIN: set(Permission),
        Role.MANAGER: {
            Permission.USERS_READ,
            Permission.CATALOG_READ,
            Permission.CATALOG_WRITE,
            Permission.INVENTORY_READ,
            Permission.INVENTORY_WRITE,
            Permission.ORDERS_READ,
            Permission.ORDERS_WRITE,
            Permission.SHIPPING_MANAGE,
            Permission.ANALYTICS_VIEW,
        },
        Role.CUSTOMER: {
            Permission.CATALOG_READ,
            Permission.ORDERS_READ,
            Permission.ORDERS_WRITE,
        },
        Role.SERVICE_CLIENT: {
            Permission.CATALOG_READ,
            Permission.INVENTORY_READ,
            Permission.INVENTORY_WRITE,
            Permission.ORDERS_READ,
            Permission.PAYMENTS_PROCESS,
            Permission.SHIPPING_MANAGE,
        }
    }

    @classmethod
    def get_permissions(cls, role: Role) -> Set[Permission]:
        return cls._ROLE_PERMISSIONS.get(role, set())

def has_permission(user_permissions: List[str], required: str) -> bool:
    return required in user_permissions
