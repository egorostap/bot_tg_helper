# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state  import State, StatesGroup
# from aiogram import types
#
#
# class FSMadmin(StageGroup):
#     photo = State()
#     name = State()
#     description = State()
#     price = State()
#
#
#
# @dp.message_handler(commands='загрузить', state=None)
# async def cm_start(message : types.Message):
#     await FSMadmin.photo.set()
#     await message.reply('загрузить фото')