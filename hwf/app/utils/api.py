import requests
import os

import utils.keyboards as kbs

from dotenv import load_dotenv

from utils.geolocation import coordinates


load_dotenv()

API_KEY = os.environ.get("API_KEY")


async def get_data(url_var: str, message: str, kb: object, name_city: str) -> None:
    
    try:
        if url_var == 'local':
            api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(coordinates.lat) + "&lon=" + str(coordinates.lng) + "&units=metric" + "&appid=" + API_KEY
            response = requests.get(api)
        elif url_var == 'city':
            api = "https://api.openweathermap.org/data/2.5/weather?q=" + message.text + "&units=metric" + "&appid=" + API_KEY
            response = requests.get(api)
        else:
            api = "https://api.openweathermap.org/data/2.5/weather?q=" + name_city + "&units=metric" + "&appid=" + API_KEY
            response = requests.get(api)
        response.raise_for_status()
        weather_data = response.json()
        await message.answer(f"Weather: {weather_data['weather'][0]['main']}, {weather_data['weather'][0]['description']}\nTemperature: {weather_data['main']['temp']} °C, feels like {weather_data['main']['feels_like']} °C\nHumidity: {weather_data['main']['humidity']} %\nWind speed: {weather_data['wind']['speed']} м/с", reply_markup=kb)
    except requests.exceptions.RequestException as e:
        await message.answer(f"Error fetching: {e}")
        await message.answer(f'Possibly no city named {message.text}', reply_markup=kbs.try_saved_home)