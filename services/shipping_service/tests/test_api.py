"""API Controller Integration Tests for Shipping & Logistics Service."""

import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_shipping_service_health_probe():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "healthy"
        assert data["service"] == "shipping_service"

@pytest.mark.asyncio
async def test_shipping_service_readiness_probe():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/ready")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ready"

@pytest.mark.asyncio
async def test_shipping_service_full_rest_lifecycle():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Create
        create_payload = {
            "name": "Integration Test Entity",
            "code": "INT-TEST-001",
            "description": "Integration test created entity",
            "category": "TEST_CATEGORY"
        }
        post_resp = await client.post("/api/v1/shipments", json=create_payload)
        assert post_resp.status_code == 201
        created_data = post_resp.json()
        eid = created_data["id"]

        # Fetch
        get_resp = await client.get(f"/api/v1/shipments/{eid}")
        assert get_resp.status_code == 200
        assert get_resp.json()["code"] == "INT-TEST-001"

        # Update
        put_resp = await client.put(f"/api/v1/shipments/{eid}", json={"name": "Renamed Test Entity"})
        assert put_resp.status_code == 200
        assert put_resp.json()["name"] == "Renamed Test Entity"

        # Status Change
        status_resp = await client.patch(f"/api/v1/shipments/{eid}/status", json={"target_status": "ACTIVE", "reason": "Test ready"})
        assert status_resp.status_code == 200
        assert status_resp.json()["status"] == "ACTIVE"

        # Add Sub-item 1
        sub1_resp = await client.post(f"/api/v1/shipments/{eid}/sub1", json={"name": "Child 1", "code": "C1-INT"})
        assert sub1_resp.status_code == 200
        assert len(sub1_resp.json()["sub_items_1"]) == 1

        # Add Sub-item 2
        sub2_resp = await client.post(f"/api/v1/shipments/{eid}/sub2", json={"label": "Child 2", "value_payload": "Payload"})
        assert sub2_resp.status_code == 200
        assert len(sub2_resp.json()["sub_items_2"]) == 1

        # Query List
        list_resp = await client.get(f"/api/v1/shipments?page=1&page_size=10")
        assert list_resp.status_code == 200
        assert "items" in list_resp.json()

        # Delete
        del_resp = await client.delete(f"/api/v1/shipments/{eid}")
        assert del_resp.status_code == 204
