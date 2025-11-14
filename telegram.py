# Сервер на Python (Flask) + библиотека python-telegram-bot
from flask import Flask, request
import requests

app = Flask(name)
TELEGRAM_BOT_TOKEN = "6797987896768446ewtdfgssdhsdfgh"

# Отправка сообщения в Telegram
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    chat_id = data['chat_id']
    text = data['text']
    
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text}
    )
    return "Сообщение отправлено!"

# Получение сообщений (вебхук)
@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.json
    if 'message' in update:
        handle_message(update['message'])
    return "OK"

def handle_message(message):
    # Логика обработки входящих сообщений
    print(f"Получено сообщение: {message['text']}")