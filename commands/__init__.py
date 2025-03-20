from commands.command_manager import CommandManager
from commands.help import HelpCommand
from commands.weather import WeatherCommand
from commands.echo import EchoCommand

command_manager = CommandManager()

def register_commands():
    """
    Регистрация всех доступных команд.
    """
    command_manager.register(HelpCommand())
    command_manager.register(WeatherCommand())
    command_manager.register(EchoCommand())
