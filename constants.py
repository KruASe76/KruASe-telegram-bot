from os import path, makedirs

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


admin_id = 737286150

makedirs("cache", exist_ok=True)
config_path = path.join("cache", "config.pickle")
names_path = path.join("names.txt")

default_buttons = [
    [
        KeyboardButton(text="Тайный Санта 🎅")
    ]
]
default_keyboard = ReplyKeyboardMarkup(
    keyboard=default_buttons,
    resize_keyboard=True
)
admin_buttons = default_buttons.copy()
admin_buttons.append([KeyboardButton(text="Панель Бога 💻")])
admin_keyboard = ReplyKeyboardMarkup(
    keyboard=admin_buttons,
    resize_keyboard=True
)
