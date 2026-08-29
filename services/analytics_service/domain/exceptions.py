"""Domain Exceptions for Analytics & BI Service."""

from shared.exceptions.base import (
    DomainException, EntityNotFoundException, ConflictException,
    BusinessRuleViolationException, ValidationException
)

class StreamMetricRecordNotFoundException(EntityNotFoundException):
    def __init__(self, entity_id: str) -> None:
        super().__init__("StreamMetricRecord", entity_id)

class StreamMetricRecordAlreadyExistsException(ConflictException):
    def __init__(self, identifier: str) -> None:
        super().__init__(f"StreamMetricRecord with identifier '{identifier}' already exists.")

class InvalidStreamMetricRecordStateTransitionException(BusinessRuleViolationException):
    def __init__(self, current_status: str, target_status: str) -> None:
        super().__init__(
            rule_name="VALID_STATE_TRANSITION",
            reason=f"Transition from '{current_status}' to '{target_status}' is forbidden in Analytics & BI Service."
        )

class StreamMetricRecordValidationException(ValidationException):
    def __init__(self, field: str, reason: str) -> None:
        super().__init__(f"Validation failed for StreamMetricRecord.{field}: {reason}")

class StreamMetricRecordQuotaExceededException(DomainException):
    def __init__(self, quota_name: str, limit: int) -> None:
        super().__init__(f"Quota '{quota_name}' exceeded for StreamMetricRecord. Limit is {limit}.", code="QUOTA_EXCEEDED")

class StreamMetricRecordConcurrencyConflictException(ConflictException):
    def __init__(self, entity_id: str, current_version: int) -> None:
        super().__init__(f"Optimistic lock conflict on StreamMetricRecord '{entity_id}' at version {current_version}.")

class StreamMetricRecordSecurityViolationException(DomainException):
    def __init__(self, operation: str) -> None:
        super().__init__(f"Security policy violated for operation '{operation}'.", code="SECURITY_VIOLATION", status_code=403)

class StreamMetricRecordDependencyUnavailableException(DomainException):
    def __init__(self, dependency_name: str) -> None:
        super().__init__(f"External dependency '{dependency_name}' is offline or unreachable.", code="DEPENDENCY_ERROR", status_code=503)
