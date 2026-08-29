"""Domain Events for User Profile Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class UserProfileCreatedEvent(DomainEvent):
    aggregate_type: str = "user_service"
    event_type: str = "user.profile.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "UserProfileCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="user.profile.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class UserProfileUpdatedEvent(DomainEvent):
    aggregate_type: str = "user_service"
    event_type: str = "user.profile.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "UserProfileUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="user.profile.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class UserProfileStatusChangedEvent(DomainEvent):
    aggregate_type: str = "user_service"
    event_type: str = "user.profile.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "UserProfileStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="user.profile.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class UserProfileSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "user_service"
    event_type: str = "user.profile.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "UserProfileSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="user.profile.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class UserProfileSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "user_service"
    event_type: str = "user.profile.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "UserProfileSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="user.profile.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class UserProfileDeletedEvent(DomainEvent):
    aggregate_type: str = "user_service"
    event_type: str = "user.profile.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "UserProfileDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="user.profile.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
