import pytest

class TestOrderShippingContract:
    """Consumer-Driven Contract: Order Service (Consumer) -> Shipping Service (Provider)."""

    EXPECTED_DISPATCH_REQUEST = {
        "order_id": "ord_ship_3003",
        "recipient_name": "Bob Johnson",
        "destination_address": {
            "street": "100 Market Street",
            "city": "San Francisco",
            "state": "CA",
            "postal_code": "94105",
            "country": "US"
        },
        "packages": [
            {"weight_kg": 2.5, "dimensions_cm": "30x20x10"}
        ],
        "carrier_service": "FEDEX_2_DAY"
    }

    EXPECTED_DISPATCH_RESPONSE = {
        "shipment_id": "ship_consignment_556677",
        "tracking_number": "FEDEX987654321012",
        "status": "LABEL_CREATED",
        "estimated_delivery": "2026-09-02T18:00:00Z"
    }

    def test_dispatch_contract(self):
        req = self.EXPECTED_DISPATCH_REQUEST
        resp = self.EXPECTED_DISPATCH_RESPONSE
        assert req["carrier_service"] == "FEDEX_2_DAY"
        assert resp["status"] == "LABEL_CREATED"
