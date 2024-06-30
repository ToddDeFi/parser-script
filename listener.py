import asyncio
from telethon import TelegramClient, events

# Конфигурация
api_id = '25382442'
api_hash = 'b319175cafe56fff3396211f3a143bc7'
phone = '+48571845635'

# Список каналов
channels = ['@script_for_misha', '@another_channel']
my_chat_id = '@script_for_misha_2'

# Словарь для фильтрации сообщений (ключевые слова)
filter_keywords = [
    'dollar',
    'bitcoin',
]

# Инициализация клиента
client = TelegramClient(phone, api_id, api_hash)

# Обработчик новых сообщений
@client.on(events.NewMessage(chats=channels))
async def handler(event):
    message_text = event.message.text
    if message_text:
        message_text_lower = message_text.lower()
        for keyword in filter_keywords:
            if keyword.lower() in message_text_lower:
                await client.send_message(my_chat_id, message_text)
                break

# Основная функция
async def main():
    await client.start()
    print("Client started")
    await client.run_until_disconnected()

# Запуск клиента
if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
