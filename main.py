#
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from ai import bot_ai
import sqlite3 as sq

# подключение бд
def sql_start():
    global base, cur
    base = sq.connect('good_bot.db')
    cur = base.cursor()
    if base:
        print('db connected ok')
    base.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
        )""")
    base.commit()


API_TOKEN = '2116329079:AAFgVBURPKMmEAd-diNNMNi6NE1eYBKnFrs'
channel_id = '-702966975'

# bot = Bot(token="")
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

ans = 'Добрый день! Я помощник.\nЗадайте интересующие Вас вопросы, мы ответим на них в самое ближайшее время.\nИли оставьте ваши контактные данные для связи:)'

specialist = {'Лев':'@leo', 'Ирина':'@irina'}

# старт
@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ['позвонить', 'специалисты']
    b1 = KeyboardButton(start_buttons[0], request_contact=True)
    b2 = KeyboardButton(start_buttons[1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(b1, b2)
    # kb_client.row(b1)

    # проверка на наличие айди в бд и новая запись в случае отсутствия
    sql_start()
    people_id = message.chat.id
    print(people_id)
    cur.execute(f"""SELECT id FROM login_id WHERE id = {people_id}""")
    data = cur.fetchone()
    print(data)
    if data is None:
        # добавить пользоателя
        user_id = [message.chat.id]
        cur.execute("INSERT INTO login_id VALUES(?);", user_id)
        base.commit()
    # отправка приветств сообщения
    await message.answer(ans, reply_markup=keyboard)
    # else:
    #     await message.answer('Такой пользователь уже есть', reply_markup=keyboard)


# удаление пользователя
@dp.message_handler(commands="delete")
async def delet(message: types.Message):
    # удаление пользователя
    sql_start()
    people_id = message.chat.id
    cur.execute(f"""DELETE FROM login_id WHERE id = {people_id}""")
    base.commit()
    await message.answer('пользователь удален')

# команда специалисты
@dp.message_handler(Text(equals='специалисты'))
async def call(message: types.Message):
    card = f"{hbold('список специалистов: ')}\n" \
           f"{hbold('Лев: ')} {specialist['Лев']}\n" \
           f"{hbold('Ирина: ')} {specialist['Ирина']}\n"

    await message.answer(card)

# сообщения
@dp.message_handler()
async def echo_send(message: types.Message):
    answer = bot_ai(message.text)
    await message.answer(answer)


if __name__ == "__main__":
    sql_start()
    executor.start_polling(dp)