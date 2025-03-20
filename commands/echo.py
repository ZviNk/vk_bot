from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    """
    Команда для повторения текста.
    """
    def __init__(self):
        super().__init__(trigger="echo")

    async def execute(self, event: dict) -> dict:
        """
        Повторяет введенное сообщение.
        """
        message = event.get('object', {}).get('message', {}).get('text', '')
        return {"response": message}
