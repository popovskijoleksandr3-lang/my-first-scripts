import telebot
import requests
Token = ''
Bot = telebot.TeleBot(Token)
url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
@Bot.message_handler(commands=['start', 'Start'])
def welcome(message):
    Bot.reply_to(message, "Привіт! Напиши /rate USD, щоб дізнатися курс.")
@Bot.message_handler(commands=['rate'])
def get_rate(message):
    list = message.text.split()
    if len(list) < 2:
        return Bot.reply_to(message, "Вкажи валюту (напр. /rate USD)")
    data = requests.get(url).json()
    for i in data:
        if i['cc'] == list[1].upper():
            return Bot.reply_to(message, f"{i['cc']}: {i['rate']} грн")
    Bot.reply_to(message, "Не знайдено")
@Bot.message_handler(func=lambda message: True)
def echo(message):
    Bot.reply_to(message, "Я не розумію. Напиши /rate USD або /start")
Bot.infinity_polling()