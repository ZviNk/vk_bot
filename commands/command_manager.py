from typing import List
from commands.base import BaseCommand

class CommandManager:
    def __init__(self):
        """
        Менеджер команд. Хранит и управляет доступными командами.
        """
        self.commands = {}

    def register(self, command: BaseCommand):
        """
        Регистрирует команду.
        """
        self.commands[command.trigger.lower()] = command

    def get_command(self, trigger: str) -> BaseCommand:
        """
        Возвращает команду по ее ключу (триггеру).
        """
        return self.commands.get(trigger.lower())

    def get_all_commands(self) -> List[str]:
        """
        Возвращает список всех доступных команд.
        """
        return list(self.commands.keys())
