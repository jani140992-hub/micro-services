class AppException(Exception):
    """Base exception for all application errors."""
    def __init__(self, message: str, code: str = "INTERNAL_ERROR", status_code: int = 500) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code

class DomainException(AppException):
    def __init__(self, message: str, code: str = "DOMAIN_ERROR") -> None:
        super().__init__(message, code=code, status_code=400)

class EntityNotFoundException(AppException):
    def __init__(self, entity_name: str, entity_id: str) -> None:
        super().__init__(f"{entity_name} with ID '{entity_id}' was not found.", code="NOT_FOUND", status_code=404)
        self.entity_name = entity_name
        self.entity_id = entity_id

class ConflictException(AppException):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="CONFLICT", status_code=409)

class ValidationException(AppException):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="VALIDATION_FAILED", status_code=422)

class UnauthorizedException(AppException):
    def __init__(self, message: str = "Authentication credentials required.") -> None:
        super().__init__(message, code="UNAUTHORIZED", status_code=401)

class ForbiddenException(AppException):
    def __init__(self, message: str = "Insufficient permissions to perform this operation.") -> None:
        super().__init__(message, code="FORBIDDEN", status_code=403)

class BusinessRuleViolationException(DomainException):
    def __init__(self, rule_name: str, reason: str) -> None:
        super().__init__(f"Business rule '{rule_name}' violated: {reason}", code="BUSINESS_RULE_VIOLATION")
