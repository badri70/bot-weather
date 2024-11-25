import aiohttp
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')

async def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                weather_text = (
                    f"🌍 Город: {city.title()}\n"
                    f"🌡 Температура: {temperature}°C\n"
                    f"💧 Влажность: {humidity}%\n"
                    f"🌬 Ветер: {wind_speed} м/с\n"
                    f"☁️ Описание: {weather_description.capitalize()}"
                )
                return weather_text
            else:
                return (
                    "К сожалению, я не смог найти погоду для этого города. "
                    "Пожалуйста, проверьте название и попробуйте снова."
                )


async def get_weather_forecast(city_name: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&lang=ru&appid={API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:  # Если запрос успешный
                data = await response.json()

                forecast_text = f"Прогноз погоды на 5 дней для города {city_name}:\n"

                for item in data['list']:
                    dt = item['dt_txt']  # Дата и время прогноза
                    temperature = item['main']['temp']  # Температура
                    weather_description = item['weather'][0]['description']  # Описание погоды

                    forecast_text += (
                        f"\nДата и время: {dt}\n"
                        f"🌡 Температура: {temperature}°C\n"
                        f"☁️ Описание: {weather_description.capitalize()}\n"
                    )

                return forecast_text
            else:
                return (
                    "К сожалению, я не смог получить прогноз погоды для этого города. "
                    "Пожалуйста, проверьте название и попробуйте снова."
                )
