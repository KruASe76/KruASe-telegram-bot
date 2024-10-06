import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from main import bot
from misc.config import conf
from misc.constants import not_started_keyboard, lucky_suffix


router = Router()


@router.message(Command(commands=["start", "help"]))
async def help_command(message: Message):
    await message.answer(
        "Привет! Я - бот великого недопрогера @KruASe\nУмею пока немного: всего пара команд",
        reply_markup=ReplyKeyboardRemove(),
    )

    if message.chat.type == "private":
        conf.users.add(message.from_user.id)


@router.message(Command(commands=["santa"]))
async def santa_command(message: Message):
    if (
        id := message.from_user.id
    ) not in conf.santa_participants.keys() and id not in conf.santa_map.values():
        await message.reply("Не для таких жалких людей, как ты, была создана эта команда!")
        return

    if not (
        participants := tuple(
            filter(
                lambda p: p[0] not in conf.santa_map.values() and p[0] != id,
                conf.santa_participants.items(),
            )
        )
    ):
        if len(conf.santa_map) + 1 == len(conf.santa_participants):
            await message.reply(
                "Ты последним вызвал эту команду, и так получилось...\nЧто ты еще и единственный, "
                f"кто остался невыбранным...\nПолучается, ты сам себе Санта в этот раз{lucky_suffix}"
            )
        else:
            await message.reply("Всех уже разобрали\!\n\n__А все а раньше надо было__")
        return

    if id not in conf.users:
        await message.reply(
            "Сначала запусти бота!\nТаковы правила Телеграма...",
            reply_markup=not_started_keyboard,
        )
        return

    if id in conf.santa_map.keys():
        await bot.send_message(
            id,
            f"Тебе уже предоставлен подопечный!\nА именно **{conf.santa_participants[conf.santa_map[id]]}**",
        )
        return

    recipient_id, recipient_name = random.choice(participants)

    conf.santa_map[id] = recipient_id

    await bot.send_message(
        id,
        f"__Запрос {len(conf.santa_map)}/{len(conf.santa_participants)}__\n\n"
        f"Тебе достается...\n**{recipient_name}**\!"
        f"{lucky_suffix if recipient_name == 'Борис Игоревич' else ''}",  # easter egg
    )
