"""gRPC Standard v1 Health Checking Protocol Provider."""
import logging
from enum import Enum
from typing import Dict

logger = logging.getLogger("shared.grpc.health")

class HealthServingStatus(Enum):
    UNKNOWN = 0
    SERVING = 1
    NOT_SERVING = 2
    SERVICE_UNKNOWN = 3

class GRPCHealthCheckingService:
    """Standard gRPC health provider conforming to grpc.health.v1."""
    def __init__(self) -> None:
        self._statuses: Dict[str, HealthServingStatus] = {"": HealthServingStatus.SERVING}

    def set_status(self, service_name: str, status: HealthServingStatus) -> None:
        logger.info(f"Setting gRPC health status for '{service_name}' to {status.name}")
        self._statuses[service_name] = status

    def check_health(self, service_name: str) -> HealthServingStatus:
        return self._statuses.get(service_name, HealthServingStatus.SERVICE_UNKNOWN)
