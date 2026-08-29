"""SQLAlchemy ORM Models for Order Management Service."""

import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, JSON, Text, ForeignKey, Index
from sqlalchemy.orm import declarative_base, relationship
from shared.database.mixins import TimestampMixin, UUIDPrimaryKeyMixin, SoftDeleteMixin

Base = declarative_base()

class CustomerOrderORM(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "customer_orders"

    tenant_id = Column(String(50), default="default", nullable=False, index=True)
    name = Column(String(150), nullable=False, index=True)
    code = Column(String(50), nullable=False, unique=True, index=True)
    status = Column(String(30), default="DRAFT", nullable=False, index=True)
    category = Column(String(50), default="STANDARD", nullable=False, index=True)
    version = Column(Integer, default=1, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    attributes_json = Column(JSON, default=dict, nullable=False)
    status_history_json = Column(JSON, default=list, nullable=False)

    sub_items_1 = relationship("OrderLineItemORM", back_populates="parent_entity", cascade="all, delete-orphan", lazy="selectin")
    sub_items_2 = relationship("OrderStatusRecordORM", back_populates="parent_entity", cascade="all, delete-orphan", lazy="selectin")

    __table_args__ = (
        Index("ix_customer_orders_tenant_status", "tenant_id", "status"),
        Index("ix_customer_orders_tenant_category", "tenant_id", "category"),
    )

class OrderLineItemORM(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "customer_orders_sub1"

    parent_id = Column(String(36), ForeignKey("customer_orders.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    priority = Column(Integer, default=10, nullable=False)
    config_json = Column(JSON, default=dict, nullable=False)

    parent_entity = relationship("CustomerOrderORM", back_populates="sub_items_1")

class OrderStatusRecordORM(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "customer_orders_sub2"

    parent_id = Column(String(36), ForeignKey("customer_orders.id", ondelete="CASCADE"), nullable=False, index=True)
    label = Column(String(100), nullable=False)
    value_payload = Column(Text, nullable=False)
    score = Column(Float, default=1.0, nullable=False)
    tags_json = Column(JSON, default=list, nullable=False)

    parent_entity = relationship("CustomerOrderORM", back_populates="sub_items_2")
