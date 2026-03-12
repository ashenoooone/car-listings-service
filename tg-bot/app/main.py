import asyncio

from aiogram import Bot, Dispatcher

from .config import get_settings
from .handlers import router


async def main() -> None:
    settings = get_settings()
    bot = Bot(token=settings.telegram_bot_token)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

