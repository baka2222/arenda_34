from aiogram import types, Router, F
from keyboards.apartaments_prices_keyboard import APARTAMENT_PRICES
from bot import bot


apartaments_rt = Router()


@apartaments_rt.callback_query(F.data == 'Apartaments')
async def apartaments_handler(callback: types.CallbackQuery):
    await bot.send_message(text='Выберите диапaзон цены в сомах, чтобы облегчить поиск:',
                           reply_markup=APARTAMENT_PRICES,
                           chat_id=callback.from_user.id)
    await callback.answer()