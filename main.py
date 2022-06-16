from cmath import log
from email import message_from_file
import logging
from re import L
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import token

Token = token.TOKEN
bot = Bot(token=Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello, {0.first_name}! Do you want to see crypto currency graphics? Then press "Currency")'.format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user_id, message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
