from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .base import AppException

def setup_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "type": f"urn:cloudmart:error:{exc.code.lower()}",
                "title": exc.code,
                "status": exc.status_code,
                "detail": exc.message,
                "instance": str(request.url)
            }
        )
