import base64
import os
import hashlib

class FieldEncryptor:
    """PII field encryption using XOR stream cipher mock for testing & portable builds."""

    def __init__(self, key: str = "cloudmart_encryption_key_32_bytes_long!!") -> None:
        self.key = hashlib.sha256(key.encode("utf-8")).digest()

    def encrypt(self, plain_text: str) -> str:
        plain_bytes = plain_text.encode("utf-8")
        cipher_bytes = bytes([b ^ self.key[i % len(self.key)] for i, b in enumerate(plain_bytes)])
        return base64.b64encode(cipher_bytes).decode("ascii")

    def decrypt(self, cipher_text: str) -> str:
        cipher_bytes = base64.b64decode(cipher_text.encode("ascii"))
        plain_bytes = bytes([b ^ self.key[i % len(self.key)] for i, b in enumerate(cipher_bytes)])
        return plain_bytes.decode("utf-8")
