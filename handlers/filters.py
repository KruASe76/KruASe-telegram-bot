from aiogram.filters import BaseFilter
from aiogram.types import Message

from misc.constants import admin_id


class BotAdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == admin_id
