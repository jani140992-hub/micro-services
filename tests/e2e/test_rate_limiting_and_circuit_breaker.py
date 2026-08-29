import pytest
import asyncio
from shared.resilience.circuit_breaker import CircuitBreaker, CircuitBreakerOpenException
from shared.resilience.rate_limiter import TokenBucketRateLimiter, LeakyBucketRateLimiter

@pytest.mark.asyncio
async def test_token_bucket_rate_limiter():
    limiter = TokenBucketRateLimiter(capacity=5, refill_rate=2.0)
    for _ in range(5):
        assert await limiter.acquire("client_ip_1") is True
    assert await limiter.acquire("client_ip_1") is False

@pytest.mark.asyncio
async def test_circuit_breaker_tripping_and_recovery():
    cb = CircuitBreaker(name="PaymentGatewayCircuit", failure_threshold=3, recovery_timeout=0.2)
    fail_counter = 0

    async def flaky_service_call():
        nonlocal fail_counter
        fail_counter += 1
        if fail_counter <= 3:
            raise ConnectionError("Upstream timeout")
        return "SUCCESS"

    for _ in range(3):
        with pytest.raises(ConnectionError):
            await cb.call(flaky_service_call)

    with pytest.raises(CircuitBreakerOpenException):
        await cb.call(flaky_service_call)

    await asyncio.sleep(0.3)
    result = await cb.call(flaky_service_call)
    assert result == "SUCCESS"
