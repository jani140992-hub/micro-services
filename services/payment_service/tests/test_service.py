"""Application Service Unit Tests for Payment & Billing Service."""

import pytest
from services.payment_service.services.service import PaymentTransactionService
from services.payment_service.repositories.repository import PaymentTransactionRepository
from services.payment_service.services.cache_service import PaymentTransactionCacheService
from services.payment_service.events.producers import PaymentTransactionEventProducer
from services.payment_service.dto.requests import (
    CreatePaymentTransactionRequest,
    UpdatePaymentTransactionRequest,
    ChangePaymentTransactionStatusRequest,
    AddLedgerEntryRequest,
    AddRefundItemRequest,
    QueryPaymentTransactionRequest,
    BatchPaymentTransactionActionRequest
)
from services.payment_service.domain.exceptions import PaymentTransactionNotFoundException, PaymentTransactionAlreadyExistsException

@pytest.fixture
def service():
    repo = PaymentTransactionRepository()
    cache = PaymentTransactionCacheService()
    producer = PaymentTransactionEventProducer()
    return PaymentTransactionService(repo, cache, producer)

@pytest.mark.asyncio
async def test_payment_service_service_create_and_get(service):
    req = CreatePaymentTransactionRequest(name="Service Created", code="SVC-001", description="Test description")
    created = await service.create(req)
    assert created.name == "Service Created"
    assert created.code == "SVC-001"

    fetched = await service.get_by_id(created.id)
    assert fetched.id == created.id

@pytest.mark.asyncio
async def test_payment_service_service_duplicate_code_conflict(service):
    req = CreatePaymentTransactionRequest(name="Original", code="DUP-CODE")
    await service.create(req)
    with pytest.raises(PaymentTransactionAlreadyExistsException):
        await service.create(req)

@pytest.mark.asyncio
async def test_payment_service_service_update(service):
    created = await service.create(CreatePaymentTransactionRequest(name="Initial Name", code="UPD-01"))
    updated = await service.update(created.id, UpdatePaymentTransactionRequest(name="Updated Name", description="New Desc"))
    assert updated.name == "Updated Name"
    assert updated.description == "New Desc"

@pytest.mark.asyncio
async def test_payment_service_service_status_transition(service):
    created = await service.create(CreatePaymentTransactionRequest(name="Status Item", code="STAT-01"))
    transitioned = await service.change_status(created.id, ChangePaymentTransactionStatusRequest(target_status="ACTIVE", reason="Approved"))
    assert transitioned.status == "ACTIVE"

@pytest.mark.asyncio
async def test_payment_service_service_add_subitems(service):
    created = await service.create(CreatePaymentTransactionRequest(name="Subitem Parent", code="SUB-PAR"))
    res1 = await service.add_sub_item_1(created.id, AddLedgerEntryRequest(name="Sub1", code="S1-01"))
    assert len(res1.sub_items_1) == 1

    res2 = await service.add_sub_item_2(created.id, AddRefundItemRequest(label="Sub2", value_payload="Payload Data"))
    assert len(res2.sub_items_2) == 1

@pytest.mark.asyncio
async def test_payment_service_service_batch_actions(service):
    e1 = await service.create(CreatePaymentTransactionRequest(name="Batch 1", code="B1-01"))
    e2 = await service.create(CreatePaymentTransactionRequest(name="Batch 2", code="B2-02"))

    batch_req = BatchPaymentTransactionActionRequest(entity_ids=[e1.id, e2.id], action="ACTIVATE", reason="Batch activate")
    result = await service.batch_action(batch_req)
    assert result.success_count == 2
    assert result.failure_count == 0
