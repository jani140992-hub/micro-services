"""Prometheus and OpenMetrics Custom Exporter for Microservices."""
import time
from typing import Dict, List, Optional
import logging

logger = logging.getLogger("shared.metrics.exporter")

class ServiceMetricsCollector:
    """Collects real-time throughput, latency histograms, and error counters."""
    def __init__(self, service_name: str) -> None:
        self.service_name = service_name
        self._counters: Dict[str, float] = {}
        self._gauges: Dict[str, float] = {}

    def increment_counter(self, metric_name: str, value: float = 1.0, labels: Optional[Dict[str, str]] = None) -> None:
        key = f"{metric_name}_{labels}" if labels else metric_name
        self._counters[key] = self._counters.get(key, 0.0) + value

    def set_gauge(self, metric_name: str, value: float) -> None:
        self._gauges[metric_name] = value

    def collect_all(self) -> Dict[str, any]:
        return {
            "service": self.service_name,
            "counters": self._counters,
            "gauges": self._gauges,
            "timestamp": time.time()
        }
