import telebot
from input_testing import letters_transform
bot = telebot.TeleBot('5704603308:AAHVM2f5_BGKg94-jbQbKxZX9rSVk2LeYyo')  # https://t.me/TranslitRUENbot


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(f'User {message.from_user.id}: {message.text}')
    if message.text == "/start":
        # send greetings
        bot.send_message(message.from_user.id, "Привет, я переделываю сообщения в другую раскладку. "
                                               "Напиши /help и я расскажу поподробнее")
        # log the message to python console
        print(f'Answer to {message.from_user.id}: "Привет, я переделываю сообщения в другую раскладку. "'
              f'"Напиши /help и я расскажу поподробнее"')

    elif message.text == "/help":
        # show bot description
        bot.send_message(message.from_user.id, "Присылай любое сообщение чтобы я его переделал в другую "
                         "раскладку\nПеревожу из русской в английскую раскладку и наоборот. Работает для традиционной "
                         "раскладки ПК, на Mac обычно всё кроме 'ё' и некоторых символов в других местах(")
        # log the message to python console
        print(f'Answer to {message.from_user.id}: Присылай любое сообщение чтобы я его переделал в другую раскладку\n'
              f'Перевожу из русской в английскую раскладку и наоборот. Работает для традиционной раскладки ПК, '
              f"на Mac обычно всё кроме 'ё' и некоторых символов в других местах(")

    else:
        # reply with the changed text
        bot.send_message(message.from_user.id, letters_transform(user_input=message.text))

        # log the message to python console
        print(f'Answer to {message.from_user.id}: {letters_transform(user_input=message.text)}')


bot.polling(none_stop=True, interval=0)
