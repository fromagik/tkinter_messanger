import sqlite3

#Create connection
def get_connection(): 
    return sqlite3.connect('app_db.db')


#Cтворюємо таблицю 
def create_table():
    connect = get_connection() 
    cursor = connect.cursor() 
    cursor.execute(''' CREATE TABLE IF NOT EXISTS user(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   login TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL,
                   authenticated INTEGER) ''') 
    connect.commit() 
    connect.close() 


def set_contact(login, password, auth): # Додаємо користувача
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO user(login, password, authenticated) VALUES (?, ?, ?)', (login, password, auth))
    connect.commit()
    connect.close()


def get_user(login): # Возвращает пользователя и его статус, для аутентификации 
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT login, authenticated FROM user WHERE login = ?', (login, ))
    user = cursor.fetchone()
    connect.close()
    if user:
        return {'Login': user[0], 'authenticated': bool(user[1])} 
    return None


def table_exist(table_name): # Перевірка на існування таблиці
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name = ?", (table_name, ))
    exists = cursor.fetchone() is not None 
    connect.close()
    return exists

