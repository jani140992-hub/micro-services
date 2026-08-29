"""REST API Controller Endpoints for User Profile Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from domain.exceptions import UserProfileNotFoundException, UserProfileAlreadyExistsException
from dto.requests import (
    CreateUserProfileRequest,
    UpdateUserProfileRequest,
    ChangeUserProfileStatusRequest,
    AddCustomerAddressRequest,
    AddUserPreferenceRequest,
    QueryUserProfileRequest,
    BatchUserProfileActionRequest
)
from dto.responses import (
    UserProfileSummaryResponse,
    UserProfileDetailResponse,
    UserProfilePageResponse,
    BatchActionResultResponse
)
from services.service import UserProfileService
from repositories.repository import UserProfileRepository
from services.cache_service import UserProfileCacheService
from events.producers import UserProfileEventProducer

router = APIRouter(prefix="/api/v1/profiles", tags=["User Profile Service"])

_repo = UserProfileRepository()
_cache = UserProfileCacheService()
_producer = UserProfileEventProducer()
_service = UserProfileService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> UserProfileService:
    return _service

@router.post("", response_model=UserProfileDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateUserProfileRequest,
    service: UserProfileService = Depends(get_service)
) -> UserProfileDetailResponse:
    """Create a new UserProfile."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=UserProfileDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: UserProfileService = Depends(get_service)
) -> UserProfileDetailResponse:
    """Retrieve UserProfile details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=UserProfileDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateUserProfileRequest,
    service: UserProfileService = Depends(get_service)
) -> UserProfileDetailResponse:
    """Update UserProfile attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=UserProfileDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeUserProfileStatusRequest,
    service: UserProfileService = Depends(get_service)
) -> UserProfileDetailResponse:
    """Transition status of UserProfile."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=UserProfileDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddCustomerAddressRequest,
    service: UserProfileService = Depends(get_service)
) -> UserProfileDetailResponse:
    """Attach child item (CustomerAddress) to UserProfile."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=UserProfileDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddUserPreferenceRequest,
    service: UserProfileService = Depends(get_service)
) -> UserProfileDetailResponse:
    """Attach child item (UserPreference) to UserProfile."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=UserProfileDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: UserProfileService = Depends(get_service)
) -> UserProfileDetailResponse:
    """Remove child item (CustomerAddress) from UserProfile."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=UserProfileDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: UserProfileService = Depends(get_service)
) -> UserProfileDetailResponse:
    """Remove child item (UserPreference) from UserProfile."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: UserProfileService = Depends(get_service)
) -> None:
    """Soft delete UserProfile."""
    await service.delete(entity_id)

@router.get("", response_model=UserProfilePageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: UserProfileService = Depends(get_service)
) -> UserProfilePageResponse:
    """Paginated search and filter for UserProfile entities."""
    q = QueryUserProfileRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchUserProfileActionRequest,
    service: UserProfileService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
