import pytest
from shared.events.bus import InMemoryEventBus
from shared.utils.identifiers import generate_order_number
from services.order_service.services.service import CustomerOrderService
from services.order_service.repositories.repository import CustomerOrderRepository
from services.order_service.services.cache_service import CustomerOrderCacheService
from services.order_service.events.producers import CustomerOrderEventProducer
from services.order_service.dto.requests import CreateCustomerOrderRequest, ChangeCustomerOrderStatusRequest
from services.inventory_service.services.service import StockItemService
from services.inventory_service.repositories.repository import StockItemRepository
from services.inventory_service.services.cache_service import StockItemCacheService
from services.inventory_service.events.producers import StockItemEventProducer
from services.inventory_service.dto.requests import CreateStockItemRequest
from services.payment_service.services.service import PaymentTransactionService
from services.payment_service.repositories.repository import PaymentTransactionRepository
from services.payment_service.services.cache_service import PaymentTransactionCacheService
from services.payment_service.events.producers import PaymentTransactionEventProducer
from services.payment_service.dto.requests import CreatePaymentTransactionRequest

@pytest.mark.asyncio
async def test_complete_distributed_checkout_saga():
    bus = InMemoryEventBus()

    # 1. Initialize services
    inv_service = StockItemService(StockItemRepository(), StockItemCacheService(), StockItemEventProducer(bus))
    order_service = CustomerOrderService(CustomerOrderRepository(), CustomerOrderCacheService(), CustomerOrderEventProducer(bus))
    pay_service = PaymentTransactionService(PaymentTransactionRepository(), PaymentTransactionCacheService(), PaymentTransactionEventProducer(bus))

    # 2. Setup inventory stock
    stock = await inv_service.create(CreateStockItemRequest(
        name="MacBook Pro 16",
        code="SKU-MBP-16",
        description="High performance laptop",
        attributes={"quantity": 100, "price": 2499.00}
    ))
    assert stock.code == "SKU-MBP-16"

    # 3. Customer initiates order
    order_code = generate_order_number()
    order = await order_service.create(CreateCustomerOrderRequest(
        name="MacBook Order",
        code=order_code,
        description="Order for MacBook Pro 16",
        attributes={"sku": "SKU-MBP-16", "quantity": 1, "unit_price": 2499.00}
    ))
    assert order.code == order_code
    assert order.status == "DRAFT"

    # 4. Saga transitions order to ACTIVE
    activated = await order_service.change_status(order.id, ChangeCustomerOrderStatusRequest(
        target_status="ACTIVE",
        reason="Inventory reservation verified"
    ))
    assert activated.status == "ACTIVE"

    # 5. Process Payment Transaction
    payment = await pay_service.create(CreatePaymentTransactionRequest(
        name=f"Payment for {order_code}",
        code=f"PAY-{order_code}",
        description="Credit Card Charge",
        attributes={"order_id": order.id, "amount": 2499.00, "currency": "USD"}
    ))
    assert payment.code == f"PAY-{order_code}"

    # 6. Finalize order
    completed = await order_service.change_status(order.id, ChangeCustomerOrderStatusRequest(
        target_status="COMPLETED",
        reason="Payment captured successfully"
    ))
    assert completed.status == "COMPLETED"
