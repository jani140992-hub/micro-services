"""Chaos Engineering & Fault Injection Middleware for Resiliency Testing."""
import random
import asyncio
import logging
from typing import Optional

logger = logging.getLogger("shared.resilience.chaos")

class ChaosMonkeyFaultInjector:
    """Injects artificial network latency and exceptions for chaos testing."""
    def __init__(self, failure_rate: float = 0.0, max_latency_ms: int = 0) -> None:
        self.failure_rate = failure_rate
        self.max_latency_ms = max_latency_ms

    async def maybe_inject_fault(self, operation_name: str) -> None:
        if self.max_latency_ms > 0:
            delay = random.uniform(0, self.max_latency_ms / 1000.0)
            logger.warning(f"Chaos Monkey injecting {delay:.3f}s latency into {operation_name}")
            await asyncio.sleep(delay)

        if self.failure_rate > 0 and random.random() < self.failure_rate:
            logger.error(f"Chaos Monkey injecting simulated failure into {operation_name}")
            raise RuntimeError(f"Chaos fault injected into {operation_name}")
