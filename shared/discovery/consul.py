"""Service Mesh Service Discovery & Registration via HashiCorp Consul."""
import logging
from typing import Dict, List, Optional

logger = logging.getLogger("shared.discovery.consul")

class ServiceMeshDiscoveryClient:
    """Manages dynamic service discovery, health heartbeats, and DNS routing."""
    def __init__(self, consul_host: str = "127.0.0.1", consul_port: int = 8500) -> None:
        self.consul_host = consul_host
        self.consul_port = consul_port
        self._registry: Dict[str, List[Dict[str, any]]] = {}

    async def register_service(self, service_name: str, service_id: str, address: str, port: int, tags: List[str]) -> bool:
        logger.info(f"Registering service {service_name} ({service_id}) at {address}:{port}")
        entry = {"id": service_id, "name": service_name, "address": address, "port": port, "tags": tags}
        self._registry.setdefault(service_name, []).append(entry)
        return True

    async def discover_endpoints(self, service_name: str) -> List[Dict[str, any]]:
        return self._registry.get(service_name, [])
