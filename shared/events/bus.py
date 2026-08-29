import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Any, Callable, Coroutine, Dict, List, Type
from .base import EventBase

logger = logging.getLogger("shared.events.bus")

EventHandler = Callable[[EventBase], Coroutine[Any, Any, None]]

class IEventBus(ABC):
    """Event Bus Interface for publishing and subscribing to events."""

    @abstractmethod
    async def publish(self, event: EventBase) -> None:
        pass

    @abstractmethod
    async def publish_batch(self, events: List[EventBase]) -> None:
        pass

    @abstractmethod
    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, event_type: str, handler: EventHandler) -> None:
        pass

class InMemoryEventBus(IEventBus):
    """Asynchronous in-memory event bus useful for tests and single-process pipelines."""

    def __init__(self) -> None:
        self._handlers: Dict[str, List[EventHandler]] = {}
        self._published_events: List[EventBase] = []

    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)
            logger.debug(f"Subscribed handler {handler.__name__} to {event_type}")

    def unsubscribe(self, event_type: str, handler: EventHandler) -> None:
        if event_type in self._handlers and handler in self._handlers[event_type]:
            self._handlers[event_type].remove(handler)

    async def publish(self, event: EventBase) -> None:
        self._published_events.append(event)
        handlers = self._handlers.get(event.event_type, [])
        wildcard_handlers = self._handlers.get("*", [])
        all_handlers = handlers + wildcard_handlers

        if not all_handlers:
            logger.warning(f"No handlers registered for event type '{event.event_type}'")
            return

        tasks = [asyncio.create_task(handler(event)) for handler in all_handlers]
        await asyncio.gather(*tasks, return_exceptions=False)

    async def publish_batch(self, events: List[EventBase]) -> None:
        for event in events:
            await self.publish(event)

    def get_published_events(self) -> List[EventBase]:
        return list(self._published_events)

    def clear(self) -> None:
        self._published_events.clear()
        self._handlers.clear()

class EventDispatcher:
    """Central event dispatcher with routing and error resilience."""

    def __init__(self, bus: IEventBus) -> None:
        self.bus = bus

    async def dispatch(self, event: EventBase) -> None:
        logger.info(f"Dispatching event: {event.event_type} (id: {event.event_id})")
        await self.bus.publish(event)
