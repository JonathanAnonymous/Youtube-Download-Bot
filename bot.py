import telebot
#from __future__ import unicode_literals
import glob 
import os
from time import sleep
bot = telebot.TeleBot('897290392:AAFz99BO_5zwD-CRvRAAejqyQGWx0R56x0c')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u'Olá, bem-vindo ao bot!')

@bot.message_handler(commands=['baixar'])
def responde(message):
    m = message.text.split()
    chat_id = message.chat.id
    bot.reply_to(message, 'Baixando...')
    os.system('tmux new-session \'youtube-dl {} -o {}\''.format(m[1], chat_id))
    bot.reply_to(message, 'Por favor, aguarde 5 segundos...')
    sleep(5)
    video = open('{}.mkv'.format(chat_id), 'rb')
    bot.send_video(chat_id, video)

@bot.message_handler(commands=['poweroff'])
def desligar(message):
    os.system('poweroff')

bot.polling()
