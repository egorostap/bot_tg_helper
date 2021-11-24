from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('поделиться номером', request_contact=True)
b2 = KeyboardButton('/специалисты')



kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1)
# kb_client.add(b1).insert(b2)