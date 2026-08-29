import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Boolean

class UUIDPrimaryKeyMixin:
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False, nullable=False, index=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def soft_delete(self) -> None:
        self.is_deleted = True
        self.deleted_at = datetime.now(timezone.utc)

class AuditTrailMixin:
    created_by = Column(String(36), nullable=True)
    updated_by = Column(String(36), nullable=True)
