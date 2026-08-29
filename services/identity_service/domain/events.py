"""Domain Events for Identity & Authentication Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class UserCredentialCreatedEvent(DomainEvent):
    aggregate_type: str = "identity_service"
    event_type: str = "identity.user.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "UserCredentialCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="identity.user.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class UserCredentialUpdatedEvent(DomainEvent):
    aggregate_type: str = "identity_service"
    event_type: str = "identity.user.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "UserCredentialUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="identity.user.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class UserCredentialStatusChangedEvent(DomainEvent):
    aggregate_type: str = "identity_service"
    event_type: str = "identity.user.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "UserCredentialStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="identity.user.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class UserCredentialSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "identity_service"
    event_type: str = "identity.user.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "UserCredentialSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="identity.user.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class UserCredentialSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "identity_service"
    event_type: str = "identity.user.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "UserCredentialSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="identity.user.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class UserCredentialDeletedEvent(DomainEvent):
    aggregate_type: str = "identity_service"
    event_type: str = "identity.user.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "UserCredentialDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="identity.user.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
