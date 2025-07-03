from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


home = ReplyKeyboardMarkup(keyboard=[[(KeyboardButton(text='Weather Forecast')),
                                      (KeyboardButton(text='Saved'))]],
                           resize_keyboard=True,
                           input_field_placeholder='What you want today?')

weather_forecast = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Choose a city', callback_data='city')],
                                                         [InlineKeyboardButton(text='Use your local point', callback_data='local')]])

return_to_home = ReplyKeyboardMarkup(keyboard=[[(KeyboardButton(text='Home')),
                                      (KeyboardButton(text='Save this city'))]],
                                     resize_keyboard=True,
                                     input_field_placeholder='What you want today?')

cities_ukr_top_list = ReplyKeyboardMarkup(keyboard=[[(KeyboardButton(text='Kyiv')), (KeyboardButton(text='Kharkiv')), (KeyboardButton(text='Odesa'))],
                                                    [(KeyboardButton(text='Dnipro')), (KeyboardButton(text='Donetsk')), (KeyboardButton(text='Lviv'))],
                                                    [(KeyboardButton(text='Zaporizhzhya')), (KeyboardButton(text='Kryvyi Rih')), (KeyboardButton(text='Luhansk'))],
                                                    [(KeyboardButton(text='Another city..'))]],
                                          resize_keyboard=True,
                                          input_field_placeholder='What you want today?')