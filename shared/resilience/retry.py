import asyncio
import functools
import logging
import random
from typing import Any, Callable, Sequence, Type

logger = logging.getLogger("shared.resilience.retry")

class ExponentialBackoff:
    def __init__(self, base_delay: float = 0.5, max_delay: float = 10.0, multiplier: float = 2.0) -> None:
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.multiplier = multiplier

    def compute(self, attempt: int) -> float:
        delay = self.base_delay * (self.multiplier ** attempt)
        return min(delay, self.max_delay)

class FullJitter:
    @staticmethod
    def apply(delay: float) -> float:
        return random.uniform(0, delay)

def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 0.5,
    max_delay: float = 5.0,
    retry_exceptions: Sequence[Type[Exception]] = (Exception,)
) -> Callable:
    """Decorator that retries async operations with exponential backoff and jitter."""
    backoff = ExponentialBackoff(base_delay, max_delay)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error: Exception = Exception("Unknown")
            for attempt in range(max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except retry_exceptions as err:
                    last_error = err
                    if attempt == max_retries:
                        logger.error(f"Retry limit reached ({max_retries}) for {func.__name__}")
                        raise err
                    raw_delay = backoff.compute(attempt)
                    jittered_delay = FullJitter.apply(raw_delay)
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {err}. Retrying in {jittered_delay:.2f}s")
                    await asyncio.sleep(jittered_delay)
            raise last_error
        return wrapper
    return decorator
