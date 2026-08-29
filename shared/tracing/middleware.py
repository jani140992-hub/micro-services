import uuid
import time
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from .context import TraceContext

class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """Ensures every inbound request has a valid X-Correlation-ID header."""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        cid = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
        TraceContext.set_correlation_id(cid)

        trace_id = request.headers.get("X-Trace-ID") or uuid.uuid4().hex
        TraceContext.set_trace_id(trace_id)

        response = await call_next(request)
        response.headers["X-Correlation-ID"] = cid
        response.headers["X-Trace-ID"] = trace_id
        return response

class TracingMiddleware(BaseHTTPMiddleware):
    """Measures request processing duration and attaches timing metrics."""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start_time) * 1000
        response.headers["X-Response-Time-Ms"] = f"{duration_ms:.2f}"
        return response
