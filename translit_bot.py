import telebot
from input_testing import letters_transform
bot = telebot.TeleBot('5704603308:AAHVM2f5_BGKg94-jbQbKxZX9rSVk2LeYyo')  # https://t.me/TranslitRUENbot


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(f'Message received from {message.from_user.id}: {message.text}')
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
                         "раскладку\nИз русской в английскую переводить или наоборот - я определяю "
                         "по первой букве. Поэтому если напишешь первый символ которого нет в моей базе (например, "
                         "'!' или число, вряд ли я выведу то, что ты ожидаешь")
        # log the message to python console
        print(f'Answer to {message.from_user.id}: "Присылай любое сообщение чтобы я его переделал в другую раскладку\n'
              f'Из русской в английскую или наоборот я определяю по первой букве. Поэтому если напишешь одно сообщение '
              f'на разных раскладках, вряд ли я выведу точно то, что ты ожидаешь"')

    else:
        # reply with the changed message
        bot.send_message(message.from_user.id, letters_transform(user_input=message.text))

        # log the message to python console
        print(f'Answer to {message.from_user.id}: {letters_transform(user_input=message.text)}')


bot.polling(none_stop=True, interval=0)
