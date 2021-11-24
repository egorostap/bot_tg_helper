from aiogram import types, Dispatcher
from create_bot import dp, bot
import string

# mat = ['фак', 'сак', 'дик']

# поидее должен отправлять сообщения пользователя в группу
# API_TOKEN = 'BOT TOKEN HERE'
# CHANNEL_ID = <CHANNEL ID HERE> # это должен быть int, например -1006666666666
#
# bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
#
#
# async def send_message(channel_id: int, text: str):
#     await bot.send_message(channel_id, text)
#
#
# async def main():
#     await send_message(CHANNEL_ID, '<b>Hello!</b>')
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


# @dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer('ok')
# фильтр матов
# if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
#   .intersection(set(mat)) != set():
#     await message.reply('маты запрещены')
#     await message.delete()


# функция для передачи функций в другие файлы
def registr_handlers_other(dp : Dispatcher):
  dp.register_message_handler(echo_send)



bot_config = {
    'intents': {
        'hello': {
            'examples': ['доброго', 'добрый день', 'здравствуйте', 'привет'],
            'responses': ['добрый день', 'Здравствуйте', 'Добрый вечер!']
        },
        'bye': {
            'examples': ['пока', 'досвидания', 'до встречи', 'хорошего дня'],
            'responses': ['всего хорошего', 'досвидания', 'хорошего дня']
        },
        'how_are_you': {
            'examples': ['как выши дела', 'как дела', 'как осбтановка', 'ну как?'],
            'responses': ['все ок', 'отлично', 'нормально нереально!']
        }
    },
    'not_found': {
        'responses': ['извините, я только учусь и не все понимаю', 'не совсем понял']
    }
}



# await message.answer('как сам?')
# await message.reply(message.text)
# await bot.send_message(message.from_user.id, message.text)