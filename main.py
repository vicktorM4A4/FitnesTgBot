import logging
from aiogram import Bot,Dispatcher,executor,types
import markups as nav

TOKEN = "5371079297:AAEDAM6GAUdziVQiGeUWoAB2MDSHBlJRwyI"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
     await bot.send_message(message.from_user.id, 'Добро пожаловать {0.first_name}'.format(message.from_user),reply_markup = nav.mainMenu)


@dp.message_handler()
async def   bot_message(message:types.Message):
    if message.text == 'Личный кабинет':
        await bot.send_message(message.from_user.id, 'https://olimpiyasport.ru/#fitnesskit_personal',reply_markup=nav.mainMenu)

    elif message.text == 'Купить абонемент':
        await bot.send_message(message.from_user.id, 'Купить абонемент',)

    elif message.text == 'Наши услуги':
        await bot.send_message(message.from_user.id, 'Здесь услуги с сайта выведутся',)

    elif message.text == 'Записатсья на тренировку':
        await bot.send_message(message.from_user.id, 'линк с базой на тренировку',)

    elif message.text == 'Другое':
        await bot.send_message(message.from_user.id, 'Наши контакты:',reply_markup=nav.otherMenu)

    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, ' Возврат ',reply_markup=nav.mainMenu)
    elif  message.text =='Информация':
        await bot.send_message(message.from_user.id, ' здесь высрется информация ')
    elif  message.text =='Адрес':
        await bot.send_message(message.from_user.id, ' здесь высрется Адрес ')
            


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)