from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import kb_client
import sqlite3

ans = 'Добрый день! Я помощник.\nЗадайте интересующие Вас вопросы, мы ответим на них в самое ближайшее время.\nИли оставьте ваши контактные данные для связи:)'


# старт переписки
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
  await bot.send_message(message.from_user.id, ans, reply_markup=kb_client)

# команды
# @dp.message_handler(commands=['перезвоните'])
async def command_1(message : types.Message):
  await bot.send_message(message.from_user.id, 'команда 1')

# @dp.message_handler(commands=['связь со специалистом'])
async def command_2(message : types.Message):
  await bot.send_message(message.from_user.id, 'команда 2')


# функция для передачи функций в другие файлы
def registr_handlers_client(dp : Dispatcher):
  dp.register_message_handler(command_start, commands=['start', 'help'])
  dp.register_message_handler(command_1, commands=['к1'])
  dp.register_message_handler(command_2, commands=['к2'])






# база данных пользователей
#   # connect db
#   connect = sqlite3.connect('users.db')
#   cursor = connect.cursor()
#   # create table
#   cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
#           id INTEGER
#           )""")
#   connect.commit()
#
#   # check
#   people_id = message.chat.id
#   cursor.execute(f"""SELECT id FROM login_id WHERE id = {people_id}""")
#   data = cursor.fetchone()
#   if data is None:
#     # add values
#     user_id = [message.chat.id]
#     cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
#     connect.commit()
#   else:
#     bot.send_message(message.chat.id, 'вы уже зарегистрированы')
#
#
# @dp.message_handler(commands=['delete'])
# async def command_start(message : types.Message):
#
#   # connect db
#   connect = sqlite3.connect('users.db')
#   cursor = connect.cursor()
#   # delete id from table
#   people_id = message.chat.id
#   cursor.execute(f"""DELETE FROM login_id WHERE id = {people_id}""")
#   connect.commit()





#для пользователей которые зашли с группы
# try:
#   await bot.send_message(message.from_user.id, "Добрый день")
#   await message.delete()
# except:
#   await message.reply('Общение с ботом через ЛС')

# await message.answer('как сам?')
# await message.reply(message.text)
# await bot.send_message(message.from_user.id, message.text)