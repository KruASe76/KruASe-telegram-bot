import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from main import bot
from misc.config import config
from misc.constants import lucky_suffix


router = Router()


@router.message(Command(commands=["start", "help"]))
async def help_command(message: Message):
    await message.answer(
        "Привет\! Я \- бот великого недопрогера @KruASe\nУмею пока немного: всего пара команд"
    )


@router.message(Command(commands=["santa"]))
async def santa_command(message: Message):
    if (id := message.from_user.id) in config.santa_map.keys():
        await bot.send_message(id, f"Тебе уже предоставлен подопечный\!\nА именно *{config.santa_map[id]}*")
        return

    if not config.santa_participants:
        await message.reply("Всех уже разобрали\!\n\n_А все а раньше надо было_")
        return

    recipient_id, recipient_name = random.choice(tuple(config.santa_participants.items()))
    while recipient_id == message.from_user.id:
        recipient_id, recipient_name = random.choice(config.santa_participants.items())

    config.santa_participants.pop(recipient_id)
    config.santa_map[message.from_user.id] = recipient_name

    await bot.send_message(
        message.from_user.id,
        f"__Запрос {len(config.santa_map)}/{len(config.santa_participants) + len(config.santa_map)}__\n\n"
        f"Тебе достается\.\.\.\n*{recipient_name}*\!"
        f"{lucky_suffix if recipient_name == 'Борис Игоревич' else ''}"
    )
