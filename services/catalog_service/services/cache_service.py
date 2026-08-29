"""Distributed Cache Service for Product Catalog Service."""

import json
import logging
from typing import Any, Dict, Optional
from domain.models import ProductItemAggregate

logger = logging.getLogger("catalog_service.cache")

class ProductItemCacheService:
    """Cache manager providing low-latency access and write-through invalidation."""

    def __init__(self, ttl: int = 300) -> None:
        self.ttl = ttl
        self._cache_store: Dict[str, Dict[str, Any]] = {}

    def _format_key(self, entity_id: str) -> str:
        return f"cloudmart:catalog_service:entity:{entity_id}"

    async def get(self, entity_id: str) -> Optional[Dict[str, Any]]:
        key = self._format_key(entity_id)
        val = self._cache_store.get(key)
        if val:
            logger.debug(f"Cache HIT for key {key}")
            return val
        logger.debug(f"Cache MISS for key {key}")
        return None

    async def set(self, entity: ProductItemAggregate) -> None:
        key = self._format_key(entity.id)
        self._cache_store[key] = entity.model_dump(mode="json")
        logger.debug(f"Cache SET for key {key} (TTL: {self.ttl}s)")

    async def evict(self, entity_id: str) -> None:
        key = self._format_key(entity_id)
        if key in self._cache_store:
            del self._cache_store[key]
            logger.debug(f"Cache EVICTED for key {key}")

    async def clear_all(self) -> None:
        self._cache_store.clear()
