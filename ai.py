# !pip install python-telegram-bot --upgrade
# !pip install -U scikit-learn
import nltk
import random
# import json
# from sklearn.linear_model import LogisticRegression
# from apscheduler.schedulers.background import BackgroundScheduler
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split

# создаем интенты
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
        'how_much': {
            'examples': ['стоимость', 'прайс', 'цена', 'сколько стоит?', 'ваши цены', 'ваш прайс', 'сколько', 'денег', 'здравствуйте, какая цена?', 'здравствуйте, сколько стоит?'],
            'responses': ['Cтоимость участков вы можете посмотреть по этой ссылке:\nhttps://xn---59-6cdammf4acpbk6acgco3bf71a.xn--p1ai/map', 'участок ИЖС + 2-х комнатный дом по цене 650 т.р.']
        },
        'where': {
            'examples': ['где находится', 'расположение', 'где вы находитесь', 'в какую сторону', 'как добраться', 'месторасположение'],
            'responses': ['ул. Пушкина д. 23 ']
        },
        'contact': {
            'examples': ['ваши контакты', 'как с вами связаться', 'ваш телефон', 'как вам позвонить', 'ваш номер', 'номер телефона'],
            'responses': ['наши контакты: +7 777 777 77 77', 'вы можете с нами связаться: +7 777 777 77 77', 'наши контактные данные: +7 777 777 77 77']
        }
    },
    'not_found': {
        'responses': ['извините, я только учусь и не все понимаю)']
    }
}

def clean(text):
  clean_text = ''
  for ch in text.lower():
    if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
      clean_text += ch
  return clean_text

def get_intent(text):
  for intent in bot_config['intents'].keys():
    # print(intent)
    for example in bot_config['intents'][intent]['examples']:
      # print(example)
      cleaned_example = clean(example)
      cleaned_text = clean(text)
      if nltk.edit_distance(cleaned_example, cleaned_text) / max(len(cleaned_example), len(cleaned_text)) < 0.4:
        # print('нашел!')
        return intent
  return 'not_found'

def bot_ai(text):
  intent = get_intent(text)
  if intent!= 'not_found':
    return random.choice(bot_config['intents'][intent]['responses'])
  else:
    return random.choice(bot_config['not_found']['responses'])

# bot('Привет!345')




#
# # записываем файл json
# # with open('bot_config.json', 'w') as f:
# #   json.dump(bot_config, f)
#
# # считываем файл json
# with open ('bot_config.json', 'r') as a:
#   bot_config = json.load(a)
#
# # задаем функции обработки данных
# def get_intent_by_model(text):
#   return clf.predict(vectorizer.transform([text]))[0]
#
# # ...
# X = []
# y = []
# for intent in bot_config['intents']:
#   for example in bot_config['intents'][intent]['examples']:
#     X.append(example)
#     y.append(intent)
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # применяем векторзайзер
# # ngram_range=(1, 3), analyzer='char_wb', min_df=5
# # vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='char_wb', min_df=5)
# vectorizer = CountVectorizer(ngram_range=(1, 3), analyzer='char_wb', min_df=5)
# X_train_vectorized = vectorizer.fit_transform(X_train)
# X_test_vectorized = vectorizer.transform(X_test)
#
# # vectorizer.get_feature_names()
#
# # применяем классифаер
# clf = RandomForestClassifier()
# # clf = LogisticRegression()
# clf.fit(X_train_vectorized, y_train)
#
# # проверяем точность модели
# print(clf.score(X_train_vectorized, y_train))
# print(clf.score(X_test_vectorized, y_test))
# # print(clf.predict(vectorizer.transform(['хай'])))
#
# def bot(text):
#   intent = get_intent_by_model(text)
#   return random.choice(bot_config['intents'][intent]['responses'])

# запуск основного цикла программы в самом коде для проверки работы
# while True:
#   input_text = input()
#   if input_text != 'exit':
#     response = bot(input_text)
#     print(response)
#   else:
#     break
