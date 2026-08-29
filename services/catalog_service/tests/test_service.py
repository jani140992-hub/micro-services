"""Application Service Unit Tests for Product Catalog Service."""

import pytest
from services.catalog_service.services.service import ProductItemService
from services.catalog_service.repositories.repository import ProductItemRepository
from services.catalog_service.services.cache_service import ProductItemCacheService
from services.catalog_service.events.producers import ProductItemEventProducer
from services.catalog_service.dto.requests import (
    CreateProductItemRequest,
    UpdateProductItemRequest,
    ChangeProductItemStatusRequest,
    AddProductVariantRequest,
    AddProductAttributeRequest,
    QueryProductItemRequest,
    BatchProductItemActionRequest
)
from services.catalog_service.domain.exceptions import ProductItemNotFoundException, ProductItemAlreadyExistsException

@pytest.fixture
def service():
    repo = ProductItemRepository()
    cache = ProductItemCacheService()
    producer = ProductItemEventProducer()
    return ProductItemService(repo, cache, producer)

@pytest.mark.asyncio
async def test_catalog_service_service_create_and_get(service):
    req = CreateProductItemRequest(name="Service Created", code="SVC-001", description="Test description")
    created = await service.create(req)
    assert created.name == "Service Created"
    assert created.code == "SVC-001"

    fetched = await service.get_by_id(created.id)
    assert fetched.id == created.id

@pytest.mark.asyncio
async def test_catalog_service_service_duplicate_code_conflict(service):
    req = CreateProductItemRequest(name="Original", code="DUP-CODE")
    await service.create(req)
    with pytest.raises(ProductItemAlreadyExistsException):
        await service.create(req)

@pytest.mark.asyncio
async def test_catalog_service_service_update(service):
    created = await service.create(CreateProductItemRequest(name="Initial Name", code="UPD-01"))
    updated = await service.update(created.id, UpdateProductItemRequest(name="Updated Name", description="New Desc"))
    assert updated.name == "Updated Name"
    assert updated.description == "New Desc"

@pytest.mark.asyncio
async def test_catalog_service_service_status_transition(service):
    created = await service.create(CreateProductItemRequest(name="Status Item", code="STAT-01"))
    transitioned = await service.change_status(created.id, ChangeProductItemStatusRequest(target_status="ACTIVE", reason="Approved"))
    assert transitioned.status == "ACTIVE"

@pytest.mark.asyncio
async def test_catalog_service_service_add_subitems(service):
    created = await service.create(CreateProductItemRequest(name="Subitem Parent", code="SUB-PAR"))
    res1 = await service.add_sub_item_1(created.id, AddProductVariantRequest(name="Sub1", code="S1-01"))
    assert len(res1.sub_items_1) == 1

    res2 = await service.add_sub_item_2(created.id, AddProductAttributeRequest(label="Sub2", value_payload="Payload Data"))
    assert len(res2.sub_items_2) == 1

@pytest.mark.asyncio
async def test_catalog_service_service_batch_actions(service):
    e1 = await service.create(CreateProductItemRequest(name="Batch 1", code="B1-01"))
    e2 = await service.create(CreateProductItemRequest(name="Batch 2", code="B2-02"))

    batch_req = BatchProductItemActionRequest(entity_ids=[e1.id, e2.id], action="ACTIVATE", reason="Batch activate")
    result = await service.batch_action(batch_req)
    assert result.success_count == 2
    assert result.failure_count == 0
