"""Application Service Orchestrator for Payment & Billing Service."""

import logging
from typing import Any, Dict, List, Optional
from services.payment_service.domain.models import PaymentTransactionAggregate, LedgerEntry, RefundItem
from services.payment_service.domain.exceptions import (
    PaymentTransactionNotFoundException,
    PaymentTransactionAlreadyExistsException
)
from services.payment_service.dto.requests import (
    CreatePaymentTransactionRequest,
    UpdatePaymentTransactionRequest,
    ChangePaymentTransactionStatusRequest,
    AddLedgerEntryRequest,
    AddRefundItemRequest,
    QueryPaymentTransactionRequest,
    BatchPaymentTransactionActionRequest
)
from services.payment_service.dto.responses import (
    PaymentTransactionSummaryResponse,
    PaymentTransactionDetailResponse,
    PaymentTransactionPageResponse,
    BatchActionResultResponse,
    LedgerEntryResponse,
    RefundItemResponse,
    StatusHistoryResponse
)
from services.payment_service.repositories.repository import PaymentTransactionRepository
from services.payment_service.services.cache_service import PaymentTransactionCacheService
from services.payment_service.events.producers import PaymentTransactionEventProducer
from shared.utils.pagination import PageMetadata

logger = logging.getLogger("payment_service.service")

