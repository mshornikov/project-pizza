import psycopg2 as db
import logging
from hashlib import sha256

def signIn(login, password):
    logging.basicConfig(filename="log_error_telegram.log", filemode='a', level=logging.ERROR, format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
    try:
        con = db.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="postgres")
    except:
        return ()
    
    cursor = con.cursor()
    hash_object = sha256(password.encode())
    hash_object = hash_object.hexdigest()
    sql = "SELECT * FROM users_customuser WHERE email = %s AND password = %s"
    cursor.execute(sql, [login, hash_object])
    res = cursor.fetchone()
    cursor.close()
    con.close()
    if res != None:
        return res[0]
    else:
        return ()

def orders(user):
    try:
        con = db.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="postgres")
    except:
        return ()

    cursor = con.cursor()
    sql = "SELECT * FROM orders_order WHERE user_id = %s"
    cursor.execute(sql, [user])
    res = cursor.fetchall()
    cursor.close()
    con.close()
    if res != []:
        string = ""
        for i in res: 
            string = string + "Заказ номер /" + str(i[0]) + " на сумму " + str(i[-2]) + "\n"
        return string
    else:
        return -1

def openOrders(number, user):
    try:
        con = db.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="postgres")
    except:
        return ()
    cursor = con.cursor()
    sql = "SELECT * FROM orders_order WHERE id = %s AND user_id =  %s"
    cursor.execute(sql, [str(number), user])
    res = cursor.fetchone()
    if res == None:
        return "Неверный номер!"

    sql = "SELECT * FROM orders_orderitems WHERE order_id = %s"
    cursor.execute(sql, str(number))
    res = cursor.fetchall()
    string =""
    for i in res:
        sql = "SELECT * FROM main_product WHERE id = %s"
        cursor.execute(sql, str(i[-1]))
        name = cursor.fetchone()
        string = string + str(i[2]) + " \"" + name[1] + "\" на сумму " + str(i[1]) + "\n"
    cursor.close()
    con.close()
    return string

def promo(user):
    try:
        con = db.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="postgres")
    except:
        return ()

    cursor = con.cursor()
    sql = "SELECT * FROM promo WHERE user_id = %s"
    cursor.execute(sql, [user])
    res = cursor.fetchall()
    cursor.close()
    con.close()
    if res != []:
        string = ""
        for i in res: 
            string = string + "Акция номер /" + str(i[0]) + "\n"
        return string
    else:
        return -1

def openPromo(number, user):
    try:
        con = db.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="postgres")
    except:
        return ()
    cursor = con.cursor()
    sql = "SELECT * FROM promo WHERE id = %s AND user_id = %s"
    cursor.execute(sql, [str(number), user])
    res = cursor.fetchone()
    if res == None:
        return "Неверный номер!"
    string =""
    sql = "SELECT * FROM main_product WHERE id = %s"
    cursor.execute(sql, str(res[2]))
    name = cursor.fetchone()
    string = string + "Акция номер /" + str(res[0]) + "\n" + "На \"" + name[1] + "\"" + "\n" + "Cкидка " + str(res[3]) + "%" + "\n"  + "До " + str(res[4])
    cursor.close()
    con.close()
    return string

def menu():
    try:
        con = db.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="postgres")
    except:
        return ()

    cursor = con.cursor()
    sql = "SELECT * FROM main_productcategory "
    cursor.execute(sql)
    res = cursor.fetchall()
    string = ""
    for i in res:
        string = string + "/" + str(i[0]) + " " + i[1] +  "\n"
    cursor.close()
    con.close()
    return string

def nextMenu(product, page):
    try:
        con = db.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="postgres")
    except:
        return ()
    cursor = con.cursor()
    sql = "SELECT * FROM main_product WHERE category_id = %s"
    cursor.execute(sql, str(product))
    res = cursor.fetchall()
    string = ""
    #flag -1 отключаем левый переход, 0 нормальное состояние, 1 отключаем правый переход
    if len(res) < page*4+5:
        len_end = len(res)
        flag = 1
    else:
        len_end = page*4+4
        flag = 0
    if page == 0:
        flag = -1
    len_start = page*4
    for i in range (len_start, len_end):
        string = string + "/" + str(i+1) + " " + res[i][1] +  "\n"
    cursor.close()
    con.close()
    return [string, flag]

def product(number, product) :
    try:
        con = db.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="postgres")
    except:
        return ()
    cursor = con.cursor()
    sql = "SELECT * FROM main_product WHERE category_id = %s"
    cursor.execute(sql, str(product))
    res = cursor.fetchall()
    string = ""
    number = int(number)
    if len(res) < number:
        return "Нету такого номера!"
    else:
        res = res[number]
        string =  res[1] + "\n"+ "Стоит " + str(res[3]) 
        res = res[2]
        if len(res) == 1:
            return string
        string   = string + "\n" + "Состав:" + "\n"
        for i in res:
            string = string + i
        return string
