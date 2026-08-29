import math
from typing import Generic, List, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")

class PageRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size

class PageMetadata(BaseModel):
    page: int
    page_size: int
    total_items: int
    total_pages: int
    has_next: bool
    has_previous: bool

class Page(BaseModel, Generic[T]):
    items: List[T]
    metadata: PageMetadata

def paginate_list(items: List[T], page_req: PageRequest) -> Page[T]:
    total_items = len(items)
    total_pages = max(1, math.ceil(total_items / page_req.page_size))
    offset = page_req.offset
    paginated_items = items[offset : offset + page_req.page_size]

    return Page(
        items=paginated_items,
        metadata=PageMetadata(
            page=page_req.page,
            page_size=page_req.page_size,
            total_items=total_items,
            total_pages=total_pages,
            has_next=page_req.page < total_pages,
            has_previous=page_req.page > 1
        )
    )
