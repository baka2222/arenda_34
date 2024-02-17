import asyncio

from aiogram import types, Router, F
from keyboards.during_parser_keyboard import DURING_PARSING_KEYBOARD, AFTER_PARSING_KEYBOARD
from keyboards.apartaments_prices_keyboard import ZHALOBA
from bot import bot
from parser import parser


prices_rt = Router()
letting = True
params = ''
message = ''


@prices_rt.callback_query()
async def prices_cb_handler(callback: types.CallbackQuery):
    global params
    params = callback.data
    await callback.message.edit_text(text=f'Вы выбрали диапозон {params}')
    await callback.answer()


@prices_rt.message()
async def send_parsed_data(msg: types.Message):
    global params
    global message
    if msg.text == 'Запустить отправку' or msg.text == 'Остановить отправку':
        message = msg.text
    print(message)
    if message == 'Запустить отправку':
        print(params.split(sep='-'))
        await msg.reply(text='Сбор данных может занять немного времени', reply_markup=DURING_PARSING_KEYBOARD)
        frm = params.split(sep='-')[0]
        if params.split(sep='-')[1]:
            to = params.split(sep='-')[1]
        else:
            to = ''
        for i in parser(count=5, frm=frm, to=to):
            if message != 'Остановить отправку':
               await bot.send_media_group(media=types.InputMediaPhoto(i['img']),
                                          chat_id=msg.from_user.id,
                                          )
               await msg.answer(text=f'''Описание: {i["title"]}\n
               Прайс: {i["price"]}\n
               Депозит: {i["deposit"]}\n
               Дополнительная информация: {i["dop_info"]}\n\n
               Телефон: {i["phone"]}''', reply_markup=ZHALOBA)
               await asyncio.sleep(1.5)


@prices_rt.callback_query(F.data == 'zhaloba')
async def dncikrlvlswio(cb: types.CallbackQuery):
    await cb.answer('Жалоба отправлена!')