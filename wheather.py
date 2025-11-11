import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

OWM_API_KEY = os.getenv("OWM_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Параметры запроса к API
    params = {
        "q": city,           # название города
        "appid": "e7c6574b6a0b73055da44a03f7f58a98",    # твой ключ
        "units": "metric",   # измерения в градусах Цельсия
        "lang": "ru"         # язык ответов — русский
    }

    # Отправляем запрос к серверу
    response = requests.get(BASE_URL, params=params)

    # Если сервер ответил ошибкой (например, город не найден)
    if response.status_code != 200:
        print("Ошибка! Проверьте название города или ключ.")
        return None

    # Преобразуем ответ в формат Python (словарь)
    data = response.json()

    weather_info = {
        "город": data["name"],
        "страна": data["sys"]["country"],
        "температура": data["main"]["temp"],
        "ощущается": data["main"]["feels_like"],
        "описание": data["weather"][0]["description"],
        "влажность": data["main"]["humidity"],
        "ветер": data["wind"]["speed"]
    }

    return weather_info

def show_weather(info):
    print("\n===============================")
    print(f"🌍 Погода в {info['город']}, {info['страна']}")
    print(f"🌡 Температура: {info['температура']} °C (ощущается как {info['ощущается']} °C)")
    print(f"🌦 Описание: {info['описание'].capitalize()}")
    print(f"💧 Влажность: {info['влажность']}%")
    print(f"💨 Ветер: {info['ветер']} м/с")
    print("===============================")

def main():
    print("Программа для получения текущей погоды.")
    
    while True:
        city = input("\nВведите название города (или 'выход(exit)' для завершения): ")
        if city.lower() == 'exit' or city.lower() == 'выход':
            print("Завершение программы. До свидания!")
            break

        weather_info = get_weather(city)
        if weather_info:
            show_weather(weather_info)

if __name__ == "__main__":
    main()