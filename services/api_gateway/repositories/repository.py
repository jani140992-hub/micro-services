"""Async Repository Implementation for API Gateway Service."""

from typing import Dict, List, Optional, Tuple
from domain.models import GatewayRouteAggregate, RoutePredicate, RouteFilter
from domain.exceptions import GatewayRouteNotFoundException

class GatewayRouteRepository:
    """Async data access repository supporting filtering, pagination, and transactional saves."""

    def __init__(self) -> None:
        self._storage: Dict[str, GatewayRouteAggregate] = {}
        self._code_index: Dict[str, str] = {}

    async def get_by_id(self, entity_id: str) -> Optional[GatewayRouteAggregate]:
        entity = self._storage.get(entity_id)
        if entity and not entity.is_deleted:
            return entity
        return None

    async def get_by_code(self, code: str) -> Optional[GatewayRouteAggregate]:
        eid = self._code_index.get(code.upper())
        if eid:
            return await self.get_by_id(eid)
        return None

    async def save(self, entity: GatewayRouteAggregate) -> GatewayRouteAggregate:
        self._storage[entity.id] = entity
        self._code_index[entity.code.upper()] = entity.id
        return entity

    async def delete(self, entity_id: str, actor_id: str) -> bool:
        entity = await self.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)
        entity.soft_delete(actor_id)
        return True

    async def query(
        self,
        search: Optional[str] = None,
        status: Optional[str] = None,
        category: Optional[str] = None,
        tenant_id: Optional[str] = None,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[List[GatewayRouteAggregate], int]:
        matches = [e for e in self._storage.values() if not e.is_deleted]

        if tenant_id:
            matches = [e for e in matches if e.tenant_id == tenant_id]
        if status:
            matches = [e for e in matches if e.status == status.upper()]
        if category:
            matches = [e for e in matches if e.category.upper() == category.upper()]
        if search:
            s = search.lower()
            matches = [e for e in matches if s in e.name.lower() or s in e.code.lower() or (e.description and s in e.description.lower())]

        total = len(matches)
        paged = matches[skip : skip + limit]
        return paged, total

    async def count_by_status(self) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for e in self._storage.values():
            if not e.is_deleted:
                counts[e.status] = counts.get(e.status, 0) + 1
        return counts
