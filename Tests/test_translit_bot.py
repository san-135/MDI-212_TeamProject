# import os
import telebot
from telebot import apihelper, TeleBot, util
from translit_bot import get_text_messages
from unittest import TestCase, main

tb = TeleBot("test")
user = telebot.types.User(id=467581205, is_bot=False, last_name='Bot', first_name='Petr')
chat = telebot.types.Chat(id=123, type='private')
message = telebot.types.Message(from_user=user, message_id=123, date=123, chat=chat, content_type='text',
                                json_string=123, options=[])


class TestBot(TestCase):
    def test_ruen(self):
        message.text = 'Xt,egtkkb'
        self.assertEqual(get_text_messages(message), 'Чебупелли')

    def test_enru(self):
        message.text = 'Мфяудштщмщу иуягьшу!!!'
        self.assertEqual(get_text_messages(message), 'Vazelinovoe bezumie!!!')

    def test_help(self):
        message.text = '/help'
        self.assertEqual(get_text_messages(message), 'Присылай любое сообщение чтобы я его переделал в другую раскладку\n'
              f'Из русской в английскую или наоборот я определяю по первой букве. Поэтому если напишешь одно сообщение '
              f'на разных раскладках, вряд ли я выведу точно то, что ты ожидаешь')

    def test_start(self):
        message.text = '/start'
        self.assertEqual(get_text_messages(message), "Привет, я переделываю сообщения в другую раскладку. "
                                               "Напиши /help и я расскажу поподробнее")


if __name__ == '__main__':
    main()
