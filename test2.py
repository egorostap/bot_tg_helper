# !pip install python-telegram-bot --upgrade
# !pip install -U scikit-learn


import random
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# создаем интенты
# bot_config = {
#     'intents': {
#         'hello': {
#             'examples': ['хай', 'приветики', 'здравствуйте', 'привет'],
#             'responses': ['добрый день', 'Здравствуйте', 'Добрый вечер!']
#         },
#         'bye': {
#             'examples': ['пока', 'досвидания', 'до встречи', 'хорошего дня'],
#             'responses': ['до связи', 'пока', 'хорошего дня']
#         },
#         'how_are_you': {
#             'examples': ['как выши дела', 'как дела', 'как осбтановка', 'ну как?'],
#             'responses': ['все ок', 'отлично', 'нормально нереально!']
#         }
#     },
#     'not_found': {
#         'responses': ['извините, не удалось определить интент', 'не совсем понял']
#     }
# }

# записываем файл json
# with open('bot_config.json', 'w') as f:
#   json.dump(bot_config, f)

# считываем файл json
with open ('bot_config.json', 'r') as a:
  bot_config = json.load(a)

# задаем функции обработки данных
def get_intent_by_model(text):
  return clf.predict(vectorizer.transform([text]))[0]

# ...
X = []
y = []
for intent in bot_config['intents']:
  for example in bot_config['intents'][intent]['examples']:
    X.append(example)
    y.append(intent)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# применяем векторзайзер
# ngram_range=(1, 3), analyzer='char_wb', min_df=5
# vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='char_wb', min_df=5)
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# vectorizer.get_feature_names()

# применяем классифаер
clf = RandomForestClassifier()
# clf = LogisticRegression()
clf.fit(X_train_vectorized, y_train)

# проверяем точность модели
print(clf.score(X_train_vectorized, y_train))
print(clf.score(X_test_vectorized, y_test))
print(clf.predict(vectorizer.transform(['хай'])))

def bot(text):
  intent = get_intent_by_model(text)
  return random.choice(bot_config['intents'][intent]['responses'])

# запуск основного цикла программы в самом коде для проверки работы
while True:
  input_text = input()
  if input_text != 'exit':
    response = bot(input_text)
    print(response)
  else:
    break
#
#
# # тело телеграм бота
# # Enable logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
#
# logger = logging.getLogger(__name__)
#
#
# # Define a few command handlers. These usually take the two arguments update and
# # context.
# def start(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     update.message.reply_markdown_v2(
#         fr'Hi {user.mention_markdown_v2()}\!',
#         reply_markup=ForceReply(selective=True),
#     )
#
#
# def help_command(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('Help!')
#
#
# def echo(update: Update, context: CallbackContext) -> None:
#     """Echo the user message."""
#     out_text = bot(update.message.text)
#     update.message.reply_text(out_text)
#
#
# def main() -> None:
#     """Start the bot."""
#     # Create the Updater and pass it your bot's token.
#     updater = Updater("2134665881:AAGw6AqzJwfyADPDQku-PbefzH7ZTBMBMtQ")
#
#     # Get the dispatcher to register handlers
#     dispatcher = updater.dispatcher
#
#     # on different commands - answer in Telegram
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("help", help_command))
#
#     # on non command i.e message - echo the message on Telegram
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
#
#     # Start the Bot
#     updater.start_polling()
#
#     # Run the bot until you press Ctrl-C or the process receives SIGINT,
#     # SIGTERM or SIGABRT. This should be used most of the time, since
#     # start_polling() is non-blocking and will stop the bot gracefully.
#     updater.idle()
#
# main()