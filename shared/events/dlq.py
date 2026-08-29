import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class DeadLetterMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    original_event_id: str
    event_type: str
    payload: Dict[str, Any]
    error_reason: str
    stack_trace: Optional[str] = None
    retry_attempts: int = 0
    received_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    resolved_at: Optional[datetime] = None
    status: str = "DEAD_LETTER"  # DEAD_LETTER, REPLAYED, DISCARDED

class DeadLetterQueue:
    def __init__(self) -> None:
        self._messages: Dict[str, DeadLetterMessage] = {}

    async def push(self, message: DeadLetterMessage) -> None:
        self._messages[message.id] = message

    async def list_pending(self) -> List[DeadLetterMessage]:
        return [m for m in self._messages.values() if m.status == "DEAD_LETTER"]

    async def mark_replayed(self, message_id: str) -> None:
        if message_id in self._messages:
            self._messages[message_id].status = "REPLAYED"
            self._messages[message_id].resolved_at = datetime.now(timezone.utc)

class PoisonPillHandler:
    """Detects unparseable or malicious payloads and diverts them to DLQ."""

    def __init__(self, dlq: DeadLetterQueue) -> None:
        self.dlq = dlq

    async def handle(self, raw_payload: Dict[str, Any], error: Exception) -> DeadLetterMessage:
        msg = DeadLetterMessage(
            original_event_id=raw_payload.get("id", str(uuid.uuid4())),
            event_type=raw_payload.get("type", "UNKNOWN"),
            payload=raw_payload,
            error_reason=str(error)
        )
        await self.dlq.push(msg)
        return msg
