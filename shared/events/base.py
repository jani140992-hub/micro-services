import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, ConfigDict

class EventMetadata(BaseModel):
    model_config = ConfigDict(frozen=True)
    correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    causation_id: Optional[str] = None
    user_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    schema_version: str = "1.0.0"

class EventBase(BaseModel):
    """Base class for all domain and integration events."""
    model_config = ConfigDict(frozen=True)
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: EventMetadata = Field(default_factory=EventMetadata)
    data: Dict[str, Any]

class CloudEvent(BaseModel):
    """CloudEvents v1.0 specification compliant structure."""
    model_config = ConfigDict(frozen=True)
    specversion: str = "1.0"
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    source: str
    type: str
    datacontenttype: str = "application/json"
    dataschema: Optional[str] = None
    subject: Optional[str] = None
    time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    data: Dict[str, Any]

    @classmethod
    def from_event_base(cls, event: EventBase, source_service: str) -> "CloudEvent":
        return cls(
            id=event.event_id,
            source=f"urn:cloudmart:{source_service}",
            type=event.event_type,
            time=event.occurred_at,
            subject=event.metadata.correlation_id,
            data=event.data
        )

class DomainEvent(EventBase):
    """Domain events representing state mutations within a single bounded context."""
    aggregate_id: str
    aggregate_type: str
    version: int = 1

class IntegrationEvent(EventBase):
    """Cross-service boundary integration events published to message brokers."""
    origin_service: str
