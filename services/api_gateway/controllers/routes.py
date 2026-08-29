"""REST API Controller Endpoints for API Gateway Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from domain.exceptions import GatewayRouteNotFoundException, GatewayRouteAlreadyExistsException
from dto.requests import (
    CreateGatewayRouteRequest,
    UpdateGatewayRouteRequest,
    ChangeGatewayRouteStatusRequest,
    AddRoutePredicateRequest,
    AddRouteFilterRequest,
    QueryGatewayRouteRequest,
    BatchGatewayRouteActionRequest
)
from dto.responses import (
    GatewayRouteSummaryResponse,
    GatewayRouteDetailResponse,
    GatewayRoutePageResponse,
    BatchActionResultResponse
)
from services.service import GatewayRouteService
from repositories.repository import GatewayRouteRepository
from services.cache_service import GatewayRouteCacheService
from events.producers import GatewayRouteEventProducer

router = APIRouter(prefix="/api/v1/routes", tags=["API Gateway Service"])

_repo = GatewayRouteRepository()
_cache = GatewayRouteCacheService()
_producer = GatewayRouteEventProducer()
_service = GatewayRouteService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> GatewayRouteService:
    return _service

@router.post("", response_model=GatewayRouteDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateGatewayRouteRequest,
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRouteDetailResponse:
    """Create a new GatewayRoute."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=GatewayRouteDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRouteDetailResponse:
    """Retrieve GatewayRoute details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=GatewayRouteDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateGatewayRouteRequest,
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRouteDetailResponse:
    """Update GatewayRoute attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=GatewayRouteDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeGatewayRouteStatusRequest,
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRouteDetailResponse:
    """Transition status of GatewayRoute."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=GatewayRouteDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddRoutePredicateRequest,
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRouteDetailResponse:
    """Attach child item (RoutePredicate) to GatewayRoute."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=GatewayRouteDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddRouteFilterRequest,
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRouteDetailResponse:
    """Attach child item (RouteFilter) to GatewayRoute."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=GatewayRouteDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRouteDetailResponse:
    """Remove child item (RoutePredicate) from GatewayRoute."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=GatewayRouteDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRouteDetailResponse:
    """Remove child item (RouteFilter) from GatewayRoute."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: GatewayRouteService = Depends(get_service)
) -> None:
    """Soft delete GatewayRoute."""
    await service.delete(entity_id)

@router.get("", response_model=GatewayRoutePageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: GatewayRouteService = Depends(get_service)
) -> GatewayRoutePageResponse:
    """Paginated search and filter for GatewayRoute entities."""
    q = QueryGatewayRouteRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchGatewayRouteActionRequest,
    service: GatewayRouteService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
