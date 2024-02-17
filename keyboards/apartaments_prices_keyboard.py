from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


APARTAMENT_PRICES = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1000-10000 (С подселением)', callback_data='1000-10000')
    ],
    [
        InlineKeyboardButton(text='10000-15000', callback_data='10000-15000'),
        InlineKeyboardButton(text='15000-25000', callback_data='15000-25000')
    ],
    [
        InlineKeyboardButton(text='25000-35000', callback_data='25000-35000'),
        InlineKeyboardButton(text='35000-50000', callback_data='35000-50000')
    ],
    [
        InlineKeyboardButton(text='50000-65000', callback_data='50000-65000'),
        InlineKeyboardButton(text='65000-85000', callback_data='65000-85000')
    ],
    [
        InlineKeyboardButton(text='85000-125000', callback_data='85000-125000'),
        InlineKeyboardButton(text='от 125000', callback_data='125000')
    ]
])

ZHALOBA = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Пожаловаться⛔", callback_data='zhaloba')]
])