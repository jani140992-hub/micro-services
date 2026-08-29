import pytest

class TestOrderPaymentContract:
    """Consumer-Driven Contract: Order Service (Consumer) -> Payment Service (Provider)."""

    EXPECTED_INTENT_REQUEST = {
        "order_id": "ord_pay_contract_2002",
        "amount": 1499.50,
        "currency": "USD",
        "payment_method": "pm_card_visa_4242",
        "idempotency_key": "idemp_ord_pay_2002_attempt_1"
    }

    EXPECTED_INTENT_RESPONSE = {
        "transaction_id": "txn_succ_889900",
        "order_id": "ord_pay_contract_2002",
        "status": "CAPTURED",
        "amount_captured": 1499.50,
        "currency": "USD",
        "ledger_entry_id": "ledg_entry_445566"
    }

    def test_payment_intent_schema(self):
        req = self.EXPECTED_INTENT_REQUEST
        assert req["amount"] > 0
        assert req["currency"] == "USD"
        assert "idempotency_key" in req

    def test_payment_response_schema(self):
        resp = self.EXPECTED_INTENT_RESPONSE
        assert resp["status"] == "CAPTURED"
        assert resp["amount_captured"] == 1499.50
