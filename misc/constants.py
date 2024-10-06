from os import path

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


config_path = path.join("cache", "config.pickle")
participants_path = path.join("participants.yml")


not_started_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[[InlineKeyboardButton(text="Бот", url="https://t.me/KruASe_bot")]]
)


lucky_suffix = "\n\n__Повезло повезло...__"


admin_id = 737286150

admin_inline_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text="Прогресс Тайного Санты 🎅", callback_data="santa_progress")],
        [InlineKeyboardButton(text="Спать! ⛔️", callback_data="shutdown")],
    ],
)
