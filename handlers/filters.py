from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from misc.constants import admin_id, special_id


class BotAdminMessageFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user is not None and message.from_user.id == admin_id


class BotAdminCallbackFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return callback.from_user.id == admin_id


class SpecialMessageFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user is not None and message.from_user.id == special_id


class SpecialCallbackFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return not callback.from_user.id == special_id
