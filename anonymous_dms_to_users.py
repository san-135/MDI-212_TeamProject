import telebot
from unittest import TestCase
bot = telebot.TeleBot('5765608273:AAHZ7gIWuGttGJ-0Ch7J6C0W_v_bEt7Pw_0')
# 5765608273:AAHZ7gIWuGttGJ-0Ch7J6C0W_v_bEt7Pw_0
# 5704603308:AAHVM2f5_BGKg94-jbQbKxZX9rSVk2LeYyo


class TestSendMessage(TestCase):
    def test_san_135(self) -> None:
        a = input()
        bot.send_message(int('689585726'), a)

        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            print(f'{message.from_user.id}: {message.text}')
            a = input()
            bot.send_message(int('689585726'), a)

        bot.polling(none_stop=True, interval=0)

    def test_T_Shelby(self) -> None:
        a = input()
        bot.send_message(int('1840388068'), a)

        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            print(f'{message.from_user.id}: {message.text}')
            a = input()
            bot.send_message(int('1840388068'), a)

        bot.polling(none_stop=True, interval=0)

