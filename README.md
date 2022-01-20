# Project Pizza
# Описание
Сайт пиццерии. На сайте можно зарегистрироваться или же войти в уже имеющийся аккаунт. Есть меню, товары в него добавляются через админку. Можно заказать на сайте товар с доставкой по указанному адресу и он добавится в корзину. Есть возможность воспользоваться акциями, прописав промокод. Можно ещё посмотреть контакты пиццерии, расположении пиццерии, посмотреть имеющиеся вакансии. Помимо этого на сайте размещены ссылки на бота и почту.

Через админку можно создавать еженедельные акции. Через админку добавляются категории товаров, сами товары, акции, комбо.

В боте есть авторизация в аккаунт (тот же, что и на сайте), можно просмотреть меню пиццерии, можно попросить дать скидочку, есть возможность посмотреть свои заказы и если очень хочется, то бот может пошутить шутку.

Оплата товаров происходит наличными при получении доставки.

# Домены
Сайт: http://localhost:8000/

Админка сайта: http://localhost:8000/admin

Ссылка на бота в Телеграме:  https://t.me/admiralKucha_bot

Имя бота в Телеграме: @admiralKucha_bot

# Команды бота
/start — начало работы с ботом
основные команды это кнопки в клавиатуры или /что-то в тексте
при отсутствие категорий меню ничего не выдает, нужно добавить хотя б 1 категорию
при отсутствие продуктов не произойдет создание акции, нужно добавить хотя б 1 товар

# Запуск

1) Перейти через консоль в папку с проектом
2) Забилдить проект через команду "docker-compose build"
3) Запустить проект через команду "docker-compose up"
4) Уже в другой консоли перейти в папку с проектом и создать суперпользователя через команду "docker exec -it site python ./projectpizza/manage.py createsuperuser"
5) Заполнить данные 
6) Сайт запускается по ссылке http://localhost:8000/
7) Для заполнения базы данных необходимо перейти по ссылке http://localhost:8000/admin/

# Авторы

Шорников Михаил 

Узингер Артём

Глинский Максим

Вихров Евгений

26 группа
