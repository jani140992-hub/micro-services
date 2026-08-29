"""Search Query Criteria and Filter DTOs for Identity & Authentication Service."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class UserCredentialSortOption(BaseModel):
    sort_field: str = Field(default="created_at")
    is_descending: bool = Field(default=True)

class UserCredentialTimeWindowFilter(BaseModel):
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    is_inclusive: bool = True

class UserCredentialSearchQuery(BaseModel):
    """Comprehensive multi-parameter query for UserCredential."""
    search_query: Optional[str] = Field(None, max_length=150)
    status_in: List[str] = Field(default_factory=list)
    category_in: List[str] = Field(default_factory=list)
    tenant_id: Optional[str] = None
    active_only: Optional[bool] = None
    time_window: Optional[UserCredentialTimeWindowFilter] = None
    sort_options: List[UserCredentialSortOption] = Field(default_factory=list)
    page_number: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    cursor_token: Optional[str] = None

class FilterPredicateSpec01(BaseModel):
    """Predicate schema 01 for dynamic query building."""
    field_name: str = "attr_filter_1"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec02(BaseModel):
    """Predicate schema 02 for dynamic query building."""
    field_name: str = "attr_filter_2"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec03(BaseModel):
    """Predicate schema 03 for dynamic query building."""
    field_name: str = "attr_filter_3"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec04(BaseModel):
    """Predicate schema 04 for dynamic query building."""
    field_name: str = "attr_filter_4"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec05(BaseModel):
    """Predicate schema 05 for dynamic query building."""
    field_name: str = "attr_filter_5"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec06(BaseModel):
    """Predicate schema 06 for dynamic query building."""
    field_name: str = "attr_filter_6"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec07(BaseModel):
    """Predicate schema 07 for dynamic query building."""
    field_name: str = "attr_filter_7"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec08(BaseModel):
    """Predicate schema 08 for dynamic query building."""
    field_name: str = "attr_filter_8"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec09(BaseModel):
    """Predicate schema 09 for dynamic query building."""
    field_name: str = "attr_filter_9"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec10(BaseModel):
    """Predicate schema 10 for dynamic query building."""
    field_name: str = "attr_filter_10"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec11(BaseModel):
    """Predicate schema 11 for dynamic query building."""
    field_name: str = "attr_filter_11"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec12(BaseModel):
    """Predicate schema 12 for dynamic query building."""
    field_name: str = "attr_filter_12"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec13(BaseModel):
    """Predicate schema 13 for dynamic query building."""
    field_name: str = "attr_filter_13"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec14(BaseModel):
    """Predicate schema 14 for dynamic query building."""
    field_name: str = "attr_filter_14"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec15(BaseModel):
    """Predicate schema 15 for dynamic query building."""
    field_name: str = "attr_filter_15"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec16(BaseModel):
    """Predicate schema 16 for dynamic query building."""
    field_name: str = "attr_filter_16"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec17(BaseModel):
    """Predicate schema 17 for dynamic query building."""
    field_name: str = "attr_filter_17"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec18(BaseModel):
    """Predicate schema 18 for dynamic query building."""
    field_name: str = "attr_filter_18"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec19(BaseModel):
    """Predicate schema 19 for dynamic query building."""
    field_name: str = "attr_filter_19"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec20(BaseModel):
    """Predicate schema 20 for dynamic query building."""
    field_name: str = "attr_filter_20"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec21(BaseModel):
    """Predicate schema 21 for dynamic query building."""
    field_name: str = "attr_filter_21"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec22(BaseModel):
    """Predicate schema 22 for dynamic query building."""
    field_name: str = "attr_filter_22"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec23(BaseModel):
    """Predicate schema 23 for dynamic query building."""
    field_name: str = "attr_filter_23"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec24(BaseModel):
    """Predicate schema 24 for dynamic query building."""
    field_name: str = "attr_filter_24"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec25(BaseModel):
    """Predicate schema 25 for dynamic query building."""
    field_name: str = "attr_filter_25"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec26(BaseModel):
    """Predicate schema 26 for dynamic query building."""
    field_name: str = "attr_filter_26"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec27(BaseModel):
    """Predicate schema 27 for dynamic query building."""
    field_name: str = "attr_filter_27"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec28(BaseModel):
    """Predicate schema 28 for dynamic query building."""
    field_name: str = "attr_filter_28"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec29(BaseModel):
    """Predicate schema 29 for dynamic query building."""
    field_name: str = "attr_filter_29"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec30(BaseModel):
    """Predicate schema 30 for dynamic query building."""
    field_name: str = "attr_filter_30"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec31(BaseModel):
    """Predicate schema 31 for dynamic query building."""
    field_name: str = "attr_filter_31"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec32(BaseModel):
    """Predicate schema 32 for dynamic query building."""
    field_name: str = "attr_filter_32"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec33(BaseModel):
    """Predicate schema 33 for dynamic query building."""
    field_name: str = "attr_filter_33"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec34(BaseModel):
    """Predicate schema 34 for dynamic query building."""
    field_name: str = "attr_filter_34"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec35(BaseModel):
    """Predicate schema 35 for dynamic query building."""
    field_name: str = "attr_filter_35"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec36(BaseModel):
    """Predicate schema 36 for dynamic query building."""
    field_name: str = "attr_filter_36"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec37(BaseModel):
    """Predicate schema 37 for dynamic query building."""
    field_name: str = "attr_filter_37"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec38(BaseModel):
    """Predicate schema 38 for dynamic query building."""
    field_name: str = "attr_filter_38"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec39(BaseModel):
    """Predicate schema 39 for dynamic query building."""
    field_name: str = "attr_filter_39"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec40(BaseModel):
    """Predicate schema 40 for dynamic query building."""
    field_name: str = "attr_filter_40"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec41(BaseModel):
    """Predicate schema 41 for dynamic query building."""
    field_name: str = "attr_filter_41"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec42(BaseModel):
    """Predicate schema 42 for dynamic query building."""
    field_name: str = "attr_filter_42"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec43(BaseModel):
    """Predicate schema 43 for dynamic query building."""
    field_name: str = "attr_filter_43"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True

class FilterPredicateSpec44(BaseModel):
    """Predicate schema 44 for dynamic query building."""
    field_name: str = "attr_filter_44"
    comparison_op: str = Field(default="EQ", description="EQ, NEQ, GT, GTE, LT, LTE, IN, CONTAINS")
    expected_value: Optional[str] = None
    case_sensitive: bool = False
    relevance_score: float = Field(default=1.0, ge=0.0)

    def matches_attribute(self, raw_value: Any) -> bool:
        if self.expected_value is None:
            return True
        val_str = str(raw_value).lower() if not self.case_sensitive else str(raw_value)
        exp_str = self.expected_value.lower() if not self.case_sensitive else self.expected_value
        if self.comparison_op == "EQ":
            return val_str == exp_str
        elif self.comparison_op == "CONTAINS":
            return exp_str in val_str
        return True
