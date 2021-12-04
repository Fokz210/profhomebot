import telebot
from telebot import types

import botconfig
import handlers

bot = telebot.TeleBot(botconfig.token)


@bot.message_handler(commands=['start', 'help'])
def welcome(message: types.Message):
    handlers.welcome(bot, message)


@bot.message_handler(func=lambda m: True)
def question(message: types.Message):
    handlers.question(bot, message)


if __name__ == '__main__':
    bot.infinity_polling()
