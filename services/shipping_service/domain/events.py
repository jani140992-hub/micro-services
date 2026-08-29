"""Domain Events for Shipping & Logistics Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class ShipmentConsignmentCreatedEvent(DomainEvent):
    aggregate_type: str = "shipping_service"
    event_type: str = "shipping.consignment.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "ShipmentConsignmentCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="shipping.consignment.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class ShipmentConsignmentUpdatedEvent(DomainEvent):
    aggregate_type: str = "shipping_service"
    event_type: str = "shipping.consignment.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "ShipmentConsignmentUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="shipping.consignment.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class ShipmentConsignmentStatusChangedEvent(DomainEvent):
    aggregate_type: str = "shipping_service"
    event_type: str = "shipping.consignment.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "ShipmentConsignmentStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="shipping.consignment.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class ShipmentConsignmentSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "shipping_service"
    event_type: str = "shipping.consignment.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "ShipmentConsignmentSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="shipping.consignment.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class ShipmentConsignmentSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "shipping_service"
    event_type: str = "shipping.consignment.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "ShipmentConsignmentSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="shipping.consignment.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class ShipmentConsignmentDeletedEvent(DomainEvent):
    aggregate_type: str = "shipping_service"
    event_type: str = "shipping.consignment.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "ShipmentConsignmentDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="shipping.consignment.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
