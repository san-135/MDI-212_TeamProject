# https://habr.com/ru/post/442800/

import telebot
from input_testing import letters_transform
# bot = telebot.TeleBot('5736580585:AAHTmzjKZTfukU3eKt4FdQJEQs1zsKhB3aU')
bot = telebot.TeleBot('5704603308:AAHVM2f5_BGKg94-jbQbKxZX9rSVk2LeYyo')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я переделываю сообщения из латинской в русскую раскладку")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Сообщение должно быть на латинской раскладке. "
                                               "Пришли его мне и я его переделаю")
    else:
        bot.send_message(message.from_user.id, letters_transform(user_input=message.text))


bot.polling(none_stop=True, interval=0)
