"""Domain Exceptions for Identity & Authentication Service."""

from shared.exceptions.base import (
    DomainException, EntityNotFoundException, ConflictException,
    BusinessRuleViolationException, ValidationException
)

class UserCredentialNotFoundException(EntityNotFoundException):
    def __init__(self, entity_id: str) -> None:
        super().__init__("UserCredential", entity_id)

class UserCredentialAlreadyExistsException(ConflictException):
    def __init__(self, identifier: str) -> None:
        super().__init__(f"UserCredential with identifier '{identifier}' already exists.")

class InvalidUserCredentialStateTransitionException(BusinessRuleViolationException):
    def __init__(self, current_status: str, target_status: str) -> None:
        super().__init__(
            rule_name="VALID_STATE_TRANSITION",
            reason=f"Transition from '{current_status}' to '{target_status}' is forbidden in Identity & Authentication Service."
        )

class UserCredentialValidationException(ValidationException):
    def __init__(self, field: str, reason: str) -> None:
        super().__init__(f"Validation failed for UserCredential.{field}: {reason}")

class UserCredentialQuotaExceededException(DomainException):
    def __init__(self, quota_name: str, limit: int) -> None:
        super().__init__(f"Quota '{quota_name}' exceeded for UserCredential. Limit is {limit}.", code="QUOTA_EXCEEDED")

class UserCredentialConcurrencyConflictException(ConflictException):
    def __init__(self, entity_id: str, current_version: int) -> None:
        super().__init__(f"Optimistic lock conflict on UserCredential '{entity_id}' at version {current_version}.")

class UserCredentialSecurityViolationException(DomainException):
    def __init__(self, operation: str) -> None:
        super().__init__(f"Security policy violated for operation '{operation}'.", code="SECURITY_VIOLATION", status_code=403)

class UserCredentialDependencyUnavailableException(DomainException):
    def __init__(self, dependency_name: str) -> None:
        super().__init__(f"External dependency '{dependency_name}' is offline or unreachable.", code="DEPENDENCY_ERROR", status_code=503)
