"""REST API Controller Endpoints for Order Management Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from services.order_service.domain.exceptions import CustomerOrderNotFoundException, CustomerOrderAlreadyExistsException
from services.order_service.dto.requests import (
    CreateCustomerOrderRequest,
    UpdateCustomerOrderRequest,
    ChangeCustomerOrderStatusRequest,
    AddOrderLineItemRequest,
    AddOrderStatusRecordRequest,
    QueryCustomerOrderRequest,
    BatchCustomerOrderActionRequest
)
from services.order_service.dto.responses import (
    CustomerOrderSummaryResponse,
    CustomerOrderDetailResponse,
    CustomerOrderPageResponse,
    BatchActionResultResponse
)
from services.order_service.services.service import CustomerOrderService
from services.order_service.repositories.repository import CustomerOrderRepository
from services.order_service.services.cache_service import CustomerOrderCacheService
from services.order_service.events.producers import CustomerOrderEventProducer

router = APIRouter(prefix="/api/v1/orders", tags=["Order Management Service"])

_repo = CustomerOrderRepository()
_cache = CustomerOrderCacheService()
_producer = CustomerOrderEventProducer()
_service = CustomerOrderService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> CustomerOrderService:
    return _service

@router.post("", response_model=CustomerOrderDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateCustomerOrderRequest,
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderDetailResponse:
    """Create a new CustomerOrder."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=CustomerOrderDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderDetailResponse:
    """Retrieve CustomerOrder details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=CustomerOrderDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateCustomerOrderRequest,
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderDetailResponse:
    """Update CustomerOrder attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=CustomerOrderDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeCustomerOrderStatusRequest,
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderDetailResponse:
    """Transition status of CustomerOrder."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=CustomerOrderDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddOrderLineItemRequest,
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderDetailResponse:
    """Attach child item (OrderLineItem) to CustomerOrder."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=CustomerOrderDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddOrderStatusRecordRequest,
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderDetailResponse:
    """Attach child item (OrderStatusRecord) to CustomerOrder."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=CustomerOrderDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderDetailResponse:
    """Remove child item (OrderLineItem) from CustomerOrder."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=CustomerOrderDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderDetailResponse:
    """Remove child item (OrderStatusRecord) from CustomerOrder."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: CustomerOrderService = Depends(get_service)
) -> None:
    """Soft delete CustomerOrder."""
    await service.delete(entity_id)

@router.get("", response_model=CustomerOrderPageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: CustomerOrderService = Depends(get_service)
) -> CustomerOrderPageResponse:
    """Paginated search and filter for CustomerOrder entities."""
    q = QueryCustomerOrderRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchCustomerOrderActionRequest,
    service: CustomerOrderService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
