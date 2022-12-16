from os import path, makedirs

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


makedirs("../cache", exist_ok=True)
config_path = path.join("cache", "config.pickle")
participants_path = path.join("participants.yml")


lucky_suffix = "\n\n_Повезло повезло\.\.\._"


admin_id = 737286150

admin_inline_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Прогресс Тайного Санты 🎅",
                callback_data="santa_progress"
            )
        ],
        [
            InlineKeyboardButton(
                text="Спать! ⛔️",
                callback_data="shutdown"
            )
        ]
    ]
)
