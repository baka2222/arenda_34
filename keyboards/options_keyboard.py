from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


OPTIONS_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Поиск квартир', callback_data='Apartaments')
    ]
])