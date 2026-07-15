import telebot
import sqlite3
from datetime import datetime
conn = sqlite3.connect('notes', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT, time TEXT)')
conn.commit()
Bot = telebot.TeleBot('')
@Bot.message_handler(commands=['show'])
def show_notes(message):
    cursor.execute('SELECT text, time FROM notes')
    all_notes = cursor.fetchall()
    if not all_notes:
        Bot.reply_to(message, "Заміток поки немає.")
    else:
        response = "Твої замітки:"
        for note in all_notes:
            response += f"{note[0]} ({note[1]})"
        Bot.reply_to(message, response)
@Bot.message_handler(func=lambda message: True)
def save_note(message):
    if message.text.startswith('/'):  # Ігноруємо команди
        return
    now = datetime.now().strftime("%d.%m %H:%M")
    cursor.execute('INSERT INTO notes (text, time) VALUES (?, ?)', (message.text, now))
    conn.commit()
    Bot.reply_to(message, "Записано!")
Bot.infinity_polling()