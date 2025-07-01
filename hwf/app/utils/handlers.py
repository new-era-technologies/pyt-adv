from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.answer('HELP, OK')