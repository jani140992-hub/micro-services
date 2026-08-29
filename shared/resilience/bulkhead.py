import asyncio
from typing import Any, Callable

class Bulkhead:
    """Bulkhead isolation limiting maximum concurrent executions."""

    def __init__(self, name: str, max_concurrent: int, max_queue: int = 10) -> None:
        self.name = name
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.max_queue = max_queue
        self._waiting = 0

    async def execute(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        if self._waiting >= self.max_queue:
            raise RuntimeError(f"Bulkhead '{self.name}' queue capacity exceeded")

        self._waiting += 1
        try:
            async with self.semaphore:
                self._waiting -= 1
                return await func(*args, **kwargs)
        except Exception:
            self._waiting = max(0, self._waiting - 1)
            raise
