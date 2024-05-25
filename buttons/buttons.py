from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


async def languages():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇺🇿 Uzbek"),
            ],
            [
                KeyboardButton(text="🇷🇺 Русский"),
            ],
        ],
        resize_keyboard=True
    )
    return keyboard


async def main_menu(lang):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=lang == 'uz' and 'Katalog' or 'Каталог'),
                KeyboardButton(text=lang == 'uz' and 'Sozlamalar' or 'Настройки'),
            ],
            [
                KeyboardButton(text=lang == 'uz' and 'Biz bilan bog\'lanish' or 'Связаться с нами'),
            ],
        ],
        resize_keyboard=True
    )
    return keyboard


async def user_registration(lang):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=lang == 'uz' and "Ro'yxatdan o'tish" or "Зарегистрироваться"),
            ],
        ],
        resize_keyboard=True
    )
    return keyboard


async def get_number(lang):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=lang == 'uz' and "Raqamni yuborish" or "Отправить номер", request_contact=True),
            ],
        ],
        resize_keyboard=True
    )
    return keyboard
