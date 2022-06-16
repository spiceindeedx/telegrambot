from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

btnMain = KeyboardButton('Main menu')

#--- Main Menu ---
btnRandom = KeyboardButton('Random number')
btnOther = KeyboardButton('Other')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnOther)

#--- Other Menu ---
btnInfo = KeyboardButton('Information')
btnMoney = KeyboardButton('Currency')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)
