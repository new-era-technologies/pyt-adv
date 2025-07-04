from aiogram import Router, F, html
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb

from utils.geolocation import coordinates
from utils.api import get_data


router = Router()


class City(StatesGroup):
    name = State()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.first_name)}!")
    await message.answer(f"I am a weather bot.", reply_markup=kb.home)

@router.message(Command('home'))
async def cmd_home(message: Message) -> None:
    await message.answer('Ok, back to home', reply_markup=kb.home)


@router.message(F.text == 'Weather Forecast')
async def weather_forecast(message: Message) -> None:
    await message.answer(f"Ok, {html.bold(message.from_user.first_name)}!", reply_markup=kb.weather_forecast)

@router.message(F.text == 'Home')
async def return_to_home(message: Message) -> None:
    await message.answer(f"Ok, {html.bold(message.from_user.first_name)}, back to start", reply_markup=kb.home)

@router.message(F.text == 'Local point')
async def fetch_weater_local(message: Message) -> None:
    await message.answer(f'Ok, no problem. Weather for {coordinates.city}, {coordinates.country}')
    await get_data(0, message, kb.save_saved_home)

@router.message(F.text == 'By city')
async def fetch_weather_by_city_set_state(message: Message, state: FSMContext) -> None:
    await message.answer('Tell me which city', reply_markup=kb.cities_default)
    await state.set_state(City.name)

@router.message(City.name)
async def fetch_weather_by_city_get_state(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await message.answer(f"Ok, {html.bold(message.from_user.first_name)}, one moment. Weather for {data['name'].capitalize()}")
    await get_data(1, message, kb.save_saved_home)
    await message.answer('Another one?')