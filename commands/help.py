from commands.base import BaseCommand

class HelpCommand(BaseCommand):
    """
    Команда для вывода справки по доступным командам.
    """
    def __init__(self):
        super().__init__(trigger="help")

    async def execute(self, event: dict) -> dict:
        """
        Выводит список всех доступных команд.
        """
        available_commands = "\n".join(f"/{cmd}" for cmd in self.command_manager.get_all_commands())
        return {
            "response": f"Доступные команды:\n{available_commands}"
        }
