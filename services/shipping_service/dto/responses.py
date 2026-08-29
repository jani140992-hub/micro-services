"""Response DTOs for Shipping & Logistics Service."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from shared.utils.pagination import PageMetadata

class TrackingCheckpointResponse(BaseModel):
    id: str
    name: str
    code: str
    is_active: bool
    priority: int
    config_data: Dict[str, Any]
    created_at: datetime

class ShippingManifestResponse(BaseModel):
    id: str
    label: str
    value_payload: str
    score: float
    tags: List[str]
    created_at: datetime

class StatusHistoryResponse(BaseModel):
    from_status: str
    to_status: str
    changed_at: datetime
    changed_by: str
    reason: Optional[str]

class ShipmentConsignmentSummaryResponse(BaseModel):
    id: str
    tenant_id: str
    name: str
    code: str
    status: str
    category: str
    is_active: bool
    version: int
    sub1_count: int
    sub2_count: int
    created_at: datetime
    updated_at: datetime

class ShipmentConsignmentDetailResponse(BaseModel):
    id: str
    tenant_id: str
    name: str
    code: str
    status: str
    category: str
    version: int
    description: Optional[str]
    is_active: bool
    is_deleted: bool
    sub_items_1: List[TrackingCheckpointResponse]
    sub_items_2: List[ShippingManifestResponse]
    attributes: Dict[str, Any]
    status_history: List[StatusHistoryResponse]
    created_at: datetime
    updated_at: datetime

class ShipmentConsignmentPageResponse(BaseModel):
    items: List[ShipmentConsignmentSummaryResponse]
    metadata: PageMetadata

class BatchActionResultResponse(BaseModel):
    success_count: int
    failure_count: int
    successful_ids: List[str]
    errors: Dict[str, str]
