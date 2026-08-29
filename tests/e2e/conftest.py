import pytest
import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from shared.security.jwt import JWTManager

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def jwt_manager():
    return JWTManager(secret_key="cloudmart_test_secret_key_12345")

@pytest.fixture
def auth_headers(jwt_manager):
    token = jwt_manager.create_access_token(
        user_id="usr_test_123456",
        email="shopper@cloudmart.com",
        roles=["CUSTOMER"],
        permissions=["orders:read", "orders:write", "catalog:read"]
    )
    return {"Authorization": f"Bearer {token}", "X-Correlation-ID": "test-corr-id-001"}
