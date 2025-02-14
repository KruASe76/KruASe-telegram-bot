from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

not_started_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Бот", url="https://t.me/KruASe_bot")]],
)

admin_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Спать! ⛔️", callback_data="shutdown")],
    ],
)

special_crossword_tasks_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить задания для кроссворда")]
    ],
    is_persistent=True,
    resize_keyboard=True,
    one_time_keyboard=True,
)

special_code_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="digit_1"),
            InlineKeyboardButton(text="2️⃣", callback_data="digit_2"),
            InlineKeyboardButton(text="3️⃣", callback_data="digit_3"),
        ],
        [
            InlineKeyboardButton(text="4️⃣", callback_data="digit_4"),
            InlineKeyboardButton(text="5️⃣", callback_data="digit_5"),
            InlineKeyboardButton(text="6️⃣", callback_data="digit_6"),
        ],
        [
            InlineKeyboardButton(text="7️⃣", callback_data="digit_7"),
            InlineKeyboardButton(text="8️⃣", callback_data="digit_8"),
            InlineKeyboardButton(text="9️⃣", callback_data="digit_9"),
        ],
        [
            InlineKeyboardButton(text="0️⃣", callback_data="digit_0"),
        ],
    ]
)
