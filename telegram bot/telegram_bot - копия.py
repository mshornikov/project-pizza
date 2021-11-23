import logging
#основа
from aiogram import Bot
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardRemove #кнопки

from aiogram.types import ParseMode, Message #обработка сообщения
from aiogram.utils.markdown import italic , text, bold #текст

from aiogram.contrib.fsm_storage.memory import MemoryStorage #состояния

#файловый импорт
from config import TOKEN
from states import TestStates
from buttons import greet, greet_menu, greet_post_login

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dic_id = dict()

logging.basicConfig(filename="log_error_telegram.log", filemode='a', level=logging.ERROR, format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")

@dp.message_handler(state=TestStates.TEST_STATE_PASSWORD)
async def first_test_state_case_met(message: Message):
    state = dp.current_state()
    msg_us_id = message.from_user.id
    msg_id = message.message_id
    #сразу для безопасности удаляем пароль, после проверяем: можем ли мы удалить прошлое сообщение бота?
    await bot.delete_message(message_id = msg_id, chat_id = msg_us_id)
    smth = dic_id[msg_us_id] 
    del dic_id[msg_us_id]

    try:
        await bot.delete_message(message_id = smth, chat_id = msg_us_id)
    except:
        for i in range  (smth, msg_id):
            try:
                await bot.delete_message(message_id = i, chat_id = msg_us_id)
            except:
                continue 
            string = "Отлично!"
            await message.answer(string, reply_markup = greet_post_login)
            await state.set_state(TestStates.all()[0])
            break

        else:   
            await message.answer("Что-то пошло не так! Попробуйте снова",  reply_markup = greet)
            await state.reset_state()

    else:
        string = "Отлично!"
        await message.answer(string, reply_markup = greet_post_login)
        await state.set_state(TestStates.all()[0])

@dp.message_handler(state=TestStates.TEST_STATE_LOGIN)
async def first_test_state_case_met(message: Message):
    state = dp.current_state()
    msg_us_id = message.from_user.id
    msg_id = message.message_id
     #сразу для безопасности удаляем логин, после проверяем: можем ли мы удалить прошлое сообщение бота?
    await bot.delete_message(message_id = msg_id, chat_id = msg_us_id)
    smth = dic_id[msg_us_id] 
    dic_id[msg_us_id] = msg_id + 1

    try:
        await bot.delete_message(message_id = smth, chat_id = msg_us_id)
    except:
        for i in range  (smth, msg_id):
            try:
                await bot.delete_message(message_id = i, chat_id = msg_us_id)
            except:
                continue
 
            string = "Теперь введите пароль"
            await state.set_state(TestStates.all()[2])
            await message.answer(string)
            break

        else: 
            await message.answer("Что-то пошло не так! Попробуйте снова",  reply_markup = greet)
            await state.reset_state()
            
    else:
        string = "Теперь введите пароль"
        await state.set_state(TestStates.all()[2])
        await message.answer(string)

@dp.message_handler(state='*')
async def process_start_command(message: Message, state: FSMContext):
    state = await state.get_state()
    if TestStates.all()[0] == state:
        greet_now = greet_post_login
    else:
        greet_now = greet

    with open('log_telegram.log','a') as f:
        log_msg = str(message.date)  + "  id: " + str(message.from_user.id)
        log_msg = log_msg + " text: " + message.text + "\n"
        f.write(log_msg)

    if message.text == 'начать':
        await message.answer("Привет! Я бот *nameCompany*!! С помощью меня вы можете ознакомиться с нашим ассортиментом и, если вы уже зарегистрировались у нас, посмотреть свои еженедельные скидки и заказы))")
        await message.answer("Для помощи можете вызвать команду \"помощь\"")
        await message.answer("Для вызова меню \"меню\"",  reply_markup = greet_now)

    elif message.text == 'помощь':
        string = text("Рад что ты спросил))"+"\n" + bold("\"помощь\"") + " с ней ты уже познакомился, это помощь)" + "\n") 
        string = string + bold("\"меню\"") + ", показывает меню... У нас все очень вкусно, скорее попробуй"+ "\n"
        string = string + bold("\"анекдот\"")  + ", секретная команда, никому про нее не рассказывай.."+ "\n"
        string = string  + bold("\"login\"") + ". Он поможет тебе зайти в твой аккаунт. Удивительно. Ты же его завел?0.о"
        await message.answer(string,  reply_markup = greet_now, parse_mode=ParseMode.MARKDOWN)
    #эх отдельное состояние надо прописать
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
        await message.answer(string,  reply_markup = greet_now)
        #здесь надо сделать обращение к базе данных, а не вот это вот

    elif message.text == 'login' and state != TestStates.all()[0]:
        dic_id[message.from_user.id] = message.message_id+1
        state = dp.current_state()
        string = "Теперь введите логин"
        await state.set_state(TestStates.all()[1])
        await message.answer(string, reply_markup = ReplyKeyboardRemove())
#эх отдельное состояние надо прописать
    elif message.text == "exit" and state == TestStates.all()[0]:
        state = dp.current_state()
        string = "Выполяняем выход..."
        await state.reset_state()
        await message.answer(string, reply_markup = greet)

    elif message.text == 'заказы' and state == TestStates.all()[0]:
        state = dp.current_state()
        string = "*Заглушка*"
        await message.answer(string, reply_markup = greet_post_login)

    elif message.text == 'акции' and state == TestStates.all()[0]:
        state = dp.current_state()
        string = "*Заглушка*"
        await message.answer(string, reply_markup = greet_post_login)

    else:  
        string = "Я вас не понимаю, к сожалению"
        await message.answer(string,  reply_markup = greet)

if __name__ == '__main__':
    executor.start_polling(dp)