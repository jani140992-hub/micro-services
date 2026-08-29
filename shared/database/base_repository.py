from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, TypeVar

T = TypeVar("T")

class IRepository(Generic[T], ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str) -> Optional[T]:
        pass

    @abstractmethod
    async def list_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        pass

    @abstractmethod
    async def add(self, entity: T) -> T:
        pass

    @abstractmethod
    async def update(self, entity: T) -> T:
        pass

    @abstractmethod
    async def delete(self, entity_id: str) -> bool:
        pass

class GenericAsyncRepository(IRepository[T]):
    """In-memory generic repository implementation suitable for testing and base patterns."""

    def __init__(self) -> None:
        self._items: Dict[str, T] = {}

    async def get_by_id(self, entity_id: str) -> Optional[T]:
        return self._items.get(entity_id)

    async def list_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        return list(self._items.values())[skip : skip + limit]

    async def add(self, entity: T) -> T:
        entity_id = getattr(entity, "id", None)
        if entity_id:
            self._items[str(entity_id)] = entity
        return entity

    async def update(self, entity: T) -> T:
        entity_id = getattr(entity, "id", None)
        if entity_id and str(entity_id) in self._items:
            self._items[str(entity_id)] = entity
        return entity

    async def delete(self, entity_id: str) -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False
