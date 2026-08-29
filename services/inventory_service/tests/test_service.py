"""Application Service Unit Tests for Inventory Management Service."""

import pytest
from services.inventory_service.services.service import StockItemService
from services.inventory_service.repositories.repository import StockItemRepository
from services.inventory_service.services.cache_service import StockItemCacheService
from services.inventory_service.events.producers import StockItemEventProducer
from services.inventory_service.dto.requests import (
    CreateStockItemRequest,
    UpdateStockItemRequest,
    ChangeStockItemStatusRequest,
    AddWarehouseLocationRequest,
    AddStockReservationRequest,
    QueryStockItemRequest,
    BatchStockItemActionRequest
)
from services.inventory_service.domain.exceptions import StockItemNotFoundException, StockItemAlreadyExistsException

@pytest.fixture
def service():
    repo = StockItemRepository()
    cache = StockItemCacheService()
    producer = StockItemEventProducer()
    return StockItemService(repo, cache, producer)

@pytest.mark.asyncio
async def test_inventory_service_service_create_and_get(service):
    req = CreateStockItemRequest(name="Service Created", code="SVC-001", description="Test description")
    created = await service.create(req)
    assert created.name == "Service Created"
    assert created.code == "SVC-001"

    fetched = await service.get_by_id(created.id)
    assert fetched.id == created.id

@pytest.mark.asyncio
async def test_inventory_service_service_duplicate_code_conflict(service):
    req = CreateStockItemRequest(name="Original", code="DUP-CODE")
    await service.create(req)
    with pytest.raises(StockItemAlreadyExistsException):
        await service.create(req)

@pytest.mark.asyncio
async def test_inventory_service_service_update(service):
    created = await service.create(CreateStockItemRequest(name="Initial Name", code="UPD-01"))
    updated = await service.update(created.id, UpdateStockItemRequest(name="Updated Name", description="New Desc"))
    assert updated.name == "Updated Name"
    assert updated.description == "New Desc"

@pytest.mark.asyncio
async def test_inventory_service_service_status_transition(service):
    created = await service.create(CreateStockItemRequest(name="Status Item", code="STAT-01"))
    transitioned = await service.change_status(created.id, ChangeStockItemStatusRequest(target_status="ACTIVE", reason="Approved"))
    assert transitioned.status == "ACTIVE"

@pytest.mark.asyncio
async def test_inventory_service_service_add_subitems(service):
    created = await service.create(CreateStockItemRequest(name="Subitem Parent", code="SUB-PAR"))
    res1 = await service.add_sub_item_1(created.id, AddWarehouseLocationRequest(name="Sub1", code="S1-01"))
    assert len(res1.sub_items_1) == 1

    res2 = await service.add_sub_item_2(created.id, AddStockReservationRequest(label="Sub2", value_payload="Payload Data"))
    assert len(res2.sub_items_2) == 1

@pytest.mark.asyncio
async def test_inventory_service_service_batch_actions(service):
    e1 = await service.create(CreateStockItemRequest(name="Batch 1", code="B1-01"))
    e2 = await service.create(CreateStockItemRequest(name="Batch 2", code="B2-02"))

    batch_req = BatchStockItemActionRequest(entity_ids=[e1.id, e2.id], action="ACTIVATE", reason="Batch activate")
    result = await service.batch_action(batch_req)
    assert result.success_count == 2
    assert result.failure_count == 0
