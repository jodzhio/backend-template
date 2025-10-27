from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

from .config import settings

DATABASE_URL = settings.DB_URL

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def db_session() -> AsyncGenerator[AsyncSession, Any]:
    async with Session() as session:
        yield session
