# https://habr.com/ru/post/442800/

import telebot
from input_testing import letters_transform
# bot = telebot.TeleBot('5736580585:AAHTmzjKZTfukU3eKt4FdQJEQs1zsKhB3aU')
bot = telebot.TeleBot('5704603308:AAHVM2f5_BGKg94-jbQbKxZX9rSVk2LeYyo')   # https://t.me/TranslitRUENbot


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        print(f'{message.from_user.id}: {message.text}')
        bot.send_message(message.from_user.id, "Привет, я переделываю сообщения в другую раскладку. "
                                               "Напиши /help и я расскажу поподробнее")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Присылай любое сообщение чтобы я его переделал в другую раскладку\n"
                                               "Из русской в английскую или наоборот я определяю по первой букве. "
                                               "Поэтому если напишешь одно сообщение на разных раскладках, вряд ли"
                                               " я выведу точно то, что ты ожидаешь")

    else:
        bot.send_message(message.from_user.id, letters_transform(user_input=message.text))


bot.polling(none_stop=True, interval=0)
