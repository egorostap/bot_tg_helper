from aiogram import types, Dispatcher
from create_bot import dp, bot
import string

# mat = ['фак', 'сак', 'дик']

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