from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_async_session
from app.dto import CarRead
from app.services.cars import list_cars
from app.users import current_active_user


router = APIRouter(prefix="/api/cars", tags=["cars"])


@router.get("", response_model=List[CarRead])
async def get_cars(
    session: AsyncSession = Depends(get_async_session),
    user=Depends(current_active_user),
):
    cars = await list_cars(session)
    return cars

