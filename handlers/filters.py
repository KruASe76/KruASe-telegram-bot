from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from misc.constants import admin_id


class BotAdminMessageFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if flag := (message.from_user.id != admin_id):
            await message.reply("Ты не отец\! 🫵")
        return not flag


class BotAdminCallbackFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if flag := (callback.from_user.id != admin_id):
            await callback.answer("Ты не отец! 🫵")
        return not flag
