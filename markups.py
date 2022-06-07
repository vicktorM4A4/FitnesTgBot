from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

#---mainmenu---
btnLc = KeyboardButton('Личный кабинет')
btnBuyticket = KeyboardButton('Купить абонемент')
btnOurservices = KeyboardButton('Наши услуги')
btnSignUpForWorkout = KeyboardButton('Записатсья на тренировку')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup (resize_keyboard = True).add(btnBuyticket,btnLc,btnSignUpForWorkout,btnOurservices,btnOther)
#--other menu---
btnInfo = KeyboardButton('Информация')
btnAdress = KeyboardButton('Адрес')
otherMenu = ReplyKeyboardMarkup (resize_keyboard = True).add(btnInfo,btnAdress,btnMain)