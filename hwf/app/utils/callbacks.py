# from aiogram import Router, F
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import CommandStart, Command

# router = Router()


# @router.message(Command('help'))
# async def cmd_help(message: Message) -> None:
#     await message.answer('HELP, OK')

# @router.callback_query(F.data == 'local')
# async def local(callback: CallbackQuery) -> None:
#     await callback.message.answer('Ok, no problem. Weather for ..')