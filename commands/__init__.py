from app.commands.command_manager import CommandManager
from app.commands.help import HelpCommand
from app.commands.weather import WeatherCommand
from app.commands.echo import EchoCommand

command_manager = CommandManager()

def register_commands():
    """
    Регистрация всех доступных команд.
    """
    command_manager.register(HelpCommand())
    command_manager.register(WeatherCommand())
    command_manager.register(EchoCommand())
