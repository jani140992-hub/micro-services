"""REST API Controller Endpoints for Payment & Billing Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from services.payment_service.domain.exceptions import PaymentTransactionNotFoundException, PaymentTransactionAlreadyExistsException
from services.payment_service.dto.requests import (
    CreatePaymentTransactionRequest,
    UpdatePaymentTransactionRequest,
    ChangePaymentTransactionStatusRequest,
    AddLedgerEntryRequest,
    AddRefundItemRequest,
    QueryPaymentTransactionRequest,
    BatchPaymentTransactionActionRequest
)
from services.payment_service.dto.responses import (
    PaymentTransactionSummaryResponse,
    PaymentTransactionDetailResponse,
    PaymentTransactionPageResponse,
    BatchActionResultResponse
)
from services.payment_service.services.service import PaymentTransactionService
from services.payment_service.repositories.repository import PaymentTransactionRepository
from services.payment_service.services.cache_service import PaymentTransactionCacheService
from services.payment_service.events.producers import PaymentTransactionEventProducer

router = APIRouter(prefix="/api/v1/payments", tags=["Payment & Billing Service"])

_repo = PaymentTransactionRepository()
_cache = PaymentTransactionCacheService()
_producer = PaymentTransactionEventProducer()
_service = PaymentTransactionService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> PaymentTransactionService:
    return _service

@router.post("", response_model=PaymentTransactionDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreatePaymentTransactionRequest,
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionDetailResponse:
    """Create a new PaymentTransaction."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=PaymentTransactionDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionDetailResponse:
    """Retrieve PaymentTransaction details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=PaymentTransactionDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdatePaymentTransactionRequest,
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionDetailResponse:
    """Update PaymentTransaction attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=PaymentTransactionDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangePaymentTransactionStatusRequest,
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionDetailResponse:
    """Transition status of PaymentTransaction."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=PaymentTransactionDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddLedgerEntryRequest,
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionDetailResponse:
    """Attach child item (LedgerEntry) to PaymentTransaction."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=PaymentTransactionDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddRefundItemRequest,
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionDetailResponse:
    """Attach child item (RefundItem) to PaymentTransaction."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=PaymentTransactionDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionDetailResponse:
    """Remove child item (LedgerEntry) from PaymentTransaction."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=PaymentTransactionDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionDetailResponse:
    """Remove child item (RefundItem) from PaymentTransaction."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: PaymentTransactionService = Depends(get_service)
) -> None:
    """Soft delete PaymentTransaction."""
    await service.delete(entity_id)

@router.get("", response_model=PaymentTransactionPageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: PaymentTransactionService = Depends(get_service)
) -> PaymentTransactionPageResponse:
    """Paginated search and filter for PaymentTransaction entities."""
    q = QueryPaymentTransactionRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchPaymentTransactionActionRequest,
    service: PaymentTransactionService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
