import logging
#основа
from aiogram import Bot
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardRemove #кнопки

from aiogram.types import ParseMode, Message #обработка сообщения

from aiogram.contrib.fsm_storage.memory import MemoryStorage #состояния

#файловый импорт
from config import TOKEN
from states import TestStates
from buttons import greet, greet_menu, greet_post_login
from stringPizza import success_str_log, fail_str_log, password_str, help_string, login_string
from stringPizza import start1, start2, start3, miss

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
            await message.answer(success_str_log, reply_markup = greet_post_login)
            await state.set_state(TestStates.all()[0])
            break

        else:   
            await message.answer(fail_str_log,  reply_markup = greet)
            await state.reset_state()

    else:
        await message.answer(success_str_log, reply_markup = greet_post_login)
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

            await state.set_state(TestStates.all()[2])
            await message.answer(password_str)
            break

        else: 
            await message.answer(fail_str_log,  reply_markup = greet)
            await state.reset_state()
            
    else:
        await state.set_state(TestStates.all()[2])
        await message.answer(password_str)

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
        await message.answer(start1)
        await message.answer(start2)
        await message.answer(start3,  reply_markup = greet_now)

    elif message.text == 'помощь':
        await message.answer(help_string,  reply_markup = greet_now, parse_mode=ParseMode.MARKDOWN)
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
        await state.set_state(TestStates.all()[1])
        await message.answer(login_string, reply_markup = ReplyKeyboardRemove())
#эх отдельное состояние надо прописать
#првоерка связи

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
        await message.answer(miss,  reply_markup = greet)

if __name__ == '__main__':
    executor.start_polling(dp)