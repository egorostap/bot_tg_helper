from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# storage = MemoryStorage
token = '2116329079:AAFgVBURPKMmEAd-diNNMNi6NE1eYBKnFrs'

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)