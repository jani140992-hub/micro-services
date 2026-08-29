"""Domain Events for Notification & Messaging Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class NotificationMessageCreatedEvent(DomainEvent):
    aggregate_type: str = "notification_service"
    event_type: str = "notification.dispatch.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "NotificationMessageCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="notification.dispatch.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class NotificationMessageUpdatedEvent(DomainEvent):
    aggregate_type: str = "notification_service"
    event_type: str = "notification.dispatch.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "NotificationMessageUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="notification.dispatch.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class NotificationMessageStatusChangedEvent(DomainEvent):
    aggregate_type: str = "notification_service"
    event_type: str = "notification.dispatch.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "NotificationMessageStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="notification.dispatch.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class NotificationMessageSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "notification_service"
    event_type: str = "notification.dispatch.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "NotificationMessageSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="notification.dispatch.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class NotificationMessageSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "notification_service"
    event_type: str = "notification.dispatch.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "NotificationMessageSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="notification.dispatch.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class NotificationMessageDeletedEvent(DomainEvent):
    aggregate_type: str = "notification_service"
    event_type: str = "notification.dispatch.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "NotificationMessageDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="notification.dispatch.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
