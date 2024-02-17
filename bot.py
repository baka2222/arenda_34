from aiogram import Dispatcher, Bot
from os import getenv
from dotenv import load_dotenv


load_dotenv()
bot = Bot(token=getenv('BOT'))
dp = Dispatcher()