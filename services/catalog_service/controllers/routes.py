"""REST API Controller Endpoints for Product Catalog Service."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from domain.exceptions import ProductItemNotFoundException, ProductItemAlreadyExistsException
from dto.requests import (
    CreateProductItemRequest,
    UpdateProductItemRequest,
    ChangeProductItemStatusRequest,
    AddProductVariantRequest,
    AddProductAttributeRequest,
    QueryProductItemRequest,
    BatchProductItemActionRequest
)
from dto.responses import (
    ProductItemSummaryResponse,
    ProductItemDetailResponse,
    ProductItemPageResponse,
    BatchActionResultResponse
)
from services.service import ProductItemService
from repositories.repository import ProductItemRepository
from services.cache_service import ProductItemCacheService
from events.producers import ProductItemEventProducer

router = APIRouter(prefix="/api/v1/products", tags=["Product Catalog Service"])

_repo = ProductItemRepository()
_cache = ProductItemCacheService()
_producer = ProductItemEventProducer()
_service = ProductItemService(repository=_repo, cache=_cache, producer=_producer)

def get_service() -> ProductItemService:
    return _service

@router.post("", response_model=ProductItemDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_entity(
    request: CreateProductItemRequest,
    service: ProductItemService = Depends(get_service)
) -> ProductItemDetailResponse:
    """Create a new ProductItem."""
    return await service.create(request)

@router.get("/{entity_id}", response_model=ProductItemDetailResponse)
async def get_entity_by_id(
    entity_id: str,
    service: ProductItemService = Depends(get_service)
) -> ProductItemDetailResponse:
    """Retrieve ProductItem details by UUID."""
    return await service.get_by_id(entity_id)

@router.put("/{entity_id}", response_model=ProductItemDetailResponse)
async def update_entity(
    entity_id: str,
    request: UpdateProductItemRequest,
    service: ProductItemService = Depends(get_service)
) -> ProductItemDetailResponse:
    """Update ProductItem attributes."""
    return await service.update(entity_id, request)

@router.patch("/{entity_id}/status", response_model=ProductItemDetailResponse)
async def change_status(
    entity_id: str,
    request: ChangeProductItemStatusRequest,
    service: ProductItemService = Depends(get_service)
) -> ProductItemDetailResponse:
    """Transition status of ProductItem."""
    return await service.change_status(entity_id, request)

@router.post("/{entity_id}/sub1", response_model=ProductItemDetailResponse)
async def add_sub_item_1(
    entity_id: str,
    request: AddProductVariantRequest,
    service: ProductItemService = Depends(get_service)
) -> ProductItemDetailResponse:
    """Attach child item (ProductVariant) to ProductItem."""
    return await service.add_sub_item_1(entity_id, request)

@router.post("/{entity_id}/sub2", response_model=ProductItemDetailResponse)
async def add_sub_item_2(
    entity_id: str,
    request: AddProductAttributeRequest,
    service: ProductItemService = Depends(get_service)
) -> ProductItemDetailResponse:
    """Attach child item (ProductAttribute) to ProductItem."""
    return await service.add_sub_item_2(entity_id, request)

@router.delete("/{entity_id}/sub1/{sub1_id}", response_model=ProductItemDetailResponse)
async def remove_sub_item_1(
    entity_id: str,
    sub1_id: str,
    service: ProductItemService = Depends(get_service)
) -> ProductItemDetailResponse:
    """Remove child item (ProductVariant) from ProductItem."""
    return await service.remove_sub_item_1(entity_id, sub1_id)

@router.delete("/{entity_id}/sub2/{sub2_id}", response_model=ProductItemDetailResponse)
async def remove_sub_item_2(
    entity_id: str,
    sub2_id: str,
    service: ProductItemService = Depends(get_service)
) -> ProductItemDetailResponse:
    """Remove child item (ProductAttribute) from ProductItem."""
    return await service.remove_sub_item_2(entity_id, sub2_id)

@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entity(
    entity_id: str,
    service: ProductItemService = Depends(get_service)
) -> None:
    """Soft delete ProductItem."""
    await service.delete(entity_id)

@router.get("", response_model=ProductItemPageResponse)
async def list_entities(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    service: ProductItemService = Depends(get_service)
) -> ProductItemPageResponse:
    """Paginated search and filter for ProductItem entities."""
    q = QueryProductItemRequest(search=search, status=status, category=category, page=page, page_size=page_size)
    return await service.query_page(q)

@router.post("/batch", response_model=BatchActionResultResponse)
async def batch_operation(
    request: BatchProductItemActionRequest,
    service: ProductItemService = Depends(get_service)
) -> BatchActionResultResponse:
    """Perform batch operations across multiple entities."""
    return await service.batch_action(request)
