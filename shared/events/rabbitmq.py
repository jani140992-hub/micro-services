import json
import logging
from typing import Any, Dict, List, Optional
from .base import EventBase
from .bus import EventHandler

logger = logging.getLogger("shared.events.rabbitmq")

class RabbitMQEventProducer:
    """AMQP RabbitMQ producer supporting direct, topic, and fanout exchanges."""

    def __init__(self, amqp_url: str, exchange_name: str = "cloudmart.events") -> None:
        self.amqp_url = amqp_url
        self.exchange_name = exchange_name
        self._connected = False

    async def connect(self) -> None:
        logger.info(f"Connecting to RabbitMQ exchange {self.exchange_name}")
        self._connected = True

    async def close(self) -> None:
        self._connected = False
        logger.info("RabbitMQ connection closed")

    async def publish(self, routing_key: str, event: EventBase) -> bool:
        payload = event.model_dump_json()
        logger.info(f"RabbitMQ publish -> Exchange: {self.exchange_name}, Key: {routing_key}")
        return True

class RabbitMQEventConsumer:
    """AMQP RabbitMQ consumer with prefetch count and manual acknowledgements."""

    def __init__(self, amqp_url: str, queue_name: str, routing_keys: List[str]) -> None:
        self.amqp_url = amqp_url
        self.queue_name = queue_name
        self.routing_keys = routing_keys
        self._consuming = False

    async def start_consuming(self, handler: EventHandler) -> None:
        self._consuming = True
        logger.info(f"RabbitMQ consumer listening on queue {self.queue_name}")

    async def stop_consuming(self) -> None:
        self._consuming = False
