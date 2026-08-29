"""FastAPI Application Main Entrypoint for Inventory Management Service."""

import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.inventory_service.controllers.routes import router
from services.inventory_service.config.settings import settings
from shared.tracing.middleware import CorrelationIdMiddleware, TracingMiddleware
from shared.exceptions.handlers import setup_exception_handlers

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Application startup lifecycle: initialize DB pools, subscribe event consumers
    yield
    # Application shutdown lifecycle: terminate worker pools, release connections

app = FastAPI(
    title="Inventory Management Service",
    description="Tracks real-time stock levels across warehouses, supports 15-minute stock holds with TTL, and restock alerts.",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(CorrelationIdMiddleware)
app.add_middleware(TracingMiddleware)

setup_exception_handlers(app)
app.include_router(router)

@app.get("/health", tags=["Health Probes"])
async def health_check():
    return {
        "status": "healthy",
        "service": "inventory_service",
        "port": settings.PORT,
        "environment": settings.ENVIRONMENT
    }

@app.get("/ready", tags=["Health Probes"])
async def readiness_check():
    return {"status": "ready", "service": "inventory_service"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)
