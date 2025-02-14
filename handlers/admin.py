import sys

import aiofiles
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.filters import BotAdminMessageFilter, BotAdminCallbackFilter
from handlers.fsm import PrizeSettingState
from handlers.keyboards import admin_inline_keyboard
from misc.constants import prize_message_file_path

router = Router()


@router.message(Command(commands=["god"]), BotAdminMessageFilter())
async def admin_panel_command(message: Message):
    await message.answer("Здарова, отец\!", reply_markup=admin_inline_keyboard)


@router.callback_query(F.data == "shutdown", BotAdminCallbackFilter())
async def shutdown_query(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Бот уходит в закат\.\.\.")

    sys.exit()


@router.message(Command(commands=["prize"]), BotAdminMessageFilter())
async def prize_command(message: Message, state: FSMContext):
    await message.answer("Отец, введи новый текст для приза\!")

    await state.set_state(PrizeSettingState.setting_prize)


@router.message(StateFilter(PrizeSettingState.setting_prize))
async def set_prize(message: Message, state: FSMContext):
    async with aiofiles.open(prize_message_file_path, "w") as file:
        await file.write(message.text)

    await message.reply("Принято\!")

    await state.clear()
