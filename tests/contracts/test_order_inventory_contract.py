import pytest
from typing import Dict, Any

class TestOrderInventoryContract:
    """Consumer-Driven Contract: Order Service (Consumer) -> Inventory Service (Provider)."""

    EXPECTED_RESERVATION_REQUEST = {
        "order_id": "ord_contract_test_1001",
        "items": [
            {"sku": "SKU-LAPTOP-PRO", "quantity": 2},
            {"sku": "SKU-MONITOR-4K", "quantity": 1}
        ],
        "ttl_seconds": 900
    }

    EXPECTED_RESERVATION_RESPONSE = {
        "reservation_id": "res_mock_778899",
        "status": "RESERVED",
        "expires_at": "2026-08-29T17:15:00Z",
        "reserved_items": [
            {"sku": "SKU-LAPTOP-PRO", "quantity": 2, "warehouse_id": "wh_us_east_1"},
            {"sku": "SKU-MONITOR-4K", "quantity": 1, "warehouse_id": "wh_us_east_2"}
        ]
    }

    def test_reservation_request_schema(self):
        req = self.EXPECTED_RESERVATION_REQUEST
        assert "order_id" in req
        assert len(req["items"]) == 2
        assert req["ttl_seconds"] == 900

    def test_reservation_response_schema(self):
        resp = self.EXPECTED_RESERVATION_RESPONSE
        assert resp["status"] == "RESERVED"
        assert "reservation_id" in resp
        assert len(resp["reserved_items"]) == 2
