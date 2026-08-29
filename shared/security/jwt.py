import jwt
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class TokenPayload(BaseModel):
    sub: str
    email: str
    roles: List[str] = Field(default_factory=list)
    permissions: List[str] = Field(default_factory=list)
    exp: int
    iat: int
    jti: str

class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int

class TokenVerificationError(Exception):
    pass

class JWTManager:
    """Cryptographic JWT issuer and verifier."""

    def __init__(self, secret_key: str = "cloudmart_super_secure_secret_key_change_in_prod", algorithm: str = "HS256") -> None:
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_access_token(self, user_id: str, email: str, roles: List[str], permissions: List[str], expires_delta: Optional[timedelta] = None) -> str:
        now = datetime.now(timezone.utc)
        expire = now + (expires_delta or timedelta(minutes=15))
        payload = {
            "sub": user_id,
            "email": email,
            "roles": roles,
            "permissions": permissions,
            "iat": int(now.timestamp()),
            "exp": int(expire.timestamp()),
            "jti": str(uuid.uuid4())
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def create_refresh_token(self, user_id: str, expires_delta: Optional[timedelta] = None) -> str:
        now = datetime.now(timezone.utc)
        expire = now + (expires_delta or timedelta(days=7))
        payload = {
            "sub": user_id,
            "iat": int(now.timestamp()),
            "exp": int(expire.timestamp()),
            "jti": str(uuid.uuid4()),
            "type": "refresh"
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token: str) -> TokenPayload:
        try:
            data = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return TokenPayload(**data)
        except jwt.ExpiredSignatureError:
            raise TokenVerificationError("Token has expired")
        except jwt.InvalidTokenError as e:
            raise TokenVerificationError(f"Invalid token: {e}")
