import time
import asyncio
import enum
import logging
from typing import Any, Callable, Optional

logger = logging.getLogger("shared.resilience.circuit_breaker")

class CircuitState(str, enum.Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class CircuitBreakerOpenException(Exception):
    def __init__(self, name: str, retry_after: float) -> None:
        super().__init__(f"Circuit breaker '{name}' is OPEN. Retry after {retry_after:.1f}s")
        self.name = name
        self.retry_after = retry_after

class CircuitBreaker:
    """Production-ready Circuit Breaker pattern implementation."""

    def __init__(
        self,
        name: str,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        half_open_success_threshold: int = 3
    ) -> None:
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_success_threshold = half_open_success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_state_change = time.time()
        self._lock = asyncio.Lock()

    async def call(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        async with self._lock:
            now = time.time()
            if self.state == CircuitState.OPEN:
                if now - self.last_state_change > self.recovery_timeout:
                    logger.info(f"Circuit '{self.name}' transitioning from OPEN to HALF_OPEN")
                    self.state = CircuitState.HALF_OPEN
                    self.success_count = 0
                else:
                    retry_after = self.recovery_timeout - (now - self.last_state_change)
                    raise CircuitBreakerOpenException(self.name, retry_after)

        try:
            result = await func(*args, **kwargs)
            await self._on_success()
            return result
        except Exception as ex:
            await self._on_failure()
            raise ex

    async def _on_success(self) -> None:
        async with self._lock:
            if self.state == CircuitState.HALF_OPEN:
                self.success_count += 1
                if self.success_count >= self.half_open_success_threshold:
                    logger.info(f"Circuit '{self.name}' recovered: transitioning to CLOSED")
                    self.state = CircuitState.CLOSED
                    self.failure_count = 0
                    self.success_count = 0
            elif self.state == CircuitState.CLOSED:
                self.failure_count = 0

    async def _on_failure(self) -> None:
        async with self._lock:
            self.failure_count += 1
            if self.state in (CircuitState.CLOSED, CircuitState.HALF_OPEN):
                if self.failure_count >= self.failure_threshold or self.state == CircuitState.HALF_OPEN:
                    logger.warning(f"Circuit '{self.name}' threshold exceeded: transitioning to OPEN")
                    self.state = CircuitState.OPEN
                    self.last_state_change = time.time()
