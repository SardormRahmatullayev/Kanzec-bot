import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from api.api import *
from get_text.get_text import *
from buttons.buttons import *
from aiogram.fsm.context import FSMContext
from states.states import Form

TOKEN = "7162103854:AAFz8uzmO1gglBI58GLrFjPVqohDzZCRnYE"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    user_exists = await create_user(user_id, username)
    lang = await get_user_language(user_id)
    if user_exists:
        await message.answer(await start_text(lang), parse_mode='markdown', reply_markup=await languages())
    else:
        await message.answer(await start_hello_text(lang), parse_mode='markdown', reply_markup=await languages())


@dp.message(lambda message: message.text == '🇺🇿 Uzbek' or message.text == '🇷🇺 Русский')
async def select_language(message: types.Message):
    user_id = message.from_user.id
    language = message.text
    text_language = await update_langugaes_text(language)
    await update_language_user(user_id, text_language)
    lang = await get_user_language(user_id)
    await message.answer(await start_text(lang), parse_mode='markdown', reply_markup=await main_menu(lang))


@dp.message(lambda message: message.text == "Katalog" or message.text == "Каталог")
async def catalog_menu(message: Message):
    user_id = message.from_user.id
    check = await check_user_registration(user_id)
    lang = await get_user_language(user_id)
    text_1 = await get_registration_user(lang)
    text_2 = await get_registration_user(lang)
    if check is None:
        await message.answer(text_2, parse_mode='markdown')
    else:
        await message.answer(text_1, parse_mode='markdown')


@dp.message(lambda message: message.text in ['Ro\'yxatdan o\'tish', 'Зарегистрироваться'])
async def reaction_to_registration(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    await message.answer(await state_user_name(lang), parse_mode='markdown', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Form.user_full_name)


@dp.message(Form.user_full_name)
async def process_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    if not (message.text.replace(__old=' ', __new='').isalpha()) and len(message.text.split()) == 2:
        await message.answer(await state_error_username(lang), parse_mode='markdown')
    else:
        await state.update_data(user_full_name=message.text)
        await state.set_state(Form.phone_number)
        await message.answer(await get_user_phone(lang), parse_mode='markdown', reply_markup=await get_number(lang))
        await message.delete()


@dp.message(Form.phone_number)
async def get_user_phone_number(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)

    if message.contact:
        await state.update_data(phone_number=message.contact.phone_number)
        data = state.get_data()
        print(data)


    else:
        await message.answer(await error_phone_user_number(lang))


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
