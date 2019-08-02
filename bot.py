import telebot
#from __future__ import unicode_literals
import glob 
import os

bot = telebot.TeleBot('897290392:AAFz99BO_5zwD-CRvRAAejqyQGWx0R56x0c')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u'Olá, bem-vindo ao bot!')

@bot.message_handler(commands=['baixar'])
def responde(message):
    m = message.text.split()
    chat_id = message.chat.id
    bot.reply_to(message, 'Baixando...')
    saida = 1
    os.system('youtube-dl {} -o video'.format(m[1]))
    bot.reply_to(message, 'Arquivo baixado com sucesso!')
    video = open('video.mkv', 'rb')
    if video:
        bot.send_video(chat_id, video)
        os.system('rm $(ls | grep *video.*)')
    else:
        video = open('video.mp4', 'rb')
        bot.send_video(chat_id, video)
        os.system('rm $(ls | grep *video.*)')

bot.polling()
