import uuid
from contextvars import ContextVar
from typing import Optional

_correlation_id_ctx: ContextVar[str] = ContextVar("correlation_id", default="")
_trace_id_ctx: ContextVar[str] = ContextVar("trace_id", default="")
_user_id_ctx: ContextVar[Optional[str]] = ContextVar("user_id", default=None)

class TraceContext:
    @staticmethod
    def get_correlation_id() -> str:
        cid = _correlation_id_ctx.get()
        if not cid:
            cid = str(uuid.uuid4())
            _correlation_id_ctx.set(cid)
        return cid

    @staticmethod
    def set_correlation_id(cid: str) -> None:
        _correlation_id_ctx.set(cid)

    @staticmethod
    def get_trace_id() -> str:
        tid = _trace_id_ctx.get()
        if not tid:
            tid = uuid.uuid4().hex
            _trace_id_ctx.set(tid)
        return tid

    @staticmethod
    def set_trace_id(tid: str) -> None:
        _trace_id_ctx.set(tid)

    @staticmethod
    def get_user_id() -> Optional[str]:
        return _user_id_ctx.get()

    @staticmethod
    def set_user_id(uid: Optional[str]) -> None:
        _user_id_ctx.set(uid)

def get_correlation_id() -> str:
    return TraceContext.get_correlation_id()

def set_correlation_id(cid: str) -> None:
    TraceContext.set_correlation_id(cid)
