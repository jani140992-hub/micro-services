"""Configuration Settings for Inventory Management Service."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="INVENTORY_", env_file=".env", extra="ignore")

    SERVICE_NAME: str = "inventory_service"
    PORT: int = 8004
    ENVIRONMENT: str = "production"
    DEBUG: bool = False

    DATABASE_URL: str = "postgresql+asyncpg://cloudmart_user:cloudmart_password@localhost:5432/inventory_db"
    REDIS_URL: str = "redis://localhost:6379/4"
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"

    JWT_SECRET_KEY: str = "cloudmart_super_secure_secret_key_change_in_prod"
    JWT_ALGORITHM: str = "HS256"

    CACHE_TTL_SECONDS: int = 300
    RATE_LIMIT_PER_MINUTE: int = 120
    CIRCUIT_BREAKER_FAILURE_THRESHOLD: int = 5
    CIRCUIT_BREAKER_RECOVERY_SECONDS: float = 30.0

settings = Settings()
