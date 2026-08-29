"""Domain Unit Tests for Inventory Management Service."""

import pytest
from domain.models import StockItemAggregate, WarehouseLocation, StockReservation
from domain.exceptions import (
    InvalidStockItemStateTransitionException,
    StockItemValidationException,
    StockItemQuotaExceededException
)

def test_inventory_service_aggregate_creation():
    agg = StockItemAggregate(name="Test StockItem", code="TEST-001")
    agg.validate_invariants()
    assert agg.name == "Test StockItem"
    assert agg.code == "TEST-001"
    assert agg.status == "DRAFT"
    assert agg.version == 1

def test_inventory_service_invalid_name_fails():
    agg = StockItemAggregate(name="X", code="VALID-CODE")
    with pytest.raises(StockItemValidationException):
        agg.validate_invariants()

def test_inventory_service_state_transition_success():
    agg = StockItemAggregate(name="Test Transition", code="TRANS-001")
    agg.transition_status("ACTIVE", actor_id="user_admin", reason="Passed review")
    assert agg.status == "ACTIVE"
    assert agg.version == 2
    assert len(agg.status_history) == 1

def test_inventory_service_state_transition_illegal_raises():
    agg = StockItemAggregate(name="Test Illegal", code="ILL-001")
    with pytest.raises(InvalidStockItemStateTransitionException):
        agg.transition_status("COMPLETED", actor_id="user_admin")

def test_inventory_service_add_and_remove_sub1():
    agg = StockItemAggregate(name="Parent Entity", code="PARENT-001")
    child = WarehouseLocation(name="Child Item", code="C-001")
    agg.add_sub_item_1(child, actor_id="admin")
    assert len(agg.sub_items_1) == 1
    assert agg.version == 2

    # Duplicate code should fail
    with pytest.raises(StockItemValidationException):
        agg.add_sub_item_1(WarehouseLocation(name="Child 2", code="C-001"), actor_id="admin")

    # Removal
    removed = agg.remove_sub_item_1(child.id)
    assert removed is True
    assert len(agg.sub_items_1) == 0

def test_inventory_service_add_and_remove_sub2():
    agg = StockItemAggregate(name="Parent Entity", code="PARENT-002")
    child = StockReservation(label="Label 1", value_payload="val")
    agg.add_sub_item_2(child, actor_id="admin")
    assert len(agg.sub_items_2) == 1

    removed = agg.remove_sub_item_2(child.id)
    assert removed is True
    assert len(agg.sub_items_2) == 0

def test_inventory_service_soft_delete():
    agg = StockItemAggregate(name="Entity to delete", code="DEL-001")
    agg.soft_delete(actor_id="tester")
    assert agg.is_deleted is True
    assert agg.status == "ARCHIVED"

    events = agg.pull_events()
    assert len(events) == 1
    assert events[0].event_type == "inventory.stock.deleted"
