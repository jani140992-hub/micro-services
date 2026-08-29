import hashlib
import os
import hmac

class PasswordHasher:
    """PBKDF2-HMAC-SHA256 password hasher with constant-time verification."""

    @staticmethod
    def hash_password(password: str) -> str:
        salt = os.urandom(16)
        key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
        return f"{salt.hex()}:{key.hex()}"

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        try:
            salt_hex, key_hex = hashed.split(":")
            salt = bytes.fromhex(salt_hex)
            expected_key = bytes.fromhex(key_hex)
            computed_key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
            return hmac.compare_digest(computed_key, expected_key)
        except Exception:
            return False
