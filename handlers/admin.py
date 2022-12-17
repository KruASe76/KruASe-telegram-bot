from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from handlers.filters import BotAdminFilter
from misc.config import conf, save_config
from misc.constants import admin_inline_keyboard


router = Router()


@router.message(Command(commands=["god"]), BotAdminFilter())
async def admin_panel_command(message: Message):
    await message.answer("Здравствуй, отец\!", reply_markup=admin_inline_keyboard)


@router.callback_query(Text(text="santa_progress"))
async def shutdown_query(callback: CallbackQuery):
    await callback.answer(f"{len(conf.santa_map)}/{len(conf.santa_participants)}")

@router.callback_query(Text(text="shutdown"))
async def shutdown_query(callback: CallbackQuery):
    save_config()

    await callback.answer()
    await callback.message.answer("Конфиг сохранен\nБот уходит в закат\.\.\.")

    exit()
