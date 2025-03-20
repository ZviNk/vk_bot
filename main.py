import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import hashlib
import hmac
import json
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем секретный ключ из переменных окружения
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

# Модель для уведомлений от VK
class VkNotification(BaseModel):
    type: str
    group_id: int
    secret_key: str
    object: dict  # Уведомление с объектом, например, сообщение

# Обработчик вебхуков (и подтверждение, и уведомления)
@app.post("/webhook")
async def webhook(request: Request, notification: VkNotification):
    # Получаем тело запроса
    body = await request.json()

    # Если тип запроса "confirmation", подтверждаем вебхук
    if body.get("type") == "confirmation":
        return JSONResponse(content="0a37b2da")

    # Проверка секретного ключа для других типов уведомлений
    if body.get("secret_key") != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid secret key")

    # Обработка уведомлений
    if body.get("type") == "message_new":
        # Пример обработки нового сообщения
        return JSONResponse(content={"status": "Message received"})
    else:
        return JSONResponse(content={"status": "Unsupported notification type"})

# Актуатор для отслеживания работы API
@app.get("/health")
async def health():
    return {"status": "ok"}
