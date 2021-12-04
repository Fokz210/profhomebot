import telebot
from telebot import types
import random

choices = [
    'Бесспорно',
    'Предрешено',
    'Никаких сомнений',
    'Определенно да',
    'Можешь быть уверен в этом',

    'Мне кажется, да',
    'Вероятнее всего',
    'Хорошие перспективы',
    'Знаки говорят - да',
    'Да',

    'Пока не ясно, попробуй еще',
    'Спроси позже',
    'Лучше не рассказывать',
    'Сейчас не стоит предсказывать',
    'Сконцентрируйся и спроси опять',

    'Даже не думай',
    'Мой ответ - нет',
    'По моим данным, нет',
    'Перспективы не очень красочные',
    'Весьма сомнительно'
]

welcome_message = 'Просто спроси)'


def welcome(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, welcome_message)


def question(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, random.choice(choices))


def default(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, 'Хватит троллить, это не вопрос((((')
