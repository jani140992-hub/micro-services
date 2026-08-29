"""Response DTOs for Analytics & BI Service."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from shared.utils.pagination import PageMetadata

class TimeSeriesDataPointResponse(BaseModel):
    id: str
    name: str
    code: str
    is_active: bool
    priority: int
    config_data: Dict[str, Any]
    created_at: datetime

class AggregationDimensionResponse(BaseModel):
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

class StreamMetricRecordSummaryResponse(BaseModel):
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

class StreamMetricRecordDetailResponse(BaseModel):
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
    sub_items_1: List[TimeSeriesDataPointResponse]
    sub_items_2: List[AggregationDimensionResponse]
    attributes: Dict[str, Any]
    status_history: List[StatusHistoryResponse]
    created_at: datetime
    updated_at: datetime

class StreamMetricRecordPageResponse(BaseModel):
    items: List[StreamMetricRecordSummaryResponse]
    metadata: PageMetadata

class BatchActionResultResponse(BaseModel):
    success_count: int
    failure_count: int
    successful_ids: List[str]
    errors: Dict[str, str]
