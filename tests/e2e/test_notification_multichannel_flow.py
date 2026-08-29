import pytest
from services.notification_service.services.service import NotificationMessageService
from services.notification_service.repositories.repository import NotificationMessageRepository
from services.notification_service.services.cache_service import NotificationMessageCacheService
from services.notification_service.events.producers import NotificationMessageEventProducer
from services.notification_service.dto.requests import CreateNotificationMessageRequest

@pytest.mark.asyncio
async def test_notification_dispatch_multichannel():
    service = NotificationMessageService(
        NotificationMessageRepository(),
        NotificationMessageCacheService(),
        NotificationMessageEventProducer()
    )

    msg = await service.create(CreateNotificationMessageRequest(
        name="Welcome Email",
        code="NOTIF-WELC-001",
        description="Customer registration welcome email template",
        attributes={"channel": "EMAIL", "recipient": "user@example.com"}
    ))
    assert msg.code == "NOTIF-WELC-001"
