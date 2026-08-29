"""REST API Controller Endpoints for Inventory Management Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from domain.exceptions import StockItemNotFoundException, StockItemAlreadyExistsException
from dto.requests import (
    CreateStockItemRequest,
    UpdateStockItemRequest,
    ChangeStockItemStatusRequest,
    AddWarehouseLocationRequest,
    AddStockReservationRequest,
    QueryStockItemRequest,
    BatchStockItemActionRequest
)
from dto.responses import (
    StockItemSummaryResponse,
    StockItemDetailResponse,
    StockItemPageResponse,
    BatchActionResultResponse
)
from services.service import StockItemService
from repositories.repository import StockItemRepository
from services.cache_service import StockItemCacheService
from events.producers import StockItemEventProducer

router = APIRouter(prefix="/api/v1/stock", tags=["Inventory Management Service"])

_repo = StockItemRepository()
_cache = StockItemCacheService()
_producer = StockItemEventProducer()
_service = StockItemService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> StockItemService:
    return _service

@router.post("", response_model=StockItemDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateStockItemRequest,
    service: StockItemService = Depends(get_service)
) -> StockItemDetailResponse:
    """Create a new StockItem."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=StockItemDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: StockItemService = Depends(get_service)
) -> StockItemDetailResponse:
    """Retrieve StockItem details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=StockItemDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateStockItemRequest,
    service: StockItemService = Depends(get_service)
) -> StockItemDetailResponse:
    """Update StockItem attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=StockItemDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeStockItemStatusRequest,
    service: StockItemService = Depends(get_service)
) -> StockItemDetailResponse:
    """Transition status of StockItem."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=StockItemDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddWarehouseLocationRequest,
    service: StockItemService = Depends(get_service)
) -> StockItemDetailResponse:
    """Attach child item (WarehouseLocation) to StockItem."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=StockItemDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddStockReservationRequest,
    service: StockItemService = Depends(get_service)
) -> StockItemDetailResponse:
    """Attach child item (StockReservation) to StockItem."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=StockItemDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: StockItemService = Depends(get_service)
) -> StockItemDetailResponse:
    """Remove child item (WarehouseLocation) from StockItem."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=StockItemDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: StockItemService = Depends(get_service)
) -> StockItemDetailResponse:
    """Remove child item (StockReservation) from StockItem."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: StockItemService = Depends(get_service)
) -> None:
    """Soft delete StockItem."""
    await service.delete(entity_id)

@router.get("", response_model=StockItemPageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: StockItemService = Depends(get_service)
) -> StockItemPageResponse:
    """Paginated search and filter for StockItem entities."""
    q = QueryStockItemRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchStockItemActionRequest,
    service: StockItemService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
