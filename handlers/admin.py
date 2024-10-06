from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from handlers.filters import BotAdminMessageFilter, BotAdminCallbackFilter
from misc.config import conf, save_config
from misc.constants import admin_inline_keyboard


router = Router()


@router.message(Command(commands=["god"]), BotAdminMessageFilter())
async def admin_panel_command(message: Message):
    await message.answer("Здарова, отец!", reply_markup=admin_inline_keyboard)


@router.callback_query(F.data == "santa_progress", BotAdminCallbackFilter())
async def santa_progress_query(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        f"**{(taken := len(conf.santa_map))}/{(total := len(conf.santa_participants))}**"
        + ("\n\n__Ждем-с__:\n" if taken < total else "")
        + "\n".join(
            map(
                lambda p: p[1],
                filter(
                    lambda p: p[0] not in conf.santa_map.keys(),
                    conf.santa_participants.items(),
                ),
            )
        )
    )


@router.callback_query(F.data == "shutdown", BotAdminCallbackFilter())
async def shutdown_query(callback: CallbackQuery):
    save_config()

    await callback.answer()
    await callback.message.answer("Конфиг сохранен\nБот уходит в закат...")

    exit()
