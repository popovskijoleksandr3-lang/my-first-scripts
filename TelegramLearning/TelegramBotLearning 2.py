import telebot
Bot = telebot.TeleBot(token='')
@Bot.message_handler(commands=['start', 'Start'])
def send_welcome(message):
    Bot.reply_to(message, 'Hello, my name is Alex_Bot')
@Bot.message_handler(commands=['Info', 'info'])
def information_about(message):
    Bot.reply_to(message, 'I am the telegram bot made by telebot')
# Це всеїдне вухо, яке ігнорує команди
@Bot.message_handler(func=lambda message: not message.text.startswith('/'))
def reply_message(message):
    Bot.reply_to(message, 'Currently i cant reply you')
Bot.infinity_polling()