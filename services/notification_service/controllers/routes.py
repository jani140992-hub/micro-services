"""REST API Controller Endpoints for Notification & Messaging Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from services.notification_service.domain.exceptions import NotificationMessageNotFoundException, NotificationMessageAlreadyExistsException
from services.notification_service.dto.requests import (
    CreateNotificationMessageRequest,
    UpdateNotificationMessageRequest,
    ChangeNotificationMessageStatusRequest,
    AddDeliveryAttemptRecordRequest,
    AddTemplateVariableRequest,
    QueryNotificationMessageRequest,
    BatchNotificationMessageActionRequest
)
from services.notification_service.dto.responses import (
    NotificationMessageSummaryResponse,
    NotificationMessageDetailResponse,
    NotificationMessagePageResponse,
    BatchActionResultResponse
)
from services.notification_service.services.service import NotificationMessageService
from services.notification_service.repositories.repository import NotificationMessageRepository
from services.notification_service.services.cache_service import NotificationMessageCacheService
from services.notification_service.events.producers import NotificationMessageEventProducer

router = APIRouter(prefix="/api/v1/notifications", tags=["Notification & Messaging Service"])

_repo = NotificationMessageRepository()
_cache = NotificationMessageCacheService()
_producer = NotificationMessageEventProducer()
_service = NotificationMessageService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> NotificationMessageService:
    return _service

@router.post("", response_model=NotificationMessageDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateNotificationMessageRequest,
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessageDetailResponse:
    """Create a new NotificationMessage."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=NotificationMessageDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessageDetailResponse:
    """Retrieve NotificationMessage details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=NotificationMessageDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateNotificationMessageRequest,
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessageDetailResponse:
    """Update NotificationMessage attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=NotificationMessageDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeNotificationMessageStatusRequest,
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessageDetailResponse:
    """Transition status of NotificationMessage."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=NotificationMessageDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddDeliveryAttemptRecordRequest,
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessageDetailResponse:
    """Attach child item (DeliveryAttemptRecord) to NotificationMessage."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=NotificationMessageDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddTemplateVariableRequest,
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessageDetailResponse:
    """Attach child item (TemplateVariable) to NotificationMessage."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=NotificationMessageDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessageDetailResponse:
    """Remove child item (DeliveryAttemptRecord) from NotificationMessage."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=NotificationMessageDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessageDetailResponse:
    """Remove child item (TemplateVariable) from NotificationMessage."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: NotificationMessageService = Depends(get_service)
) -> None:
    """Soft delete NotificationMessage."""
    await service.delete(entity_id)

@router.get("", response_model=NotificationMessagePageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: NotificationMessageService = Depends(get_service)
) -> NotificationMessagePageResponse:
    """Paginated search and filter for NotificationMessage entities."""
    q = QueryNotificationMessageRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchNotificationMessageActionRequest,
    service: NotificationMessageService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
