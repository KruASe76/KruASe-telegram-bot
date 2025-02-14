from aiogram.fsm.state import StatesGroup, State


class SpecialState(StatesGroup):
    started = State()
    solving_crossword = State()
    guessing_code = State()


class PrizeSettingState(StatesGroup):
    setting_prize = State()
