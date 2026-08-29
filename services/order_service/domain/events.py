"""Domain Events for Order Management Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class CustomerOrderCreatedEvent(DomainEvent):
    aggregate_type: str = "order_service"
    event_type: str = "order.lifecycle.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "CustomerOrderCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="order.lifecycle.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class CustomerOrderUpdatedEvent(DomainEvent):
    aggregate_type: str = "order_service"
    event_type: str = "order.lifecycle.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "CustomerOrderUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="order.lifecycle.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class CustomerOrderStatusChangedEvent(DomainEvent):
    aggregate_type: str = "order_service"
    event_type: str = "order.lifecycle.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "CustomerOrderStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="order.lifecycle.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class CustomerOrderSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "order_service"
    event_type: str = "order.lifecycle.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "CustomerOrderSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="order.lifecycle.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class CustomerOrderSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "order_service"
    event_type: str = "order.lifecycle.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "CustomerOrderSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="order.lifecycle.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class CustomerOrderDeletedEvent(DomainEvent):
    aggregate_type: str = "order_service"
    event_type: str = "order.lifecycle.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "CustomerOrderDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="order.lifecycle.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
