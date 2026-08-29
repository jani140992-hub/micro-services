"""REST API Controller Endpoints for Identity & Authentication Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from services.identity_service.domain.exceptions import UserCredentialNotFoundException, UserCredentialAlreadyExistsException
from services.identity_service.dto.requests import (
    CreateUserCredentialRequest,
    UpdateUserCredentialRequest,
    ChangeUserCredentialStatusRequest,
    AddUserSessionRequest,
    AddRoleAssignmentRequest,
    QueryUserCredentialRequest,
    BatchUserCredentialActionRequest
)
from services.identity_service.dto.responses import (
    UserCredentialSummaryResponse,
    UserCredentialDetailResponse,
    UserCredentialPageResponse,
    BatchActionResultResponse
)
from services.identity_service.services.service import UserCredentialService
from services.identity_service.repositories.repository import UserCredentialRepository
from services.identity_service.services.cache_service import UserCredentialCacheService
from services.identity_service.events.producers import UserCredentialEventProducer

router = APIRouter(prefix="/api/v1/auth", tags=["Identity & Authentication Service"])

_repo = UserCredentialRepository()
_cache = UserCredentialCacheService()
_producer = UserCredentialEventProducer()
_service = UserCredentialService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> UserCredentialService:
    return _service

@router.post("", response_model=UserCredentialDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateUserCredentialRequest,
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialDetailResponse:
    """Create a new UserCredential."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=UserCredentialDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialDetailResponse:
    """Retrieve UserCredential details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=UserCredentialDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateUserCredentialRequest,
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialDetailResponse:
    """Update UserCredential attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=UserCredentialDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeUserCredentialStatusRequest,
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialDetailResponse:
    """Transition status of UserCredential."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=UserCredentialDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddUserSessionRequest,
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialDetailResponse:
    """Attach child item (UserSession) to UserCredential."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=UserCredentialDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddRoleAssignmentRequest,
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialDetailResponse:
    """Attach child item (RoleAssignment) to UserCredential."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=UserCredentialDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialDetailResponse:
    """Remove child item (UserSession) from UserCredential."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=UserCredentialDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialDetailResponse:
    """Remove child item (RoleAssignment) from UserCredential."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: UserCredentialService = Depends(get_service)
) -> None:
    """Soft delete UserCredential."""
    await service.delete(entity_id)

@router.get("", response_model=UserCredentialPageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: UserCredentialService = Depends(get_service)
) -> UserCredentialPageResponse:
    """Paginated search and filter for UserCredential entities."""
    q = QueryUserCredentialRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchUserCredentialActionRequest,
    service: UserCredentialService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
