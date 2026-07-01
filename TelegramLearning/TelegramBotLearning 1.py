import telebot
Bot = telebot.TeleBot(token='')
@Bot.message_handler(commands=['start'])
def send_welcome(message):
    Bot.reply_to(message, "Hello, I'm Telegram Bot Learning 1")
@Bot.message_handler(func=lambda message: True)
def echo_all(message):
    Bot.reply_to(message, "I received your message:  " + message.text)
Bot.infinity_polling()