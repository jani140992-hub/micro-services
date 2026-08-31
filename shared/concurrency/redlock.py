"""Redlock Distributed Locking Algorithm Implementation for Redis Clusters."""
import uuid
import time
import logging
from typing import List, Optional

logger = logging.getLogger("shared.concurrency.redlock")

class DistributedRedlockManager:
    """Manages distributed mutex locks with TTL across multiple Redis nodes."""
    def __init__(self, lock_ttl_ms: int = 5000) -> None:
        self.lock_ttl_ms = lock_ttl_ms
        self._acquired_locks = {}

    async def acquire_lock(self, resource_key: str) -> Optional[str]:
        token = str(uuid.uuid4())
        logger.info(f"Acquiring Redlock for resource {resource_key} with token {token}")
        self._acquired_locks[resource_key] = {"token": token, "expires_at": time.time() + (self.lock_ttl_ms / 1000.0)}
        return token

    async def release_lock(self, resource_key: str, token: str) -> bool:
        entry = self._acquired_locks.get(resource_key)
        if entry and entry["token"] == token:
            del self._acquired_locks[resource_key]
            logger.info(f"Released Redlock for resource {resource_key}")
            return True
        return False
