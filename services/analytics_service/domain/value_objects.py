"""Value Objects for Analytics & BI Service."""

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, ConfigDict

class Money(BaseModel):
    model_config = ConfigDict(frozen=True)
    amount: float = Field(default=0.0, ge=0.0)
    currency: str = Field(default="USD", min_length=3, max_length=3)

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError(f"Currency mismatch: {self.currency} vs {other.currency}")
        return Money(amount=round(self.amount + other.amount, 2), currency=self.currency)

    def multiply(self, factor: float) -> "Money":
        if factor < 0:
            raise ValueError("Multiplier must be non-negative")
        return Money(amount=round(self.amount * factor, 2), currency=self.currency)

class PostalAddress(BaseModel):
    model_config = ConfigDict(frozen=True)
    street_line_1: str = Field(..., min_length=2, max_length=150)
    street_line_2: Optional[str] = Field(None, max_length=150)
    city: str = Field(..., min_length=2, max_length=80)
    state_province: str = Field(..., min_length=2, max_length=80)
    postal_code: str = Field(..., min_length=3, max_length=20)
    country_code: str = Field(default="US", min_length=2, max_length=3)

class Dimensions(BaseModel):
    model_config = ConfigDict(frozen=True)
    length: float = Field(default=10.0, gt=0.0)
    width: float = Field(default=10.0, gt=0.0)
    height: float = Field(default=10.0, gt=0.0)
    unit: str = "cm"

    @property
    def volume(self) -> float:
        return self.length * self.width * self.height

class Weight(BaseModel):
    model_config = ConfigDict(frozen=True)
    value: float = Field(default=1.0, gt=0.0)
    unit: str = "kg"

class StatusHistoryEntry(BaseModel):
    model_config = ConfigDict(frozen=True)
    from_status: str
    to_status: str
    changed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    changed_by: str
    reason: Optional[str] = None
