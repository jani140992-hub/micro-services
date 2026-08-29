import pytest
from shared.events.dlq import DeadLetterQueue, PoisonPillHandler

@pytest.mark.asyncio
async def test_poison_pill_diverted_to_dlq():
    dlq = DeadLetterQueue()
    handler = PoisonPillHandler(dlq)

    corrupted_data = {"id": "bad-id", "type": "MALFORMED_EVENT", "corrupt": True}
    msg = await handler.handle(corrupted_data, ValueError("Malformed JSON payload"))

    assert msg.status == "DEAD_LETTER"
    assert msg.event_type == "MALFORMED_EVENT"

    pending = await dlq.list_pending()
    assert len(pending) == 1

    await dlq.mark_replayed(msg.id)
    assert msg.status == "REPLAYED"
