import os
import random
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from constants import default_keyboard, admin_keyboard, admin_id
from config import config, save_config


bot = Bot(token=os.environ.get("TOKEN"), parse_mode="MarkdownV2")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def help(message: Message):
    await message.answer(
        "Привет\! Я \- бот великого недопрогера @KruASe\nУмею пока немного: внизу всего пара кнопок",
        reply_markup=admin_keyboard if message.from_id == admin_id else default_keyboard
    )


@dp.message_handler(Text(equals=default_keyboard.keyboard[0][0].text))  # Тайный Санта
async def santa(message: Message):
    if message.from_id in config.santa_used_ids:
        await message.reply(
            "Тебе уже предоставлен подопечный\!"
        )
        return

    name = random.choice(config.santa_participants)
    config.santa_participants.remove(name)
    config.santa_used_ids.append(message.from_id)

    await message.reply(
        f"__Запрос {len(config.santa_used_ids)}/{len(config.santa_participants) + len(config.santa_used_ids)}__\n\n"
        f"Тебе достается\.\.\.\n*{name}*\!"
    )


@dp.message_handler(Text(equals=admin_keyboard.keyboard[-1][0].text))
async def admin_panel(message: Message):
    save_config()

    await message.answer("Конфиг сохранен\nБот уходит в закат")

    exit()


def main():
    logging.basicConfig(level=logging.INFO)

    executor.start_polling(dp)


if __name__ == '__main__':
    main()
