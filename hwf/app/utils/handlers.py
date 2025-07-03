import requests
import os

from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery, InputTextMessageContent
from aiogram.filters import CommandStart, Command

from dotenv import load_dotenv

import utils.keyboards as kb
from utils.geolocation import coordinates

load_dotenv()
API_KEY = os.environ.get("API_KEY")

router = Router()

cities_reply = [
    'Kyiv',
    'Kharkiv',
    'Odesa',
    'Dnipro',
    'Donetsk',
    'Lviv',
    'Zaporizhzhya',
    'Kryvyi Rih',
    'Luhansk'
]


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.first_name)}!")
    await message.answer(f"I am a weather bot.", reply_markup=kb.home)


@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.answer('HELP, OK')


@router.message(F.text == 'Weather Forecast')
async def weather_forecast(message: Message) -> None:
    await message.answer(f"Ok, {html.bold(message.from_user.first_name)}!", reply_markup=kb.weather_forecast)

@router.message(F.text == 'Home')
async def weather_forecast(message: Message) -> None:
    await message.answer(f"Ok, {html.bold(message.from_user.first_name)}, back to start", reply_markup=kb.home)

for city in cities_reply:
    @router.message(F.text == city)
    async def weather_forecast(message: InputTextMessageContent) -> None:
        await message.answer(f"Ok, {html.bold(message.from_user.first_name)}, one moment. Weather for {message.text}", reply_markup=kb.return_to_home)

        api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + message.text + "&units=metric" + "&appid=" + API_KEY

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            weather_data = response.json()
            await message.answer(f"Weather: {weather_data['weather'][0]['main']}, {weather_data['weather'][0]['description']}\nTemperature: {weather_data['main']['temp']} °C, feels like {weather_data['main']['feels_like']} °C\nHumidity: {weather_data['main']['humidity']} %\nWind speed: {weather_data['wind']['speed']} м/с", reply_markup=kb.return_to_home)
        except requests.exceptions.RequestException as e:
            await message.answer(f"Error fetching fact: {e}")

@router.callback_query(F.data == 'local')
async def fetch_weater_local(callback: CallbackQuery) -> None:
    await callback.message.answer(f'Ok, no problem. Weather for {coordinates.city}, {coordinates.country}')

    api_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(coordinates.lat) + "&lon=" + str(coordinates.lng) + "&units=metric" + "&appid=" + API_KEY
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = response.json()
        await callback.message.answer(f"Weather: {weather_data['weather'][0]['main']}, {weather_data['weather'][0]['description']}\nTemperature: {weather_data['main']['temp']} °C, feels like {weather_data['main']['feels_like']} °C\nHumidity: {weather_data['main']['humidity']} %\nWind speed: {weather_data['wind']['speed']} м/с", reply_markup=kb.return_to_home)
    except requests.exceptions.RequestException as e:
        await callback.message.answer(f"Error fetching fact: {e}")

@router.callback_query(F.data == 'city')
async def fetch_weater_by_city(callback: CallbackQuery) -> None:
    await callback.message.answer(f'Ok, no problem. You can tap city or write your own', reply_markup=kb.cities_ukr_top_list)

@router.message(F.text == 'Another city..')
async def fetch_weater_city_by_input(message: Message) -> None:
    await message.answer(f'Ok, no problem. Just tell me which one')

    # api_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(coordinates.lat) + "&lon=" + str(coordinates.lng) + "&units=metric" + "&appid=" + API_KEY
    # try:
    #     response = requests.get(api_url)
    #     response.raise_for_status()
    #     weather_data = response.json()
    #     await callback.message.answer(f"Weather: {weather_data['weather'][0]['main']}, {weather_data['weather'][0]['description']}\nTemperature: {weather_data['main']['temp']} °C, feels like {weather_data['main']['feels_like']} °C\nHumidity: {weather_data['main']['humidity']} %\nWind speed: {weather_data['wind']['speed']} м/с", reply_markup=kb.return_to_home)
    # except requests.exceptions.RequestException as e:
    #     await callback.message.answer(f"Error fetching fact: {e}")

@router.callback_query(F.data == 'city')
async def fetch_weater_by_city(callback: CallbackQuery) -> None:
    await callback.message.answer(f'Ok, no problem. You can tap city or write your own', reply_markup=kb.cities_ukr_top_list)