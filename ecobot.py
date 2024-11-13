import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os

TOKEN = ''
   
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Здравствуй!')
    bot.reply_to(message, message.text)

bot.polling()
