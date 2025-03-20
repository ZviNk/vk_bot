from app.commands.base import BaseCommand
import requests

class WeatherCommand(BaseCommand):
    """
    Команда для получения информации о погоде.
    """
    def __init__(self):
        super().__init__(trigger="weather")

    async def execute(self, event: dict) -> dict:
        """
        Получает данные о текущей погоде.
        """
        city = "Moscow"  # Здесь можно использовать данные из сообщения
        api_key = "YOUR_WEATHER_API_KEY"  # Вставьте свой API ключ
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url).json()

        if response.get("cod") != 200:
            return {"response": "Не удалось получить информацию о погоде."}

        temp = response['main']['temp']
        description = response['weather'][0]['description']
        return {
            "response": f"Погода в {city}: {temp}°C, {description}"
        }
