import asyncio
import os
import logging

from aiogram import Bot, Dispatcher

from handlers import user
from handlers import admin


bot = Bot(token=os.environ.get("TOKEN"), parse_mode="MarkdownV2")
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


async def main():
    dp.include_router(user.router)
    dp.include_router(admin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
