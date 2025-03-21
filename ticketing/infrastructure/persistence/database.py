from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.config import settings

engine = create_async_engine(settings.database_url)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
