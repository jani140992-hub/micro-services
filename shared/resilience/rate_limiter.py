import time
import asyncio
from typing import Dict

class TokenBucketRateLimiter:
    """In-memory token bucket rate limiter."""

    def __init__(self, capacity: int, refill_rate: float) -> None:
        self.capacity = capacity
        self.refill_rate = refill_rate
        self._tokens: Dict[str, float] = {}
        self._last_refill: Dict[str, float] = {}
        self._lock = asyncio.Lock()

    async def acquire(self, key: str, tokens: int = 1) -> bool:
        async with self._lock:
            now = time.time()
            if key not in self._tokens:
                self._tokens[key] = float(self.capacity)
                self._last_refill[key] = now

            elapsed = now - self._last_refill[key]
            self._tokens[key] = min(float(self.capacity), self._tokens[key] + elapsed * self.refill_rate)
            self._last_refill[key] = now

            if self._tokens[key] >= tokens:
                self._tokens[key] -= tokens
                return True
            return False

class LeakyBucketRateLimiter:
    """Leaky bucket rate limiter enforcing constant egress rate."""

    def __init__(self, capacity: int, leak_rate: float) -> None:
        self.capacity = capacity
        self.leak_rate = leak_rate
        self._water: Dict[str, float] = {}
        self._last_leak: Dict[str, float] = {}
        self._lock = asyncio.Lock()

    async def check_allowed(self, client_id: str) -> bool:
        async with self._lock:
            now = time.time()
            if client_id not in self._water:
                self._water[client_id] = 0.0
                self._last_leak[client_id] = now

            elapsed = now - self._last_leak[client_id]
            leaked = elapsed * self.leak_rate
            self._water[client_id] = max(0.0, self._water[client_id] - leaked)
            self._last_leak[client_id] = now

            if self._water[client_id] + 1.0 <= self.capacity:
                self._water[client_id] += 1.0
                return True
            return False
