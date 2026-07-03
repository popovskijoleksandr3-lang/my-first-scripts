import requests
import telebot
url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
Token = ''
bot = telebot.TeleBot(Token)
@bot.message_handler(commands=['Start', 'start'])
def welcome_message(message):
    bot.reply_to(message, 'Currently I have commands like /USD_in_UAH and /EUR_in_UAH')
@bot.message_handler(commands=['USD_in_UAH'])
def send_usd(message):
    response = requests.get(url)
    data = response.json()
    for item in data:
        if item["cc"] == "USD":
            text = f"USD rate: {item['rate']} UAH"
            bot.reply_to(message, text)
@bot.message_handler(commands=['EUR_in_UAH'])
def send_eur(message):
    response = requests.get(url)
    data = response.json()
    for item in data:
        if item["cc"] == "EUR":
            text = f"EUR rate: {item['rate']} UAH"
            bot.reply_to(message, text)
bot.infinity_polling()