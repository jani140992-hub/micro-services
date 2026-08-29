import pytest
import time
from shared.security.jwt import JWTManager, TokenVerificationError

def test_jwt_token_pair_lifecycle():
    jwt_mgr = JWTManager(secret_key="unit_test_jwt_secret_key_1234567890")

    access_token = jwt_mgr.create_access_token(
        user_id="usr_001",
        email="alice@cloudmart.com",
        roles=["CUSTOMER"],
        permissions=["catalog:read", "orders:write"]
    )
    refresh_token = jwt_mgr.create_refresh_token(user_id="usr_001")

    assert access_token is not None
    assert refresh_token is not None

    payload = jwt_mgr.verify_token(access_token)
    assert payload.sub == "usr_001"
    assert payload.email == "alice@cloudmart.com"
    assert "CUSTOMER" in payload.roles
    assert "orders:write" in payload.permissions

    refresh_payload = jwt_mgr.verify_token(refresh_token)
    assert refresh_payload.sub == "usr_001"

    tampered_token = access_token[:-5] + "XXXXX"
    with pytest.raises(TokenVerificationError):
        jwt_mgr.verify_token(tampered_token)
