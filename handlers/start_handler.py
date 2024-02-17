from aiogram import Router, types
from aiogram.filters import Command
from keyboards.options_keyboard import OPTIONS_KEYBOARD


start_rt = Router()
TEXT = 'Я постараюсь помочь Вам найти машину мечты в Бишкеке, без каких-либо посредников!'


@start_rt.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text=f'Добро пожаловать, {message.from_user.full_name}. ' + TEXT)
    await message.answer(text=f'Ваш ID: {message.from_user.id}')
    await message.answer(text='Пожалуйста, выберите опцию:', reply_markup=OPTIONS_KEYBOARD)
