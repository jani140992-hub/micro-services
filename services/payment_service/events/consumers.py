"""Event Consumer for Payment & Billing Service."""

import logging
from typing import Any, Dict, Set
from shared.events.base import EventBase

logger = logging.getLogger("payment_service.events.consumer")

class PaymentTransactionEventConsumer:
    """Subscribes to external domain events and applies idempotent local state updates."""

    def __init__(self) -> None:
        self._processed: Set[str] = set()

    async def consume(self, event: EventBase) -> bool:
        if event.event_id in self._processed:
            logger.debug(f"Duplicate event {event.event_id} ignored by payment_service")
            return True

        logger.info(f"[payment_service] Received event {event.event_type} [correlation_id={event.metadata.correlation_id}]")

        if "order." in event.event_type:
            await self._on_order_event(event)
        elif "payment." in event.event_type:
            await self._on_payment_event(event)
        elif "inventory." in event.event_type:
            await self._on_inventory_event(event)
        else:
            await self._on_generic_event(event)

        self._processed.add(event.event_id)
        return True

    async def _on_order_event(self, event: EventBase) -> None:
        logger.debug(f"Handling order event in payment_service: {event.event_id}")

    async def _on_payment_event(self, event: EventBase) -> None:
        logger.debug(f"Handling payment event in payment_service: {event.event_id}")

    async def _on_inventory_event(self, event: EventBase) -> None:
        logger.debug(f"Handling inventory event in payment_service: {event.event_id}")

    async def _on_generic_event(self, event: EventBase) -> None:
        logger.debug(f"Handling generic event in payment_service: {event.event_id}")
