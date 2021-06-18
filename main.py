import os
import telebot

API_KEY = os.getenv('TeleBot_API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands=['Char'])
def greet(message):
	message_parsed = message.text.split()
	for param in message_parsed:
		bot.send_message(message.chat.id, param) 

bot.polling()  
