"""Application Service Unit Tests for API Gateway Service."""

import pytest
from services.service import GatewayRouteService
from repositories.repository import GatewayRouteRepository
from services.cache_service import GatewayRouteCacheService
from events.producers import GatewayRouteEventProducer
from dto.requests import (
    CreateGatewayRouteRequest,
    UpdateGatewayRouteRequest,
    ChangeGatewayRouteStatusRequest,
    AddRoutePredicateRequest,
    AddRouteFilterRequest,
    QueryGatewayRouteRequest,
    BatchGatewayRouteActionRequest
)
from domain.exceptions import GatewayRouteNotFoundException, GatewayRouteAlreadyExistsException

@pytest.fixture
def service():
    repo = GatewayRouteRepository()
    cache = GatewayRouteCacheService()
    producer = GatewayRouteEventProducer()
    return GatewayRouteService(repo, cache, producer)

@pytest.mark.asyncio
async def test_api_gateway_service_create_and_get(service):
    req = CreateGatewayRouteRequest(name="Service Created", code="SVC-001", description="Test description")
    created = await service.create(req)
    assert created.name == "Service Created"
    assert created.code == "SVC-001"

    fetched = await service.get_by_id(created.id)
    assert fetched.id == created.id

@pytest.mark.asyncio
async def test_api_gateway_service_duplicate_code_conflict(service):
    req = CreateGatewayRouteRequest(name="Original", code="DUP-CODE")
    await service.create(req)
    with pytest.raises(GatewayRouteAlreadyExistsException):
        await service.create(req)

@pytest.mark.asyncio
async def test_api_gateway_service_update(service):
    created = await service.create(CreateGatewayRouteRequest(name="Initial Name", code="UPD-01"))
    updated = await service.update(created.id, UpdateGatewayRouteRequest(name="Updated Name", description="New Desc"))
    assert updated.name == "Updated Name"
    assert updated.description == "New Desc"

@pytest.mark.asyncio
async def test_api_gateway_service_status_transition(service):
    created = await service.create(CreateGatewayRouteRequest(name="Status Item", code="STAT-01"))
    transitioned = await service.change_status(created.id, ChangeGatewayRouteStatusRequest(target_status="ACTIVE", reason="Approved"))
    assert transitioned.status == "ACTIVE"

@pytest.mark.asyncio
async def test_api_gateway_service_add_subitems(service):
    created = await service.create(CreateGatewayRouteRequest(name="Subitem Parent", code="SUB-PAR"))
    res1 = await service.add_sub_item_1(created.id, AddRoutePredicateRequest(name="Sub1", code="S1-01"))
    assert len(res1.sub_items_1) == 1

    res2 = await service.add_sub_item_2(created.id, AddRouteFilterRequest(label="Sub2", value_payload="Payload Data"))
    assert len(res2.sub_items_2) == 1

@pytest.mark.asyncio
async def test_api_gateway_service_batch_actions(service):
    e1 = await service.create(CreateGatewayRouteRequest(name="Batch 1", code="B1-01"))
    e2 = await service.create(CreateGatewayRouteRequest(name="Batch 2", code="B2-02"))

    batch_req = BatchGatewayRouteActionRequest(entity_ids=[e1.id, e2.id], action="ACTIVATE", reason="Batch activate")
    result = await service.batch_action(batch_req)
    assert result.success_count == 2
    assert result.failure_count == 0
