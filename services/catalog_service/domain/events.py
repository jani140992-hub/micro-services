"""Domain Events for Product Catalog Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class ProductItemCreatedEvent(DomainEvent):
    aggregate_type: str = "catalog_service"
    event_type: str = "catalog.product.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "ProductItemCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="catalog.product.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class ProductItemUpdatedEvent(DomainEvent):
    aggregate_type: str = "catalog_service"
    event_type: str = "catalog.product.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "ProductItemUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="catalog.product.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class ProductItemStatusChangedEvent(DomainEvent):
    aggregate_type: str = "catalog_service"
    event_type: str = "catalog.product.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "ProductItemStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="catalog.product.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class ProductItemSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "catalog_service"
    event_type: str = "catalog.product.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "ProductItemSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="catalog.product.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class ProductItemSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "catalog_service"
    event_type: str = "catalog.product.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "ProductItemSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="catalog.product.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class ProductItemDeletedEvent(DomainEvent):
    aggregate_type: str = "catalog_service"
    event_type: str = "catalog.product.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "ProductItemDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="catalog.product.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
