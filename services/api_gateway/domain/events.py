"""Domain Events for API Gateway Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class GatewayRouteCreatedEvent(DomainEvent):
    aggregate_type: str = "api_gateway"
    event_type: str = "gateway.route.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "GatewayRouteCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="gateway.route.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class GatewayRouteUpdatedEvent(DomainEvent):
    aggregate_type: str = "api_gateway"
    event_type: str = "gateway.route.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "GatewayRouteUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="gateway.route.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class GatewayRouteStatusChangedEvent(DomainEvent):
    aggregate_type: str = "api_gateway"
    event_type: str = "gateway.route.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "GatewayRouteStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="gateway.route.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class GatewayRouteSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "api_gateway"
    event_type: str = "gateway.route.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "GatewayRouteSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="gateway.route.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class GatewayRouteSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "api_gateway"
    event_type: str = "gateway.route.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "GatewayRouteSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="gateway.route.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class GatewayRouteDeletedEvent(DomainEvent):
    aggregate_type: str = "api_gateway"
    event_type: str = "gateway.route.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "GatewayRouteDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="gateway.route.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
