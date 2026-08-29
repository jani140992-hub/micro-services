"""Domain Events for Inventory Management Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class StockItemCreatedEvent(DomainEvent):
    aggregate_type: str = "inventory_service"
    event_type: str = "inventory.stock.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "StockItemCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="inventory.stock.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class StockItemUpdatedEvent(DomainEvent):
    aggregate_type: str = "inventory_service"
    event_type: str = "inventory.stock.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "StockItemUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="inventory.stock.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class StockItemStatusChangedEvent(DomainEvent):
    aggregate_type: str = "inventory_service"
    event_type: str = "inventory.stock.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "StockItemStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="inventory.stock.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class StockItemSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "inventory_service"
    event_type: str = "inventory.stock.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "StockItemSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="inventory.stock.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class StockItemSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "inventory_service"
    event_type: str = "inventory.stock.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "StockItemSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="inventory.stock.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class StockItemDeletedEvent(DomainEvent):
    aggregate_type: str = "inventory_service"
    event_type: str = "inventory.stock.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "StockItemDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="inventory.stock.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
