import sqlite3 as sql3
from hashlib import sha256

def signIn(login, password):
    con = sql3.connect("C:/Users/Максим/Documents/GitHub/project-pizza/telegram bot/db4.sqlite3")
    cursor = con.cursor()
    hash_object = sha256(password.encode())
    hash_object = hash_object.hexdigest()
    sql = "SELECT * FROM auth_user WHERE password=? AND email=?"
    cursor.execute(sql, (hash_object, login))
    res = cursor.fetchall()
    if res != []:
        return True
    else:
        return False
        
print(signIn("projectpizza@dev.il", "1234"))