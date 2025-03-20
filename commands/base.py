from abc import ABC, abstractmethod

class BaseCommand(ABC):
    def __init__(self, trigger: str):
        self.trigger = trigger

    @abstractmethod
    async def execute(self, event: dict) -> dict:
        pass
