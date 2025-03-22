import vk_api
import logging
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
import os

from commands import start, help

load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    longpoll = VkLongPoll(vk_session)

    logger.info("Бот запущен")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            logger.info(f"Новое сообщение от {event.user_id}: {event.text}")

            # Обработка команды
            if event.text.lower() == "/start":
                start.handle(event, vk_session)
            elif event.text.lower() == "/help":
                help.handle(event, vk_session)
            else:
                vk_session.method('messages.send', {
                    'user_id': event.user_id,
                    'message': 'Неизвестная команда. Введите /help для помощи.',
                    'random_id': 0
                })

if __name__ == '__main__':
    main()
