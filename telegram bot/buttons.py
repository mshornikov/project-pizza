from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton #кнопки

#кнопки
button_help = KeyboardButton("помощь")
button_menu = KeyboardButton("меню")
button_menu_all = KeyboardButton("покажи все меню")
button_menu_pizza = KeyboardButton("вся пицца")
button_joke = KeyboardButton("анекдот")
button_login = KeyboardButton("login")
button_exit = KeyboardButton("exit")
button_orders = KeyboardButton("заказы")
button_promo = KeyboardButton("акции")
greet = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_joke).add(button_login)
greet_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_menu_all).add(button_menu_pizza)
greet_post_login = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_joke).add(button_exit).add(button_orders).add(button_promo)