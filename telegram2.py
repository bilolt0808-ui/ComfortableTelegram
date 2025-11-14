# Сервер на Python + Telethon
from telethon import TelegramClient, events
import asyncio

api_id = '68479494349468saf6ASDGF'
api_hash = '74567687978768768217368127368127361234325'
phone = '+998-93-398-08-08'

client = TelegramClient('session_name', api_id, api_hash)

# Событие для входящих сообщений
@client.on(events.NewMessage)
async def handler(event):
    print(f"Получено сообщение: {event.text}")
    # Пересылка в ваше приложение через WebSocket или HTTP

async def send_message(recipient, text):
    await client.send_message(recipient, text)

client.start()
client.run_until_disconnected()