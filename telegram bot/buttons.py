from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton #кнопки

#кнопки
button_help = KeyboardButton("помощь")
button_menu = KeyboardButton("меню")
button_joke = KeyboardButton("анекдот")
button_login = KeyboardButton("login")
button_exit = KeyboardButton("exit")
button_orders = KeyboardButton("заказы")
button_promo = KeyboardButton("акции")
button_acc = KeyboardButton("аккаунт")
button_next = KeyboardButton("следующая страница")
button_last = KeyboardButton("прошлая страница")

greet = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_joke).add(button_login)
greet_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu)
greet_post_login = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_joke).add(button_acc)
greet_acc = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_orders).add(button_promo).add(button_exit)
greet_order = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_acc)
greet_product_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_next).add(button_last)
greet_product_menu_w_l = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_next)
greet_product_menu_w_n = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu).add(button_last)
greet_product_menu_w_n_l = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_menu)