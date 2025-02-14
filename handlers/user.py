import asyncio

import aiofiles
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.utils.formatting import Text, Spoiler, Italic

from handlers.filters import SpecialMessageFilter
from handlers.fsm import SpecialState
from handlers.keyboards import special_crossword_tasks_reply_keyboard, special_code_inline_keyboard
from misc.constants import invisible_separator, digit_to_emoji, prize_message_file_path

router = Router()


@router.message(Command(commands=["start", "help"]))
async def help_command(message: Message, state: FSMContext):
    await message.answer(
        (
            "Привет\! Я \- бот недопрогера @KruASe\n"
            "Умею пока немного: всего пара команд"
        ),
        reply_markup=ReplyKeyboardRemove(),
    )

    if await SpecialMessageFilter()(message):
        await message.answer(
            (
                "_О, неужели, это вы, госпожа, добро пожаловать\!_\n"
                "_Если вы здесь, значит, этот день настал\.\.\._"
            ),
            reply_markup=special_crossword_tasks_reply_keyboard,
        )

        await state.set_state(SpecialState.started)


@router.message(
    F.text == special_crossword_tasks_reply_keyboard.keyboard[0][0].text,
    SpecialMessageFilter(),
    StateFilter(SpecialState.started)
)
async def special_crossword_tasks(message: Message, state: FSMContext):
    await message.reply(
        (
            "_Повелитель поручил мне передать это:_\n\n"
            "*1\.* Мой главный коуч по отношениям\n"
            "*2\.* Аниме, с которого все началось\n"
            "*3\.* Исторически первая жертва твоего шипа со мной\n"
            "*4\.* Самый неудачный мой подарок\n"
            '*5\.* Наш традиционный ответ на "вот разлюбишь меня\.\.\."\n'
            "*6\.* Пока единственный город вне МО, где мы побывали вместе\n"
            "*7\.* Парк, в котором была первая встреча\n"
            "*8\.* Исторически самый первый твой локальный конкурент\n\n"
            "_Госпожа, когда закончите с кроссвордом, напишите финальный ответ, и я подскажу, что делать дальше_"
        ),
        reply_markup=ReplyKeyboardRemove(),
    )

    await state.set_state(SpecialState.solving_crossword)


@router.message(
    SpecialMessageFilter(),
    StateFilter(SpecialState.solving_crossword)
)
async def special_crossword_solution(message: Message, state: FSMContext):
    if message.text.lower().replace("ё", "е") != "чертенок":
        await message.delete()
        sent_message = await message.answer(
            (
                "_Сделаем вид, что этой попытки не было :\)_"
            )
        )

        await asyncio.sleep(3)

        await sent_message.delete()

        return

    await message.reply(
        (
            "_О, я и не сомневался, что вы справитесь\!_\n"
            "_Остался лишь последний шаг\.\.\._"
        ),
    )

    await message.answer(
        (
            "_Введите четырехзначный код_\n\n"
            "*Подсказка:* ||Количество дней, проведенных вместе||\n\n"
            "_Текущий ввод:_\n"
            f"{invisible_separator}"
        ),
        reply_markup=special_code_inline_keyboard,
    )

    await state.set_state(SpecialState.guessing_code)


@router.callback_query(
    SpecialMessageFilter(),
    F.data.regexp(r"digit_\d")
)
async def digit_input(callback: CallbackQuery, state: FSMContext):
    correct_code = "".join(digit_to_emoji[digit] for digit in "1036")

    new_message_text = callback.message.md_text + digit_to_emoji[callback.data[-1]]
    await callback.message.edit_text(
        new_message_text,
        reply_markup=special_code_inline_keyboard,
    )

    if new_message_text.split(invisible_separator)[-1] == correct_code:
        await callback.answer()
        await callback.message.delete_reply_markup()

        async with aiofiles.open(prize_message_file_path, "r") as file:
            prize_message = await file.read()
            prize_message = prize_message.strip()

        content = Text(Italic("И вы выигрываете..."), "\n\n", Spoiler(prize_message))
        await callback.message.answer(**content.as_kwargs())

        await state.clear()
    elif len(new_message_text.split(invisible_separator)[-1]) >= len(correct_code):
        await callback.answer(
            text="Сделаем вид, что этой попытки не было :)",
            show_alert=True,
        )

        await callback.message.edit_text(
            new_message_text.split(invisible_separator)[0] + invisible_separator,
            reply_markup=special_code_inline_keyboard,
        )
