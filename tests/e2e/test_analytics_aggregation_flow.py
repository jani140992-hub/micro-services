import pytest
from services.analytics_service.services.service import StreamMetricRecordService
from services.analytics_service.repositories.repository import StreamMetricRecordRepository
from services.analytics_service.services.cache_service import StreamMetricRecordCacheService
from services.analytics_service.events.producers import StreamMetricRecordEventProducer
from services.analytics_service.dto.requests import CreateStreamMetricRecordRequest

@pytest.mark.asyncio
async def test_analytics_stream_record_ingestion():
    service = StreamMetricRecordService(
        StreamMetricRecordRepository(),
        StreamMetricRecordCacheService(),
        StreamMetricRecordEventProducer()
    )

    metric = await service.create(CreateStreamMetricRecordRequest(
        name="Hourly Revenue Metric",
        code="METRIC-REV-2026-H1",
        description="Aggregated order revenue hourly summary",
        attributes={"total_orders": 450, "gross_revenue": 112500.00}
    ))
    assert metric.code == "METRIC-REV-2026-H1"
