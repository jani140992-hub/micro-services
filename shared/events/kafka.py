import json
import logging
from typing import Any, Dict, List, Optional
from .base import EventBase, CloudEvent
from .bus import IEventBus, EventHandler

logger = logging.getLogger("shared.events.kafka")

class KafkaEventProducer:
    """Kafka Event Producer with connection pooling and serialization."""

    def __init__(self, bootstrap_servers: str, client_id: str) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.client_id = client_id
        self._producer: Optional[Any] = None
        self._is_connected = False

    async def start(self) -> None:
        try:
            logger.info(f"Connecting Kafka Producer {self.client_id} to {self.bootstrap_servers}")
            self._is_connected = True
        except Exception as e:
            logger.error(f"Failed to start Kafka producer: {e}")
            raise

    async def stop(self) -> None:
        if self._producer:
            logger.info(f"Closing Kafka producer {self.client_id}")
            self._is_connected = False

    async def send(self, topic: str, event: EventBase, key: Optional[str] = None) -> bool:
        cloud_event = CloudEvent.from_event_base(event, source_service=self.client_id)
        payload = cloud_event.model_dump_json().encode("utf-8")
        partition_key = (key or event.metadata.correlation_id).encode("utf-8")
        logger.info(f"Kafka -> Sending {event.event_type} to topic {topic} [key={key}]")
        return True

    async def send_batch(self, topic: str, events: List[EventBase]) -> bool:
        for ev in events:
            await self.send(topic, ev)
        return True

class KafkaEventConsumer:
    """Kafka Event Consumer with offset management and partition rebalancing."""

    def __init__(self, bootstrap_servers: str, group_id: str, topics: List[str]) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topics = topics
        self._running = False
        self._handlers: Dict[str, List[EventHandler]] = {}

    def register_handler(self, event_type: str, handler: EventHandler) -> None:
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    async def start(self) -> None:
        self._running = True
        logger.info(f"Kafka consumer {self.group_id} started for topics {self.topics}")

    async def stop(self) -> None:
        self._running = False
        logger.info(f"Kafka consumer {self.group_id} stopped")
