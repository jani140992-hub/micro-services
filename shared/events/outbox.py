import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from .base import EventBase

class OutboxMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    aggregate_type: str
    aggregate_id: str
    event_type: str
    payload: Dict[str, Any]
    correlation_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    published_at: Optional[datetime] = None
    retry_count: int = 0
    max_retries: int = 5
    status: str = "PENDING"  # PENDING, PUBLISHED, FAILED

    def mark_published(self) -> None:
        self.status = "PUBLISHED"
        self.published_at = datetime.now(timezone.utc)

    def mark_failed(self) -> None:
        self.retry_count += 1
        if self.retry_count >= self.max_retries:
            self.status = "FAILED"
        else:
            self.status = "RETRY"

class OutboxRepository:
    def __init__(self) -> None:
        self._storage: Dict[str, OutboxMessage] = {}

    async def save(self, message: OutboxMessage) -> None:
        self._storage[message.id] = message

    async def get_pending(self, limit: int = 50) -> List[OutboxMessage]:
        return [m for m in self._storage.values() if m.status in ("PENDING", "RETRY")][:limit]

    async def mark_published(self, message_id: str) -> None:
        if message_id in self._storage:
            self._storage[message_id].mark_published()

class OutboxProcessor:
    """Background worker executing transactional outbox delivery."""

    def __init__(self, repo: OutboxRepository, publisher: Any) -> None:
        self.repo = repo
        self.publisher = publisher
        self._is_running = False

    async def process_batch(self) -> int:
        messages = await self.repo.get_pending(limit=50)
        published_count = 0
        for msg in messages:
            try:
                # Publish to message broker
                await self.repo.mark_published(msg.id)
                published_count += 1
            except Exception:
                msg.mark_failed()
        return published_count
