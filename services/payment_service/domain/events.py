"""Domain Events for Payment & Billing Service."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from shared.events.base import DomainEvent, EventMetadata

class PaymentTransactionCreatedEvent(DomainEvent):
    aggregate_type: str = "payment_service"
    event_type: str = "payment.tx.created"
    aggregate_id: str
    payload: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> "PaymentTransactionCreatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="payment.tx.created",
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=payload,
            payload=payload
        )

class PaymentTransactionUpdatedEvent(DomainEvent):
    aggregate_type: str = "payment_service"
    event_type: str = "payment.tx.updated"
    aggregate_id: str
    version: int
    changes: Dict[str, Any]

    @classmethod
    def create(cls, aggregate_id: str, version: int, changes: Dict[str, Any], correlation_id: Optional[str] = None) -> "PaymentTransactionUpdatedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="payment.tx.updated",
            version=version,
            metadata=EventMetadata(correlation_id=correlation_id or str(uuid.uuid4())),
            data=changes,
            changes=changes
        )

class PaymentTransactionStatusChangedEvent(DomainEvent):
    aggregate_type: str = "payment_service"
    event_type: str = "payment.tx.status_changed"
    aggregate_id: str
    old_status: str
    new_status: str
    reason: Optional[str] = None

    @classmethod
    def create(cls, aggregate_id: str, old_status: str, new_status: str, reason: Optional[str] = None) -> "PaymentTransactionStatusChangedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="payment.tx.status_changed",
            metadata=EventMetadata(),
            data={"old_status": old_status, "new_status": new_status, "reason": reason},
            old_status=old_status,
            new_status=new_status,
            reason=reason
        )

class PaymentTransactionSubItem1AddedEvent(DomainEvent):
    aggregate_type: str = "payment_service"
    event_type: str = "payment.tx.sub1_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "PaymentTransactionSubItem1AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="payment.tx.sub1_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class PaymentTransactionSubItem2AddedEvent(DomainEvent):
    aggregate_type: str = "payment_service"
    event_type: str = "payment.tx.sub2_added"
    aggregate_id: str
    sub_item_id: str

    @classmethod
    def create(cls, aggregate_id: str, sub_item_id: str) -> "PaymentTransactionSubItem2AddedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="payment.tx.sub2_added",
            metadata=EventMetadata(),
            data={"sub_item_id": sub_item_id},
            sub_item_id=sub_item_id
        )

class PaymentTransactionDeletedEvent(DomainEvent):
    aggregate_type: str = "payment_service"
    event_type: str = "payment.tx.deleted"
    aggregate_id: str
    deleted_by: str

    @classmethod
    def create(cls, aggregate_id: str, deleted_by: str) -> "PaymentTransactionDeletedEvent":
        return cls(
            aggregate_id=aggregate_id,
            event_type="payment.tx.deleted",
            metadata=EventMetadata(),
            data={"deleted_by": deleted_by},
            deleted_by=deleted_by
        )
