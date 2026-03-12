from typing import List

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from .config import get_settings
from .db import get_async_session
from .llm import CarSearchFilters, extract_filters_from_query
from .models import Car


router = Router()
settings = get_settings()


def _apply_filters(stmt: Select[Car], filters: CarSearchFilters) -> Select[Car]:
    if filters.make:
        stmt = stmt.where(Car.make.ilike(f"%{filters.make}%"))
    if filters.model:
        stmt = stmt.where(Car.model.ilike(f"%{filters.model}%"))
    if filters.color:
        stmt = stmt.where(Car.color.ilike(f"%{filters.color}%"))
    if filters.max_price is not None:
        stmt = stmt.where(Car.price <= filters.max_price)
    if filters.min_price is not None:
        stmt = stmt.where(Car.price >= filters.min_price)
    if filters.min_year is not None:
        stmt = stmt.where(Car.year >= filters.min_year)
    if filters.max_year is not None:
        stmt = stmt.where(Car.year <= filters.max_year)
    return stmt


def _format_cars(cars: List[Car]) -> str:
    parts: List[str] = []
    for car in cars:
        line = (
            f"{car.make} {car.model}, {car.year} г.\n"
            f"Цена: {car.price}\n"
            f"Цвет: {car.color or 'не указан'}\n"
            f"Ссылка: {car.url}"
        )
        parts.append(line)
    return "\n\n".join(parts)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        "Привет! Я бот для поиска авто.\n\n"
        "Напиши запрос в свободной форме, например:\n"
        "— Найди красную BMW до 2 млн\n"
        "— Нужна Toyota Corolla после 2015 года до 1.5 млн\n"
        "Я попробую найти подходящие варианты в базе."
    )


@router.message()
async def handle_free_text(message: Message) -> None:
    text = (message.text or "").strip()
    if not text:
        await message.answer("Пожалуйста, отправь текстовый запрос.")
        return

    await message.chat.do("typing")

    try:
        filters = await extract_filters_from_query(text)
    except Exception as exc:  # noqa: BLE001
        await message.answer(
            "Не удалось обратиться к LLM-сервису для разбора запроса. "
            "Попробуй позже."
        )
        return

    async for session in get_async_session():
        stmt: Select[Car] = select(Car).limit(settings.max_results)
        stmt = _apply_filters(stmt, filters)
        result = await session.execute(stmt)
        cars = list(result.scalars().all())

    if not cars:
        await message.answer("По твоему запросу ничего не найдено.")
        return

    reply = _format_cars(cars)
    await message.answer(reply)

