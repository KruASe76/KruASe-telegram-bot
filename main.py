import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from handlers import user
from handlers import admin


bot = Bot(token=os.environ.get("TOKEN"), efault=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


async def main():
    os.makedirs("cache", exist_ok=True)

    dp.include_router(user.router)
    dp.include_router(admin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
