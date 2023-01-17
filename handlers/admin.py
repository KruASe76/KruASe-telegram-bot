from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from handlers.filters import BotAdminMessageFilter, BotAdminCallbackFilter
from misc.config import conf, save_config
from misc.constants import admin_inline_keyboard


router = Router()


@router.message(Command(commands=["god"]), BotAdminMessageFilter())
async def admin_panel_command(message: Message):
    await message.answer("Здарова, отец\!", reply_markup=admin_inline_keyboard)


@router.callback_query(Text(text="santa_progress"), BotAdminCallbackFilter())
async def shutdown_query(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        f"*{(taken := len(conf.santa_map))}/{(total := len(conf.santa_participants))}*" +
        ("\n\n_Ждем\-с_:\n" if taken < total else "") +
        "\n".join(map(
            lambda p: p[1],
            filter(lambda p: p[0] not in conf.santa_map.keys(), conf.santa_participants.items())
        ))
    )

@router.callback_query(Text(text="shutdown"), BotAdminCallbackFilter())
async def shutdown_query(callback: CallbackQuery):
    save_config()

    await callback.answer()
    await callback.message.answer("Конфиг сохранен\nБот уходит в закат\.\.\.")

    exit()
