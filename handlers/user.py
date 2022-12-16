import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.exceptions import TelegramForbiddenError

from main import bot
from misc.config import conf
from misc.constants import not_started_keyboard, lucky_suffix


router = Router()


@router.message(Command(commands=["start", "help"]))
async def help_command(message: Message):
    await message.answer(
        "Привет\! Я \- бот великого недопрогера @KruASe\nУмею пока немного: всего пара команд"
    )


@router.message(Command(commands=["santa"]))
async def santa_command(message: Message):
    if (id := message.from_user.id) not in conf.santa_participants.keys() and id not in conf.santa_map.keys():
        await message.reply("Не для таких жалких людей, как ты, была создана эта команда\!")
        return

    if (id := message.from_user.id) in conf.santa_map.keys():
        try:
            await bot.send_message(id, f"Тебе уже предоставлен подопечный\!\nА именно *{conf.santa_map[id]}*")
        except TelegramForbiddenError:
            await message.reply("Сначала запусти бота\!\nТаковы правила Телеграма", reply_markup=not_started_keyboard)
        return

    if not conf.santa_participants:
        await message.reply("Всех уже разобрали\!\n\n_А все а раньше надо было_")
        return

    recipient_id, recipient_name = random.choice(tuple(conf.santa_participants.items()))
    while recipient_id == message.from_user.id:
        recipient_id, recipient_name = random.choice(conf.santa_participants.items())

    conf.santa_participants.pop(recipient_id)
    conf.santa_map[message.from_user.id] = recipient_name

    await bot.send_message(
        message.from_user.id,
        f"__Запрос {len(conf.santa_map)}/{len(conf.santa_participants) + len(conf.santa_map)}__\n\n"
        f"Тебе достается\.\.\.\n*{recipient_name}*\!"
        f"{lucky_suffix if recipient_name == 'Борис Игоревич' else ''}"
    )
