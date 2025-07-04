import requests
import os

from dotenv import load_dotenv

from utils.geolocation import coordinates


load_dotenv()

API_KEY = os.environ.get("API_KEY")


async def get_data(url_var: int, message: str, kb: object) -> None:
    
    api_city_url = "https://api.openweathermap.org/data/2.5/weather?q=" + message.text + "&units=metric" + "&appid=" + API_KEY
    api_local_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(coordinates.lat) + "&lon=" + str(coordinates.lng) + "&units=metric" + "&appid=" + API_KEY

    try:
        if url_var == 1:
            response = requests.get(api_city_url)
        else:
            response = requests.get(api_local_url)
        response.raise_for_status()
        weather_data = response.json()
        await message.answer(f"Weather: {weather_data['weather'][0]['main']}, {weather_data['weather'][0]['description']}\nTemperature: {weather_data['main']['temp']} °C, feels like {weather_data['main']['feels_like']} °C\nHumidity: {weather_data['main']['humidity']} %\nWind speed: {weather_data['wind']['speed']} м/с", reply_markup=kb)
    except requests.exceptions.RequestException as e:
        await message.answer(f"Error fetching fact: {e}")