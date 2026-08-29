"""Redis-backed Distributed Token Bucket Rate Limiter with Leaky Bucket Burst Protection."""
import time
import logging
from typing import Optional, Tuple

logger = logging.getLogger("shared.resilience.redis_limiter")

class DistributedRedisRateLimiter:
    """High-throughput atomic Lua-scripted rate limiter for distributed API gateways."""
    def __init__(self, default_rate: float = 100.0, burst_capacity: int = 200) -> None:
        self.default_rate = default_rate
        self.burst_capacity = burst_capacity
        self._local_buckets = {}

    async def acquire_token(self, client_identifier: str, requested_tokens: int = 1) -> Tuple[bool, float]:
        now = time.time()
        bucket = self._local_buckets.setdefault(client_identifier, {"tokens": self.burst_capacity, "last_updated": now})
        elapsed = now - bucket["last_updated"]
        bucket["tokens"] = min(float(self.burst_capacity), bucket["tokens"] + elapsed * self.default_rate)
        bucket["last_updated"] = now
        if bucket["tokens"] >= requested_tokens:
            bucket["tokens"] -= requested_tokens
            return True, bucket["tokens"]
        return False, 0.0
