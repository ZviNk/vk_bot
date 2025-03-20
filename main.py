import os
import h11
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
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

# Обработчик вебхуков (и подтверждение, и уведомления)
@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()

    # Если тип запроса "confirmation", сразу возвращаем ответ
    if body.get("type") == "confirmation":
        return PlainTextResponse("0a37b2da")

    # Для остальных типов выполняем валидацию через модель
    notification = VkNotification.parse_obj(body)

    # Здесь можно добавить проверку secret_key и дальнейшую обработку уведомления
    if notification.secret_key != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid secret key")

    if notification.type == "message_new":
        return JSONResponse(content={"status": "Message received"})
    else:
        return JSONResponse(content={"status": "Unsupported notification type"})

# Актуатор для отслеживания работы API
@app.get("/health")
async def health():
    return {"status": "ok"}
