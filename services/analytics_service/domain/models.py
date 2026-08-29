"""Domain Models and Aggregate Root for Analytics & BI Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, ConfigDict

from .value_objects import Money, StatusHistoryEntry
from .exceptions import (
    InvalidStreamMetricRecordStateTransitionException,
    StreamMetricRecordValidationException,
    StreamMetricRecordQuotaExceededException
)
from .events import (
    StreamMetricRecordCreatedEvent,
    StreamMetricRecordUpdatedEvent,
    StreamMetricRecordStatusChangedEvent,
    StreamMetricRecordSubItem1AddedEvent,
    StreamMetricRecordSubItem2AddedEvent,
    StreamMetricRecordDeletedEvent
)

class TimeSeriesDataPoint(BaseModel):
    """Child Entity 1 of StreamMetricRecord Aggregate."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    code: str
    is_active: bool = True
    priority: int = 10
    config_data: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def update_config(self, new_config: Dict[str, Any]) -> None:
        self.config_data.update(new_config)

class AggregationDimension(BaseModel):
    """Child Entity 2 of StreamMetricRecord Aggregate."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    label: str
    value_payload: str
    score: float = 1.0
    tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

class StreamMetricRecordAggregate(BaseModel):
    """
    Aggregate Root for Analytics & BI Service.
    Encapsulates all domain invariants, business rules, and state mutators.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    tenant_id: str = "default"
    name: str
    code: str
    status: str = "DRAFT"
    version: int = 1
    description: Optional[str] = None
    category: str = "STANDARD"
    is_active: bool = True
    is_deleted: bool = False

    sub_items_1: List[TimeSeriesDataPoint] = Field(default_factory=list)
    sub_items_2: List[AggregationDimension] = Field(default_factory=list)
    attributes: Dict[str, Any] = Field(default_factory=dict)
    status_history: List[StatusHistoryEntry] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    _pending_events: List[Any] = []

    def validate_invariants(self) -> None:
        if not self.name or len(self.name.strip()) < 2:
            raise StreamMetricRecordValidationException("name", "Name must contain at least 2 characters")
        if not self.code or len(self.code.strip()) < 2:
            raise StreamMetricRecordValidationException("code", "Code must contain at least 2 characters")
        if len(self.sub_items_1) > 100:
            raise StreamMetricRecordQuotaExceededException("TimeSeriesDataPoint", 100)
        if len(self.sub_items_2) > 200:
            raise StreamMetricRecordQuotaExceededException("AggregationDimension", 200)

    def transition_status(self, target_status: str, actor_id: str, reason: Optional[str] = None) -> None:
        state_flow: Dict[str, List[str]] = {
            "DRAFT": ["ACTIVE", "REVIEW", "CANCELLED", "ARCHIVED"],
            "REVIEW": ["ACTIVE", "REJECTED", "DRAFT"],
            "ACTIVE": ["SUSPENDED", "PENDING", "PROCESSING", "COMPLETED", "ARCHIVED"],
            "PENDING": ["ACTIVE", "FAILED", "PROCESSING"],
            "PROCESSING": ["COMPLETED", "FAILED"],
            "REJECTED": ["DRAFT", "ARCHIVED"],
            "SUSPENDED": ["ACTIVE", "ARCHIVED"],
            "COMPLETED": ["ARCHIVED"],
            "FAILED": ["DRAFT", "ARCHIVED"],
            "CANCELLED": ["ARCHIVED"],
            "ARCHIVED": []
        }
        allowed = state_flow.get(self.status, [])
        if target_status.upper() not in allowed:
            raise InvalidStreamMetricRecordStateTransitionException(self.status, target_status.upper())

        prev_status = self.status
        self.status = target_status.upper()
        self.version += 1
        self.updated_at = datetime.now(timezone.utc)

        self.status_history.append(StatusHistoryEntry(
            from_status=prev_status,
            to_status=self.status,
            changed_by=actor_id,
            reason=reason
        ))

        self._pending_events.append(StreamMetricRecordStatusChangedEvent.create(
            aggregate_id=self.id,
            old_status=prev_status,
            new_status=self.status,
            reason=reason
        ))

    def update_attributes(self, name: Optional[str], description: Optional[str], attributes: Optional[Dict[str, Any]], actor_id: str) -> None:
        delta: Dict[str, Any] = {}
        if name and name != self.name:
            delta["name"] = {"old": self.name, "new": name}
            self.name = name
        if description is not None and description != self.description:
            delta["description"] = {"old": self.description, "new": description}
            self.description = description
        if attributes:
            self.attributes.update(attributes)
            delta["attributes"] = attributes

        if delta:
            self.version += 1
            self.updated_at = datetime.now(timezone.utc)
            self._pending_events.append(StreamMetricRecordUpdatedEvent.create(
                aggregate_id=self.id,
                version=self.version,
                changes=delta
            ))

    def add_sub_item_1(self, item: TimeSeriesDataPoint, actor_id: str) -> None:
        if any(x.code == item.code for x in self.sub_items_1):
            raise StreamMetricRecordValidationException("TimeSeriesDataPoint.code", f"Code '{item.code}' already exists in aggregate")
        self.sub_items_1.append(item)
        self.version += 1
        self.updated_at = datetime.now(timezone.utc)
        self._pending_events.append(StreamMetricRecordSubItem1AddedEvent.create(self.id, item.id))

    def add_sub_item_2(self, item: AggregationDimension, actor_id: str) -> None:
        self.sub_items_2.append(item)
        self.version += 1
        self.updated_at = datetime.now(timezone.utc)
        self._pending_events.append(StreamMetricRecordSubItem2AddedEvent.create(self.id, item.id))

    def remove_sub_item_1(self, sub_item_id: str) -> bool:
        init_len = len(self.sub_items_1)
        self.sub_items_1 = [x for x in self.sub_items_1 if x.id != sub_item_id]
        if len(self.sub_items_1) < init_len:
            self.version += 1
            self.updated_at = datetime.now(timezone.utc)
            return True
        return False

    def remove_sub_item_2(self, sub_item_id: str) -> bool:
        init_len = len(self.sub_items_2)
        self.sub_items_2 = [x for x in self.sub_items_2 if x.id != sub_item_id]
        if len(self.sub_items_2) < init_len:
            self.version += 1
            self.updated_at = datetime.now(timezone.utc)
            return True
        return False

    def soft_delete(self, actor_id: str) -> None:
        self.is_deleted = True
        self.status = "ARCHIVED"
        self.version += 1
        self.updated_at = datetime.now(timezone.utc)
        self._pending_events.append(StreamMetricRecordDeletedEvent.create(self.id, deleted_by=actor_id))

    def pull_events(self) -> List[Any]:
        events = list(self._pending_events)
        self._pending_events.clear()
        return events
