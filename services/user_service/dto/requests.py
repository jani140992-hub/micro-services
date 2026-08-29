"""Request DTOs for User Profile Service."""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_validator

class CreateUserProfileRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=150, description="Primary descriptive name")
    code: str = Field(..., min_length=2, max_length=50, description="System-wide unique code")
    description: Optional[str] = Field(None, max_length=2000, description="Long-form description")
    category: str = Field(default="STANDARD", max_length=50)
    attributes: Dict[str, Any] = Field(default_factory=dict)
    initial_tags: List[str] = Field(default_factory=list)

    @field_validator("code")
    @classmethod
    def normalize_code(cls, v: str) -> str:
        code = v.strip().upper()
        if not all(c.isalnum() or c in "-_" for c in code):
            raise ValueError("Code must contain only alphanumeric characters, dashes, or underscores")
        return code

class UpdateUserProfileRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=150)
    description: Optional[str] = Field(None, max_length=2000)
    category: Optional[str] = Field(None, max_length=50)
    attributes: Optional[Dict[str, Any]] = None

class ChangeUserProfileStatusRequest(BaseModel):
    target_status: str = Field(..., min_length=2, max_length=30)
    reason: Optional[str] = Field(None, max_length=500)

class AddCustomerAddressRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    code: str = Field(..., min_length=2, max_length=50)
    priority: int = Field(default=10, ge=1, le=100)
    config_data: Dict[str, Any] = Field(default_factory=dict)

class AddUserPreferenceRequest(BaseModel):
    label: str = Field(..., min_length=2, max_length=100)
    value_payload: str = Field(..., min_length=1, max_length=1000)
    score: float = Field(default=1.0, ge=0.0)
    tags: List[str] = Field(default_factory=list)

class QueryUserProfileRequest(BaseModel):
    search: Optional[str] = Field(None, max_length=100)
    status: Optional[str] = Field(None, max_length=30)
    category: Optional[str] = Field(None, max_length=50)
    tenant_id: Optional[str] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    sort_by: str = Field(default="created_at")
    sort_desc: bool = Field(default=True)

class BatchUserProfileActionRequest(BaseModel):
    entity_ids: List[str] = Field(..., min_length=1, max_length=100)
    action: str = Field(..., description="Action: ACTIVATE, SUSPEND, ARCHIVE, DELETE")
    reason: Optional[str] = None
