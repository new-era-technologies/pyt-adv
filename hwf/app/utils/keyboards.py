from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


home = ReplyKeyboardMarkup(keyboard=[[(KeyboardButton(text='Weather Forecast')), (KeyboardButton(text='Saved'))]],
                           resize_keyboard=True,
                           input_field_placeholder='What you want today?')

weather_forecast = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='By city'), KeyboardButton(text='Local point')]],
                                       resize_keyboard=True,
                                       input_field_placeholder='What you want today?')

save_saved_home = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Save'), KeyboardButton(text='Saved')],
                                                [KeyboardButton(text='Home')]],
                                      resize_keyboard=True)

cities_default = ReplyKeyboardMarkup(keyboard=[[(KeyboardButton(text='Kyiv')), (KeyboardButton(text='Kharkiv')), (KeyboardButton(text='Odesa'))],
                                               [(KeyboardButton(text='Dnipro')), (KeyboardButton(text='Donetsk')), (KeyboardButton(text='Lviv'))],
                                               [(KeyboardButton(text='Zaporizhzhya')), (KeyboardButton(text='Kryvyi Rih')), (KeyboardButton(text='Luhansk'))]],
                                     resize_keyboard=True,
                                     input_field_placeholder='Type the city')