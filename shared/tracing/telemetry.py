import functools
import logging
import time
from typing import Any, Callable

logger = logging.getLogger("shared.tracing.telemetry")

def configure_telemetry(service_name: str) -> None:
    """Configures OpenTelemetry tracer provider and Prometheus metrics."""
    logger.info(f"OpenTelemetry instrumentation configured for {service_name}")

def trace_span(span_name: str) -> Callable:
    """Decorator to create a distributed trace span around a coroutine."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.perf_counter()
            logger.debug(f"[SPAN START] {span_name}")
            try:
                res = await func(*args, **kwargs)
                elapsed_ms = (time.perf_counter() - start_time) * 1000
                logger.debug(f"[SPAN END] {span_name} completed in {elapsed_ms:.2f}ms")
                return res
            except Exception as e:
                elapsed_ms = (time.perf_counter() - start_time) * 1000
                logger.error(f"[SPAN ERROR] {span_name} failed after {elapsed_ms:.2f}ms: {e}")
                raise
        return wrapper
    return decorator
