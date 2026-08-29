from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

class AsyncDatabaseSessionManager:
    """Async SQLAlchemy engine and session manager."""

    def __init__(self, db_url: str = "sqlite+aiosqlite:///:memory:") -> None:
        self.engine = create_async_engine(db_url, echo=False, pool_pre_ping=True)
        self.session_maker = async_sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False)

    async def close(self) -> None:
        if self.engine:
            await self.engine.dispose()

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    # Placeholder session generator for FastAPI Depends
    yield None
