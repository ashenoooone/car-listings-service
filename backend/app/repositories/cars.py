from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Car


async def list_cars(session: AsyncSession) -> Sequence[Car]:
    result = await session.execute(select(Car))
    return result.scalars().all()

