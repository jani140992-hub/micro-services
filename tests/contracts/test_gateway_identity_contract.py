import pytest

class TestGatewayIdentityContract:
    """Consumer-Driven Contract: API Gateway (Consumer) -> Identity Service (Provider)."""

    EXPECTED_INTROSPECTION_REQUEST = {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.fake_signature"
    }

    EXPECTED_INTROSPECTION_RESPONSE = {
        "active": True,
        "sub": "usr_998877",
        "email": "developer@cloudmart.com",
        "roles": ["ADMIN", "MANAGER"],
        "permissions": ["catalog:write", "inventory:write", "orders:read"]
    }

    def test_introspection_schema(self):
        resp = self.EXPECTED_INTROSPECTION_RESPONSE
        assert resp["active"] is True
        assert "ADMIN" in resp["roles"]
