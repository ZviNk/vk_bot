from commands import CommandManager
from config import VK_API_TOKEN, GROUP_ID
from vk_api import VkApi
from utils.vk_utils import get_updates


class VkBot:
    def __init__(self):
        """
        Инициализация бота. Подключение к VK API.
        """
        self.vk = VkApi(token=VK_API_TOKEN)  # Создаем объект для работы с VK API
        self.group_id = GROUP_ID  # ID вашей группы
        self.command_manager = CommandManager()  # Менеджер команд

    async def handle_event(self, event: dict):
        """
        Обработка входящего события от VK.
        В зависимости от текста сообщения вызывает соответствующую команду.
        """
        message = event.get('object', {}).get('message', {}).get('text', '').strip().lower()

        if message:
            command = self.command_manager.get_command(message)
            if command:
                return await command.execute(event)  # Выполнение команды
            else:
                return await self.handle_unknown_command(event)
        return {"status": "ok"}

    async def handle_unknown_command(self, event: dict):
        """
        Обработка неизвестных команд.
        """
        return {
            "response": "Команда не распознана. Попробуйте использовать 'help' для списка доступных команд."
        }


vk_bot = VkBot()
