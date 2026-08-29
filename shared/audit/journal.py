"""Enterprise Compliance Audit Journal & Tamper-Evident Hashing."""
import hashlib
import json
import logging
from datetime import datetime, timezone
from typing import Any, Dict, Optional

logger = logging.getLogger("shared.audit.journal")

class AuditJournalManager:
    """Immutable audit trail with cryptographic hash chaining for regulatory compliance."""
    def __init__(self) -> None:
        self._previous_hash = "GENESIS_HASH_0000000000000000"

    def record_audit_entry(self, actor: str, action: str, resource_type: str, resource_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        timestamp = datetime.now(timezone.utc).isoformat()
        entry_data = {"actor": actor, "action": action, "resource_type": resource_type, "resource_id": resource_id, "payload": payload, "timestamp": timestamp, "prev_hash": self._previous_hash}
        serialized = json.dumps(entry_data, sort_keys=True)
        current_hash = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
        entry_data["hash"] = current_hash
        self._previous_hash = current_hash
        logger.info(f"Recorded audit entry {current_hash[:12]} for {actor} on {resource_type}/{resource_id}")
        return entry_data
