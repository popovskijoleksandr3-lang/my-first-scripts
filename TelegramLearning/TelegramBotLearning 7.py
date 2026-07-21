import telebot
import requests
url = "https://catfact.ninja/fact"
Token = ''
bot = telebot.TeleBot(Token)
@bot.message_handler(commands=['fact'])
def fact(message):
        response = requests.get(url)
        data = response.json()
        bot.send_message(message.chat.id, data['fact'])
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Hello")
bot.infinity_polling()