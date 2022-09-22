import telebot
from telebot import types
import surrogates
import os
import shutil
x = surrogates.decode('\ud83e\udde0')
import datetime
import time

now = datetime.datetime.now()


classes = ["11",
           "10 А","10 Б",
           "9 А","9 Б",
           "8 А","8 Б","8 В",
           "7 А","7 Б","7 В",
           "6 А","6 Б","я учитель","я админ"
           ]

bot = telebot.TeleBot('5655411900:AAFDh-2Raq114LAf4QqwTQhvTzbBadEUGN0')

usersId = 1253115796  # 765843635 #замени на свой айди

@bot.message_handler(commands=["what"])
def what(message, res=False):
    bot.send_message(message.chat.id, 'Привет ' + message.chat.first_name + '!\n' + 'Часто было такое, что расписание просто вылетило из головы?🤔'
                                                                                    'Этот бот подскажет какой урок и кабинет у твоего класса', )
@bot.message_handler(commands=["salam"])
def salam(message, res=False):
    bot.delete_message(message.chat.id, message.message_id)
    markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к оплате", url="https://t.me/+qzHXH4Z0OJs4OGIy")
    markup.add(url_button)
    bot.send_message(message.chat.id, 'Ахах, кто-то новенький узнал про секрет бота.' + '\n' + 'Вот группа, только тсс 🤐! ', reply_markup=markup)

@bot.message_handler(commands=["start"])
def salam(message, res=False):
    bot.send_message(message.chat.id, 'Нажми на синие меню', )


@bot.message_handler(commands=["class"])
def admin(message):
    global classes
    keyboard = types.InlineKeyboardMarkup()
    button_list = [types.InlineKeyboardButton(text=x, callback_data=x) for x in classes]
    keyboard.add(*button_list)
    bot.send_message(message.chat.id, 'Выбери свой класс', reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def handle_text(message, res=False):
    if message.text.strip() == 'Кто же твой создатель?' or 'Кто создатель?':
        bot.send_message(message.chat.id, 'Меня создал Сарачинский Артем',)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
     if call.data == "11":
         if now.weekday() == 0:
             photo = open('classes/'+str(call.data) + "/" + str(now.weekday())+".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса", )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
            photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
            bot.send_message(call.message.chat.id, 'Вот расписание для вторника у  ' + str(call.data) + " класса", )
            bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
            photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
            bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса", )
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
            bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса", )
            photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
            bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
            photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
            bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса", )
            bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать',)


     elif call.data == "10 Б":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )


     elif call.data == "10 А":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )


     elif call.data == "9 Б":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для средыу' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )

     elif call.data == "9 А":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )


     elif call.data == "8 Б":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )

     elif call.data == "8 А":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )

     elif call.data == "8 В":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )

     elif call.data == "7 Б":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )

     elif call.data == "7 А":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )

     elif call.data == "7 В":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )

     elif call.data == "6 Б":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )

     elif call.data == "6 А":
         if now.weekday() == 0:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для понедельника у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 1:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для вторника у  ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 2:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для среды у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
             bot.send_message(call.message.chat.id, 'не забудь что инф час смещяет расписание на 30 минут', )
         elif now.weekday() == 3:
             bot.send_message(call.message.chat.id, 'Вот расписание для четверга у ' + str(call.data) + " класса" )
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_photo(call.message.chat.id, photo)
         elif now.weekday() == 4:
             photo = open('classes/' + str(call.data) + "/" + str(now.weekday()) + ".JPG", 'rb')
             bot.send_message(call.message.chat.id, 'Вот расписание для пятницы у ' + str(call.data) + " класса" )
             bot.send_photo(call.message.chat.id, photo)
         else:
             bot.send_message(call.message.chat.id, 'Можешь спать', )


     elif call.data == "я учитель":
          bot.send_message(call.message.chat.id, 'Этот раздел в дороботке', )

     elif call.data == "я админ":
         photo = open("nn.jpg", 'rb')
         bot.send_message(call.message.chat.id, 'ты точно не админ', )
         bot.send_photo(call.message.chat.id, photo)


     else:
         bot.send_message(call.message.chat.id, 'Мне не понятно, что ты от меня хочешь',)

        # bot.send_message(call.message.chat.id, "Так, значит смотрим " + (call.data),reply_markup=markup)
        # clas = call.data





bot.polling(none_stop=True, interval=0)