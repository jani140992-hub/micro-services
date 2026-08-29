"""Domain Events for Analytics & BI Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class StreamMetricRecordCreatedEvent(DomainEvent):
    aggregate_type: str = "analytics_service"
    event_type: str = "analytics.metric.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "StreamMetricRecordCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="analytics.metric.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class StreamMetricRecordUpdatedEvent(DomainEvent):
    aggregate_type: str = "analytics_service"
    event_type: str = "analytics.metric.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "StreamMetricRecordUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="analytics.metric.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class StreamMetricRecordStatusChangedEvent(DomainEvent):
    aggregate_type: str = "analytics_service"
    event_type: str = "analytics.metric.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "StreamMetricRecordStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="analytics.metric.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class StreamMetricRecordSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "analytics_service"
    event_type: str = "analytics.metric.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "StreamMetricRecordSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="analytics.metric.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class StreamMetricRecordSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "analytics_service"
    event_type: str = "analytics.metric.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "StreamMetricRecordSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="analytics.metric.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class StreamMetricRecordDeletedEvent(DomainEvent):
    aggregate_type: str = "analytics_service"
    event_type: str = "analytics.metric.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "StreamMetricRecordDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="analytics.metric.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
