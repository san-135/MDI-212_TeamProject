import telebot
from input_testing import letters_transform
bot = telebot.TeleBot('5704603308:AAHVM2f5_BGKg94-jbQbKxZX9rSVk2LeYyo')  # https://t.me/TranslitRUENbot

"""
Required python packages: telebot, pyTelegramBotAPI
"""


@bot.message_handler(commands=['/start', '/help', '/ru', '/en'])
def command_handling(message):
    print(f'User {message.from_user.id}: {message.text}')
    if message.text == "/start":
        # send greetings
        bot.send_message(message.from_user.id, "Привет, я переделываю сообщения в другую раскладку. "
                                               "Напиши /help и я расскажу поподробнее")
        # log the message to python console
        print(f'Answer to {message.from_user.id}: Привет, я переделываю сообщения в другую раскладку. '
              f'Напиши /help и я расскажу поподробнее')

    elif message.text == "/help":
        # show bot description
        bot.send_message(message.from_user.id, "Присылай любое сообщение чтобы я его переделал в другую раскладку\n"
                         "Но сначала уточни пожалуйста, нужно из русской в английскую раскладку /en или наоборот /ru ?")
        # log the message to python console
        print(f'Answer to {message.from_user.id}: Присылай любое сообщение чтобы я его переделал в другую раскладку\n'
              f'Но сначала уточни пожалуйста, нужно из русской в английскую раскладку /en или наоборот /ru ?')

    elif message.text == '/ru':
        bot.register_next_step_handler(message=bot.reply_to(message, 'Кидай текст в английской раскладке!'),
                                       callback=lang_ru)
        print(f'Answer to {message.from_user.id}: Кидай текст в английской раскладке!')

    elif message.text == '/en':
        bot.register_next_step_handler(message=bot.reply_to(message, 'Кидай текст в русской раскладке!'),
                                       callback=lang_en)
        print(f'Answer to {message.from_user.id}: Кидай текст в русской раскладке!')

    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, выберите конечную раскладку:\n/ru Русская\n/en Английская')
        print(f'Answer to {message.from_user.id}: Пожалуйста, выберите конечную раскладку:\n'
              f'/ru Русская\n/en Английская')


def lang_ru(message):
    # reply with the changed text
    bot.send_message(message.from_user.id, letters_transform(user_input=message.text, lang='ru'))
    # log the message to python console
    print(f"Answer to {message.from_user.id}: {letters_transform(user_input=message.text, lang='ru')}")


def lang_en(message):
    # reply with the changed text
    bot.send_message(message.from_user.id, letters_transform(user_input=message.text, lang='en'))
    # log the message to python console
    print(f"Answer to {message.from_user.id}: {letters_transform(user_input=message.text, lang='en')}")


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.infinity_polling()
