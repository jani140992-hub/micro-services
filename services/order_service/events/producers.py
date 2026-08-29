"""Event Publisher for Order Management Service."""

import logging
from typing import Any, Optional
from shared.events.base import EventBase
from shared.events.bus import InMemoryEventBus

logger = logging.getLogger("order_service.events.producer")

class CustomerOrderEventProducer:
    """Publishes events from Order Management Service to Kafka or In-Memory Bus."""

    def __init__(self, bus: Optional[InMemoryEventBus] = None) -> None:
        self.bus = bus or InMemoryEventBus()

    async def publish(self, event: Any) -> bool:
        if isinstance(event, EventBase):
            logger.info(f"[order_service] Publishing {event.event_type} (id={event.event_id})")
            await self.bus.publish(event)
            return True
        logger.warning(f"Unrecognized event payload: {type(event)}")
        return False
