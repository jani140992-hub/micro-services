"""Application Service Unit Tests for Shipping & Logistics Service."""

import pytest
from services.shipping_service.services.service import ShipmentConsignmentService
from services.shipping_service.repositories.repository import ShipmentConsignmentRepository
from services.shipping_service.services.cache_service import ShipmentConsignmentCacheService
from services.shipping_service.events.producers import ShipmentConsignmentEventProducer
from services.shipping_service.dto.requests import (
    CreateShipmentConsignmentRequest,
    UpdateShipmentConsignmentRequest,
    ChangeShipmentConsignmentStatusRequest,
    AddTrackingCheckpointRequest,
    AddShippingManifestRequest,
    QueryShipmentConsignmentRequest,
    BatchShipmentConsignmentActionRequest
)
from services.shipping_service.domain.exceptions import ShipmentConsignmentNotFoundException, ShipmentConsignmentAlreadyExistsException

@pytest.fixture
def service():
    repo = ShipmentConsignmentRepository()
    cache = ShipmentConsignmentCacheService()
    producer = ShipmentConsignmentEventProducer()
    return ShipmentConsignmentService(repo, cache, producer)

@pytest.mark.asyncio
async def test_shipping_service_service_create_and_get(service):
    req = CreateShipmentConsignmentRequest(name="Service Created", code="SVC-001", description="Test description")
    created = await service.create(req)
    assert created.name == "Service Created"
    assert created.code == "SVC-001"

    fetched = await service.get_by_id(created.id)
    assert fetched.id == created.id

@pytest.mark.asyncio
async def test_shipping_service_service_duplicate_code_conflict(service):
    req = CreateShipmentConsignmentRequest(name="Original", code="DUP-CODE")
    await service.create(req)
    with pytest.raises(ShipmentConsignmentAlreadyExistsException):
        await service.create(req)

@pytest.mark.asyncio
async def test_shipping_service_service_update(service):
    created = await service.create(CreateShipmentConsignmentRequest(name="Initial Name", code="UPD-01"))
    updated = await service.update(created.id, UpdateShipmentConsignmentRequest(name="Updated Name", description="New Desc"))
    assert updated.name == "Updated Name"
    assert updated.description == "New Desc"

@pytest.mark.asyncio
async def test_shipping_service_service_status_transition(service):
    created = await service.create(CreateShipmentConsignmentRequest(name="Status Item", code="STAT-01"))
    transitioned = await service.change_status(created.id, ChangeShipmentConsignmentStatusRequest(target_status="ACTIVE", reason="Approved"))
    assert transitioned.status == "ACTIVE"

@pytest.mark.asyncio
async def test_shipping_service_service_add_subitems(service):
    created = await service.create(CreateShipmentConsignmentRequest(name="Subitem Parent", code="SUB-PAR"))
    res1 = await service.add_sub_item_1(created.id, AddTrackingCheckpointRequest(name="Sub1", code="S1-01"))
    assert len(res1.sub_items_1) == 1

    res2 = await service.add_sub_item_2(created.id, AddShippingManifestRequest(label="Sub2", value_payload="Payload Data"))
    assert len(res2.sub_items_2) == 1

@pytest.mark.asyncio
async def test_shipping_service_service_batch_actions(service):
    e1 = await service.create(CreateShipmentConsignmentRequest(name="Batch 1", code="B1-01"))
    e2 = await service.create(CreateShipmentConsignmentRequest(name="Batch 2", code="B2-02"))

    batch_req = BatchShipmentConsignmentActionRequest(entity_ids=[e1.id, e2.id], action="ACTIVATE", reason="Batch activate")
    result = await service.batch_action(batch_req)
    assert result.success_count == 2
    assert result.failure_count == 0
