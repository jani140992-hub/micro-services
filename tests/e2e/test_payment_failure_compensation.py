import pytest
from services.order_service.services.service import CustomerOrderService
from services.order_service.repositories.repository import CustomerOrderRepository
from services.order_service.services.cache_service import CustomerOrderCacheService
from services.order_service.events.producers import CustomerOrderEventProducer
from services.order_service.dto.requests import CreateCustomerOrderRequest, ChangeCustomerOrderStatusRequest

@pytest.mark.asyncio
async def test_payment_declined_compensating_transaction():
    order_service = CustomerOrderService(
        CustomerOrderRepository(),
        CustomerOrderCacheService(),
        CustomerOrderEventProducer()
    )

    # Create initial order
    order = await order_service.create(CreateCustomerOrderRequest(
        name="Compensating Order",
        code="ORD-COMP-001",
        description="Order that will trigger payment failure"
    ))
    assert order.status == "DRAFT"

    # Move to REVIEW
    under_review = await order_service.change_status(order.id, ChangeCustomerOrderStatusRequest(
        target_status="REVIEW",
        reason="Hold stock for payment"
    ))
    assert under_review.status == "REVIEW"

    # Payment Gateway rejects card -> trigger compensation (transition to REJECTED)
    compensated = await order_service.change_status(order.id, ChangeCustomerOrderStatusRequest(
        target_status="REJECTED",
        reason="Card declined: Insufficient funds. Released stock reservation."
    ))
    assert compensated.status == "REJECTED"
