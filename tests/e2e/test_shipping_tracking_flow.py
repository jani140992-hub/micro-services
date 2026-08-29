import pytest
from services.shipping_service.services.service import ShipmentConsignmentService
from services.shipping_service.repositories.repository import ShipmentConsignmentRepository
from services.shipping_service.services.cache_service import ShipmentConsignmentCacheService
from services.shipping_service.events.producers import ShipmentConsignmentEventProducer
from services.shipping_service.dto.requests import (
    CreateShipmentConsignmentRequest,
    ChangeShipmentConsignmentStatusRequest,
    AddTrackingCheckpointRequest
)

@pytest.mark.asyncio
async def test_shipping_lifecycle_and_checkpoints():
    service = ShipmentConsignmentService(
        ShipmentConsignmentRepository(),
        ShipmentConsignmentCacheService(),
        ShipmentConsignmentEventProducer()
    )

    consignment = await service.create(CreateShipmentConsignmentRequest(
        name="FedEx Ground Priority",
        code="TRK-FEDEX-998811",
        description="Parcel delivery to customer"
    ))
    assert consignment.status == "DRAFT"

    # Add Checkpoint
    checkpoint_resp = await service.add_sub_item_1(consignment.id, AddTrackingCheckpointRequest(
        name="Origin Scan - Memphis Hub",
        code="SCAN-MEM-01",
        priority=1
    ))
    assert len(checkpoint_resp.sub_items_1) == 1

    # Transition to ACTIVE
    activated = await service.change_status(consignment.id, ChangeShipmentConsignmentStatusRequest(
        target_status="ACTIVE",
        reason="Dispatched from carrier terminal"
    ))
    assert activated.status == "ACTIVE"
