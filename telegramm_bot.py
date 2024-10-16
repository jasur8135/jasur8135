# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:32:14 2024

@author: laptop
"""

my_token='7985443957:AAHDRXTEw91UM_7tK4dwqrNvjzVmjEIJB-Q'
#my_bot_link=https://t.me/Jasurbek_Maxammadjonov_bot
import telebot
bot=telebot.Telebot(my_token,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'salom ishlar qalay')
    
@bot.message_handler(func=lambda m:True)
def echo_all(xabar):
    bot.reply_to(xabar,xabar.text)
    
bot.polling()
