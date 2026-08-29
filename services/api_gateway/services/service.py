"""Application Service Orchestrator for API Gateway Service."""

import logging
from typing import Any, Dict, List, Optional
from domain.models import GatewayRouteAggregate, RoutePredicate, RouteFilter
from domain.exceptions import (
    GatewayRouteNotFoundException,
    GatewayRouteAlreadyExistsException
)
from dto.requests import (
    CreateGatewayRouteRequest,
    UpdateGatewayRouteRequest,
    ChangeGatewayRouteStatusRequest,
    AddRoutePredicateRequest,
    AddRouteFilterRequest,
    QueryGatewayRouteRequest,
    BatchGatewayRouteActionRequest
)
from dto.responses import (
    GatewayRouteSummaryResponse,
    GatewayRouteDetailResponse,
    GatewayRoutePageResponse,
    BatchActionResultResponse,
    RoutePredicateResponse,
    RouteFilterResponse,
    StatusHistoryResponse
)
from repositories.repository import GatewayRouteRepository
from services.cache_service import GatewayRouteCacheService
from events.producers import GatewayRouteEventProducer
from shared.utils.pagination import PageMetadata

logger = logging.getLogger("api_gateway.service")

class GatewayRouteService:
    """Core Application Service managing lifecycle, domain invariants, caching and events."""

    def __init__(
        self,
        repository: GatewayRouteRepository,
        cache: GatewayRouteCacheService,
        producer: GatewayRouteEventProducer
    ) -> None:
        self.repository = repository
        self.cache = cache
        self.producer = producer

    def _to_summary(self, entity: GatewayRouteAggregate) -> GatewayRouteSummaryResponse:
        return GatewayRouteSummaryResponse(
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

    def _to_detail(self, entity: GatewayRouteAggregate) -> GatewayRouteDetailResponse:
        return GatewayRouteDetailResponse(
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
            sub_items_1=[RoutePredicateResponse(**item.model_dump()) for item in entity.sub_items_1],
            sub_items_2=[RouteFilterResponse(**item.model_dump()) for item in entity.sub_items_2],
            attributes=entity.attributes,
            status_history=[StatusHistoryResponse(**h.model_dump()) for h in entity.status_history],
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    async def create(self, req: CreateGatewayRouteRequest, actor_id: str = "system") -> GatewayRouteDetailResponse:
        existing = await self.repository.get_by_code(req.code)
        if existing:
            raise GatewayRouteAlreadyExistsException(req.code)

        entity = GatewayRouteAggregate(
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

        logger.info(f"Successfully created GatewayRoute {entity.id} [code={entity.code}]")
        return self._to_detail(entity)

    async def get_by_id(self, entity_id: str) -> GatewayRouteDetailResponse:
        cached = await self.cache.get(entity_id)
        if cached:
            return GatewayRouteDetailResponse(**cached)

        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)

        await self.cache.set(entity)
        return self._to_detail(entity)

    async def update(self, entity_id: str, req: UpdateGatewayRouteRequest, actor_id: str = "system") -> GatewayRouteDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)

        entity.update_attributes(name=req.name, description=req.description, attributes=req.attributes, actor_id=actor_id)
        if req.category:
            entity.category = req.category

        entity.validate_invariants()
        await self.repository.save(entity)
        await self.cache.set(entity)

        for ev in entity.pull_events():
            await self.producer.publish(ev)

        logger.info(f"Updated GatewayRoute {entity.id}")
        return self._to_detail(entity)

    async def change_status(self, entity_id: str, req: ChangeGatewayRouteStatusRequest, actor_id: str = "system") -> GatewayRouteDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)

        entity.transition_status(target_status=req.target_status, actor_id=actor_id, reason=req.reason)

        await self.repository.save(entity)
        await self.cache.set(entity)

        for ev in entity.pull_events():
            await self.producer.publish(ev)

        logger.info(f"Status transition on GatewayRoute {entity.id} -> {req.target_status}")
        return self._to_detail(entity)

    async def add_sub_item_1(self, entity_id: str, req: AddRoutePredicateRequest, actor_id: str = "system") -> GatewayRouteDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)

        item = RoutePredicate(
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

    async def add_sub_item_2(self, entity_id: str, req: AddRouteFilterRequest, actor_id: str = "system") -> GatewayRouteDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)

        item = RouteFilter(
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

    async def remove_sub_item_1(self, entity_id: str, sub1_id: str) -> GatewayRouteDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)

        entity.remove_sub_item_1(sub1_id)
        await self.repository.save(entity)
        await self.cache.set(entity)
        return self._to_detail(entity)

    async def remove_sub_item_2(self, entity_id: str, sub2_id: str) -> GatewayRouteDetailResponse:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)

        entity.remove_sub_item_2(sub2_id)
        await self.repository.save(entity)
        await self.cache.set(entity)
        return self._to_detail(entity)

    async def delete(self, entity_id: str, actor_id: str = "system") -> bool:
        entity = await self.repository.get_by_id(entity_id)
        if not entity:
            raise GatewayRouteNotFoundException(entity_id)

        entity.soft_delete(actor_id=actor_id)
        await self.repository.save(entity)
        await self.cache.evict(entity_id)

        for ev in entity.pull_events():
            await self.producer.publish(ev)

        logger.info(f"Soft deleted GatewayRoute {entity_id}")
        return True

    async def query_page(self, q: QueryGatewayRouteRequest) -> GatewayRoutePageResponse:
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

        return GatewayRoutePageResponse(
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

    async def batch_action(self, batch_req: BatchGatewayRouteActionRequest, actor_id: str = "system") -> BatchActionResultResponse:
        success: List[str] = []
        errors: Dict[str, str] = {}

        for eid in batch_req.entity_ids:
            try:
                if batch_req.action == "ACTIVATE":
                    await self.change_status(eid, ChangeGatewayRouteStatusRequest(target_status="ACTIVE", reason=batch_req.reason), actor_id)
                elif batch_req.action == "SUSPEND":
                    await self.change_status(eid, ChangeGatewayRouteStatusRequest(target_status="SUSPENDED", reason=batch_req.reason), actor_id)
                elif batch_req.action == "ARCHIVE":
                    await self.change_status(eid, ChangeGatewayRouteStatusRequest(target_status="ARCHIVED", reason=batch_req.reason), actor_id)
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
