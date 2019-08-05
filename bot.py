#!/usr/bin/python3
import telebot
#from __future__ import unicode_literals
import glob 
import os
from time import sleep
bot = telebot.TeleBot('897290392:AAHsSCgmj1Djm_8P2KfEss5J4N-d9t0Wj4g')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u'Olá, bem-vindo ao bot!')

@bot.message_handler(commands=['baixar'])
def responde(message):
    m = message.text.split()
    chat_id = message.chat.id
    bot.reply_to(message, 'Baixando...')
    try:
        os.system('tmux new-session \'youtube-dl {} -o {}\''.format(m[1], chat_id))
        bot.reply_to(message, 'Por favor, aguarde 5 segundos...')
        sleep(5)
        video = open('{}.mkv'.format(chat_id), 'rb')
        bot.send_video(chat_id, video)
        os.system('rm {}.mkv'.format(chat_id))
    except:
        bot.reply_to(message, 'Ocorreu um erro!')

bot.polling()
