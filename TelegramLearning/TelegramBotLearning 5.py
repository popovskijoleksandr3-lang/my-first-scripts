import telebot

Bot = telebot.TeleBot('')

@Bot.message_handler(commands=['start'])
def welcome(message):
    Bot.reply_to(message, "Привіт! Напиши мені приклад, наприклад: 2 + 2 або 10 * 5")

@Bot.message_handler(func=lambda message: True)
def calculator(message):
    try:
        # eval() автоматично рахує математичний вираз
        result = eval(message.text)
        Bot.reply_to(message, f"Результат: {result}")
    except:
        Bot.reply_to(message, "Я не розумію. Напиши приклад цифрами (наприклад: 5 * 5)")

Bot.infinity_polling()