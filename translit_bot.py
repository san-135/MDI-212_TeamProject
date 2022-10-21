import telebot, logging
from input_testing import letters_transform

bot = telebot.TeleBot('5704603308:AAHVM2f5_BGKg94-jbQbKxZX9rSVk2LeYyo')  # https://t.me/TranslitRUENbot

logging.basicConfig(filename='bot.log')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.from_user.id)
    print(f'Message received from {message.from_user.id}: {message.text}')


"""
Required python packages: telebot, pyTelegramBotAPI
"""


@bot.message_handler(content_types=['text'])
def command_handling(message):
    print(f'User {message.from_user.id}: {message.text}')
    if message.text == "/start":
        # send greetings
        logging.info('Bot status: Active')
        bot.send_message(message.from_user.id, "Привет, я переделываю сообщения в другую раскладку. "
                                               "Напиши /help и я расскажу поподробнее")
        # log the message to python console
        print(f'Answer to {message.from_user.id}: "Привет, я переделываю сообщения в другую раскладку. "'
              f'"Напиши /help и я расскажу поподробнее"')
        return("Привет, я переделываю сообщения в другую раскладку. "
                                               "Напиши /help и я расскажу поподробнее")

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
        return ('Присылай любое сообщение чтобы я его переделал в другую раскладку\n'
              f'Из русской в английскую или наоборот я определяю по первой букве. Поэтому если напишешь одно сообщение '
              f'на разных раскладках, вряд ли я выведу точно то, что ты ожидаешь')

    elif message.text == '/halloween':
        bot.send_message(message.from_user.id, '👻')
        bot.send_message(message.from_user.id, 'Бугагашенька')
        print(f'Answer to {message.from_user.id}: 👻 Бугагашенька')

    else:
        # reply with the changed message
        logging.info(message.from_user.id, letters_transform(user_input=message.text))
        bot.send_message(message.from_user.id, letters_transform(user_input=message.text))

        # log the message to python console
        print(f'Answer to {message.from_user.id}: {letters_transform(user_input=message.text)}')
        return letters_transform(user_input=message.text)


def lang_en(message):
    # reply with the changed text
    bot.send_message(message.from_user.id, letters_transform(user_input=message.text, lang='en'))
    # log the message to python console
    print(f"Answer to {message.from_user.id}: {letters_transform(user_input=message.text, lang='en')}")


bot.polling(none_stop=True, interval=0)

bot.enable_save_next_step_handlers(delay=1)
bot.load_next_step_handlers()

bot.polling(none_stop=True, interval=1)
