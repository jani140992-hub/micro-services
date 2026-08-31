"""CloudEvents v1.0 JSON Schema Validator and Semantic Version Compatibility."""
import json
import logging
from typing import Any, Dict, Tuple

logger = logging.getLogger("shared.events.validator")

class CloudEventsSchemaValidator:
    """Validates outbound event envelopes against CloudEvents specification."""
    REQUIRED_FIELDS = ["id", "source", "specversion", "type", "data"]

    @classmethod
    def validate_envelope(cls, event_dict: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        for field in cls.REQUIRED_FIELDS:
            if field not in event_dict:
                return False, f"Missing required CloudEvents field: {field}"
        if event_dict.get("specversion") != "1.0":
            return False, f"Unsupported specversion: {event_dict.get('specversion')}"
        return True, None
