"""REST API Controller Endpoints for Shipping & Logistics Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from domain.exceptions import ShipmentConsignmentNotFoundException, ShipmentConsignmentAlreadyExistsException
from dto.requests import (
    CreateShipmentConsignmentRequest,
    UpdateShipmentConsignmentRequest,
    ChangeShipmentConsignmentStatusRequest,
    AddTrackingCheckpointRequest,
    AddShippingManifestRequest,
    QueryShipmentConsignmentRequest,
    BatchShipmentConsignmentActionRequest
)
from dto.responses import (
    ShipmentConsignmentSummaryResponse,
    ShipmentConsignmentDetailResponse,
    ShipmentConsignmentPageResponse,
    BatchActionResultResponse
)
from services.service import ShipmentConsignmentService
from repositories.repository import ShipmentConsignmentRepository
from services.cache_service import ShipmentConsignmentCacheService
from events.producers import ShipmentConsignmentEventProducer

router = APIRouter(prefix="/api/v1/shipments", tags=["Shipping & Logistics Service"])

_repo = ShipmentConsignmentRepository()
_cache = ShipmentConsignmentCacheService()
_producer = ShipmentConsignmentEventProducer()
_service = ShipmentConsignmentService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> ShipmentConsignmentService:
    return _service

@router.post("", response_model=ShipmentConsignmentDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateShipmentConsignmentRequest,
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentDetailResponse:
    """Create a new ShipmentConsignment."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=ShipmentConsignmentDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentDetailResponse:
    """Retrieve ShipmentConsignment details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=ShipmentConsignmentDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateShipmentConsignmentRequest,
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentDetailResponse:
    """Update ShipmentConsignment attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=ShipmentConsignmentDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeShipmentConsignmentStatusRequest,
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentDetailResponse:
    """Transition status of ShipmentConsignment."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=ShipmentConsignmentDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddTrackingCheckpointRequest,
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentDetailResponse:
    """Attach child item (TrackingCheckpoint) to ShipmentConsignment."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=ShipmentConsignmentDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddShippingManifestRequest,
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentDetailResponse:
    """Attach child item (ShippingManifest) to ShipmentConsignment."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=ShipmentConsignmentDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentDetailResponse:
    """Remove child item (TrackingCheckpoint) from ShipmentConsignment."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=ShipmentConsignmentDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentDetailResponse:
    """Remove child item (ShippingManifest) from ShipmentConsignment."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: ShipmentConsignmentService = Depends(get_service)
) -> None:
    """Soft delete ShipmentConsignment."""
    await service.delete(entity_id)

@router.get("", response_model=ShipmentConsignmentPageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: ShipmentConsignmentService = Depends(get_service)
) -> ShipmentConsignmentPageResponse:
    """Paginated search and filter for ShipmentConsignment entities."""
    q = QueryShipmentConsignmentRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchShipmentConsignmentActionRequest,
    service: ShipmentConsignmentService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
