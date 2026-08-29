"""Repository Unit Tests for Payment & Billing Service."""

import pytest
from domain.models import PaymentTransactionAggregate
from repositories.repository import PaymentTransactionRepository

@pytest.mark.asyncio
async def test_payment_service_repo_crud_operations():
    repo = PaymentTransactionRepository()
    entity = PaymentTransactionAggregate(name="Repository Record", code="REPO-001")

    # Save
    saved = await repo.save(entity)
    assert saved.id == entity.id

    # Get by ID
    fetched = await repo.get_by_id(entity.id)
    assert fetched is not None
    assert fetched.code == "REPO-001"

    # Get by Code
    by_code = await repo.get_by_code("REPO-001")
    assert by_code is not None

    # Delete
    deleted = await repo.delete(entity.id, actor_id="admin")
    assert deleted is True

    # Confirm soft deleted
    after_delete = await repo.get_by_id(entity.id)
    assert after_delete is None

@pytest.mark.asyncio
async def test_payment_service_repo_query_and_pagination():
    repo = PaymentTransactionRepository()
    for i in range(25):
        await repo.save(PaymentTransactionAggregate(
            name=f"Bulk Item {i}",
            code=f"BULK-{i:03d}",
            status="ACTIVE" if i % 2 == 0 else "DRAFT",
            category="SPECIAL" if i % 5 == 0 else "STANDARD"
        ))

    items, total = await repo.query(status="ACTIVE", skip=0, limit=10)
    assert len(items) == 10
    assert total == 13

    counts = await repo.count_by_status()
    assert counts.get("ACTIVE") == 13
    assert counts.get("DRAFT") == 12
