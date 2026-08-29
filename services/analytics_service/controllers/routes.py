"""REST API Controller Endpoints for Analytics & BI Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from services.analytics_service.domain.exceptions import StreamMetricRecordNotFoundException, StreamMetricRecordAlreadyExistsException
from services.analytics_service.dto.requests import (
    CreateStreamMetricRecordRequest,
    UpdateStreamMetricRecordRequest,
    ChangeStreamMetricRecordStatusRequest,
    AddTimeSeriesDataPointRequest,
    AddAggregationDimensionRequest,
    QueryStreamMetricRecordRequest,
    BatchStreamMetricRecordActionRequest
)
from services.analytics_service.dto.responses import (
    StreamMetricRecordSummaryResponse,
    StreamMetricRecordDetailResponse,
    StreamMetricRecordPageResponse,
    BatchActionResultResponse
)
from services.analytics_service.services.service import StreamMetricRecordService
from services.analytics_service.repositories.repository import StreamMetricRecordRepository
from services.analytics_service.services.cache_service import StreamMetricRecordCacheService
from services.analytics_service.events.producers import StreamMetricRecordEventProducer

router = APIRouter(prefix="/api/v1/metrics", tags=["Analytics & BI Service"])

_repo = StreamMetricRecordRepository()
_cache = StreamMetricRecordCacheService()
_producer = StreamMetricRecordEventProducer()
_service = StreamMetricRecordService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> StreamMetricRecordService:
    return _service

@router.post("", response_model=StreamMetricRecordDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateStreamMetricRecordRequest,
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordDetailResponse:
    """Create a new StreamMetricRecord."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=StreamMetricRecordDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordDetailResponse:
    """Retrieve StreamMetricRecord details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=StreamMetricRecordDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateStreamMetricRecordRequest,
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordDetailResponse:
    """Update StreamMetricRecord attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=StreamMetricRecordDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeStreamMetricRecordStatusRequest,
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordDetailResponse:
    """Transition status of StreamMetricRecord."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=StreamMetricRecordDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddTimeSeriesDataPointRequest,
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordDetailResponse:
    """Attach child item (TimeSeriesDataPoint) to StreamMetricRecord."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=StreamMetricRecordDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddAggregationDimensionRequest,
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordDetailResponse:
    """Attach child item (AggregationDimension) to StreamMetricRecord."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=StreamMetricRecordDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordDetailResponse:
    """Remove child item (TimeSeriesDataPoint) from StreamMetricRecord."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=StreamMetricRecordDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordDetailResponse:
    """Remove child item (AggregationDimension) from StreamMetricRecord."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: StreamMetricRecordService = Depends(get_service)
) -> None:
    """Soft delete StreamMetricRecord."""
    await service.delete(entity_id)

@router.get("", response_model=StreamMetricRecordPageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: StreamMetricRecordService = Depends(get_service)
) -> StreamMetricRecordPageResponse:
    """Paginated search and filter for StreamMetricRecord entities."""
    q = QueryStreamMetricRecordRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchStreamMetricRecordActionRequest,
    service: StreamMetricRecordService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