class PaymentTransactionService:
    """Core Application Service managing lifecycle, domain invariants, caching and events."""

    def __init__(
        self,
        repository: PaymentTransactionRepository,
        cache: PaymentTransactionCacheService,
        producer: PaymentTransactionEventProducer
    ) -> None:
        self.repository = repository
        self.cache = cache
        self.producer = producer

    def _to_summary(self, entity: PaymentTransactionAggregate) -> PaymentTransactionSummaryResponse:
        return PaymentTransactionSummaryResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            name=entity.name,
            code=entity.code,
            status=entity.status,
            category=entity.category,
            is_active=entity.is_active,
            version=entity.version,
            sub1_count=len(entity.sub_items_1),
            sub2_count=len(entity.sub_items_2),
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    def _to_detail(self, entity: PaymentTransactionAggregate) -> PaymentTransactionDetailResponse:
        return PaymentTransactionDetailResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            name=entity.name,
            code=entity.code,
            status=entity.status,
            category=entity.category,
            version=entity.version,
            description=entity.description,
            is_active=entity.is_active,
            is_deleted=entity.is_deleted,
            sub_items_1=[LedgerEntryResponse(**item.model_dump()) for item in entity.sub_items_1],
            sub_items_2=[RefundItemResponse(**item.model_dump()) for item in entity.sub_items_2],
            attributes=entity.attributes,
            status_history=[StatusHistoryResponse(**h.model_dump()) for h in entity.status_history],
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    async def create(self, req: CreatePaymentTransactionRequest, actor_id: str = "system") -> PaymentTransactionDetailResponse:
        existing = await self.repository.get_by_code(req.code)
        if existing:
            raise PaymentTransactionAlreadyExistsException(req.code)

        entity = PaymentTransactionAggregate(
            name=req.name,
            code=req.code,
            description=req.description,
            category=req.category,
            attributes=req.attributes
        )
        entity.validate_invariants()

        await self.repository.save(entity)
        await self.cache.set(entity)

        # Dispatch events
        events = entity.pull_events()
        for ev in events:
            await self.producer.publish(ev)

        logger.info(f"Successfully created PaymentTransaction {entity.id} [code={entity.code}]")
        return self._to_detail(entity)

    async def get_by_id(self, entity_id: str) -> PaymentTransactionDetailResponse:
        cached = await self.cache.get(entity_id)
        if cached:
            return PaymentTransactionDetailResponse(**cached)

        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise PaymentTransactionNotFoundException(entity_id)

        await self.cache.set(entity)
        return self._to_detail(entity)

    async def update(self, entity_id: str, req: UpdatePaymentTransactionRequest, actor_id: str = "system") -> PaymentTransactionDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise PaymentTransactionNotFoundException(entity_id)

        entity.update_attributes(name=req.name, description=req.description, attributes=req.attributes, actor_id=actor_id)
        if req.category:
            entity.category = req.category

        entity.validate_invariants()
        await self.repository.save(entity)
        await self.cache.set(entity)

        for ev in entity.pull_events():
            await self.producer.publish(ev)

        logger.info(f"Updated PaymentTransaction {entity.id}")
        return self._to_detail(entity)

    async def change_status(self, entity_id: str, req: ChangePaymentTransactionStatusRequest, actor_id: str = "system") -> PaymentTransactionDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise PaymentTransactionNotFoundException(entity_id)

        entity.transition_status(target_status=req.target_status, actor_id=actor_id, reason=req.reason)

        await self.repository.save(entity)
        await self.cache.set(entity)

        for ev in entity.pull_events():
            await self.producer.publish(ev)

        logger.info(f"Status transition on PaymentTransaction {entity.id} -> {req.target_status}")
        return self._to_detail(entity)

    async def add_sub_item_1(self, entity_id: str, req: AddLedgerEntryRequest, actor_id: str = "system") -> PaymentTransactionDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise PaymentTransactionNotFoundException(entity_id)

        item = LedgerEntry(
            name=req.name,
            code=req.code,
            priority=req.priority,
            config_data=req.config_data
        )
        entity.add_sub_item_1(item, actor_id=actor_id)

        await self.repository.save(entity)
        await self.cache.set(entity)
        for ev in entity.pull_events():
            await self.producer.publish(ev)

        return self._to_detail(entity)

    async def add_sub_item_2(self, entity_id: str, req: AddRefundItemRequest, actor_id: str = "system") -> PaymentTransactionDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise PaymentTransactionNotFoundException(entity_id)

        item = RefundItem(
            label=req.label,
            value_payload=req.value_payload,
            score=req.score,
            tags=req.tags
        )
        entity.add_sub_item_2(item, actor_id=actor_id)

        await self.repository.save(entity)
        await self.cache.set(entity)
        for ev in entity.pull_events():
            await self.producer.publish(ev)

        return self._to_detail(entity)

    async def remove_sub_item_1(self, entity_id: str, sub1_id: str) -> PaymentTransactionDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise PaymentTransactionNotFoundException(entity_id)

        entity.remove_sub_item_1(sub1_id)
        await self.repository.save(entity)
        await self.cache.set(entity)
        return self._to_detail(entity)

    async def remove_sub_item_2(self, entity_id: str, sub2_id: str) -> PaymentTransactionDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise PaymentTransactionNotFoundException(entity_id)

        entity.remove_sub_item_2(sub2_id)
        await self.repository.save(entity)
        await self.cache.set(entity)
        return self._to_detail(entity)

    async def delete(self, entity_id: str, actor_id: str = "system") -> bool:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise PaymentTransactionNotFoundException(entity_id)

        entity.soft_delete(actor_id=actor_id)
        await self.repository.save(entity)
        await self.cache.evict(entity_id)

        for ev in entity.pull_events():
            await self.producer.publish(ev)

        logger.info(f"Soft deleted PaymentTransaction {entity_id}")
        return True

    async def query_page(self, q: QueryPaymentTransactionRequest) -> PaymentTransactionPageResponse:
        skip = (q.page - 1) * q.page_size
        items, total = await self.repository.query(
            search=q.search,
            status=q.status,
            category=q.category,
            tenant_id=q.tenant_id,
            skip=skip,
            limit=q.page_size
        )
        total_pages = max(1, (total + q.page_size - 1) // q.page_size)

        return PaymentTransactionPageResponse(
            items=[self._to_summary(e) for e in items],
            metadata=PageMetadata(
                page=q.page,
                page_size=q.page_size,
                total_items=total,
                total_pages=total_pages,
                has_next=q.page < total_pages,
                has_previous=q.page > 1
            )
        )

    async def batch_action(self, batch_req: BatchPaymentTransactionActionRequest, actor_id: str = "system") -> BatchActionResultResponse:
        success: List[str] = []
        errors: Dict[str, str] = {}

        for eid in batch_req.entity_ids:
            try:
                if batch_req.action == "ACTIVATE":
                    await self.change_status(eid, ChangePaymentTransactionStatusRequest(target_status="ACTIVE", reason=batch_req.reason), actor_id)
                elif batch_req.action == "SUSPEND":
                    await self.change_status(eid, ChangePaymentTransactionStatusRequest(target_status="SUSPENDED", reason=batch_req.reason), actor_id)
                elif batch_req.action == "ARCHIVE":
                    await self.change_status(eid, ChangePaymentTransactionStatusRequest(target_status="ARCHIVED", reason=batch_req.reason), actor_id)
                elif batch_req.action == "DELETE":
                    await self.delete(eid, actor_id)
                else:
                    errors[eid] = f"Unsupported action: {batch_req.action}"
                    continue
                success.append(eid)
            except Exception as ex:
                errors[eid] = str(ex)

        return BatchActionResultResponse(
            success_count=len(success),
            failure_count=len(errors),
            successful_ids=success,
            errors=errors
        )
