from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


DURING_PARSING_KEYBOARD = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Остановить отправку")]
], resize_keyboard=True)

AFTER_PARSING_KEYBOARD = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Запустить отправку")]
], resize_keyboard=True)