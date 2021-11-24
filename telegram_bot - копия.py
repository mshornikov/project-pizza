import logging

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, ParseMode, Message
from aiogram.utils import executor
from aiogram.utils.markdown import italic , text, bold

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#кнопки
button_help = KeyboardButton("помощь")
button_menu = KeyboardButton("меню")
button_menu_all = KeyboardButton("покажи все меню")
button_menu_pizza = KeyboardButton("вся пицца")
button_joke = KeyboardButton("анекдот")
button_login = KeyboardButton("login")
greet = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_joke).add(button_login)
greet_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_menu_all).add(button_menu_pizza)

logging.basicConfig(filename="log_error_telegram.log", filemode='a', level=logging.ERROR, format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")

@dp.message_handler()
async def process_start_command(message: Message):
    with open("log_telegram.log", "a") as f:
        log_msg = "id: " + str(message.from_user.id)
        log_msg = log_msg + " text: " + message.text + "\n"
        f.write(log_msg)

    if message.text == 'начать':
        await message.answer("Привет! Я бот *nameCompany*!! С помощью меня вы можете ознакомиться с нашим ассортиментом и, если вы уже зарегистрировались у нас, посмотреть свои еженедельные скидки и заказы))")
        await message.answer("Для помощи можете вызвать команду \"помощь\"")
        await message.answer("Для вызова меню \"меню\"",  reply_markup = greet)

    elif message.text == 'помощь':
        string = text("Рад что ты спросил))"+"\n" + bold("\"помощь\"") + " с ней ты уже познакомился, это помощь)" + "\n") 
        string = string + bold("\"меню\"") + ", показывает меню... У нас все очень вкусно, скорее попробуй"+ "\n"
        string = string + bold("\"анекдот\"")  + ", секретная команда, никому про нее не рассказывай.."+ "\n"
        string = string  + bold("\"login\"") + ". Он поможет тебе зайти в твой аккаунт. Удивительно. Ты же его завел?0.о"
        await message.answer(string,  reply_markup = greet, parse_mode=ParseMode.MARKDOWN)

    elif message.text == "меню":
        string = "*Заглушка (здесь должна использоваться бд)*" + "\n"
        await message.answer(string,  reply_markup = greet_menu) 

    elif message.text == 'покажи все меню':
        string = "*Заглушка*"
        await message.answer(string,  reply_markup = greet_menu)

    elif message.text == 'вся пицца':
        string = ("*Заглушка*")
        await message.answer(string, reply_markup = greet_menu)

    elif message.text == 'анекдот':
        string = "*Заглушка (здесь должна использоваться бд)*"
        await message.answer(string,  reply_markup = greet)
        #здесь надо сделать обращение к базе данных, а не вот это вот

    elif message.text == 'login':
        string = "*Заглушка (здесь должна использоваться бд и хэши)*"
        await message.answer(string,  reply_markup = greet)

    else:
        string = "Я вас не понимаю, к сожалению"
        await message.answer(string,  reply_markup = greet)

if __name__ == '__main__':
    executor.start_polling(dp)