from abc import ABC, abstractmethod

class IUnitOfWork(ABC):
    async def __aenter__(self) -> "IUnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass

class SQLAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self, session: Any = None) -> None:
        self.session = session

    async def commit(self) -> None:
        if self.session:
            await self.session.commit()

    async def rollback(self) -> None:
        if self.session:
            await self.session.rollback()
