from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Car
from app.repositories.cars import list_cars as list_cars_repo


async def list_cars(session: AsyncSession) -> Sequence[Car]:
    return await list_cars_repo(session)

