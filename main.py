from fastapi import FastAPI
from app.bot import vk_bot
from app.commands import register_commands

app = FastAPI()

# Регистрируем команды при старте приложения
register_commands()

@app.post("/webhook/")
async def vk_webhook(event: dict):
    """
    Обрабатываем входящие события от VK.
    """
    response = await vk_bot.handle_event(event)
    return response
