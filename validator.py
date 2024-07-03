import bcrypt
import re
from app_db import *
from functools import wraps
from tkinter import messagebox

def validator(login_entry, password_entry, pass_conf_entry, error_label):
    login_entry.config(bg='#64c7f5')
    pass_conf_entry.config(bg='#64c7f5')
    password_entry.config(bg='#64c7f5')

    login = login_entry.get()
    password = password_entry.get()
    pass_conf = pass_conf_entry.get()
    
    
    # Проверка условий пароля
    if (len(password) > 8 and
        re.search(r"[!@#é$=]", password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password)):
        
        if password == pass_conf:
            # Хеширование пароля
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            try:
                set_contact(login, hashed_password, 0)
                error_label.config(text="Пользователь зарегистрирован успешно!")
            except Exception as e:
                login_entry.config(bg='red')
                error_label.config(text="Такой пользователь уже существует!")
        else:
            pass_conf_entry.config(bg='red')
            error_label.config(text="Пароли не соответствуют!")
    else:
        password_entry.config(bg='red')
        error_label.config(text="Пароль должен состоять из:\n1 заглавной буквы,\n1 цифры,\n1 специального символа (!@#é$=)")

# Декоратор для активного юзера
def user_required(func):
    @wraps(func)
    def inner(self, login, current_user, *args, **kwargs):
        login = login.get()
        user = get_user(login)
        current_user = login
        if user:
            user['authenticated'] = 1
        if not user or not user['authenticated']: 
            raise PermissionError("User is not authenticated")
        return func(self, login, current_user, *args, **kwargs)
    return inner


# Декораток для выхода пользоваеля, нужно провести тест на работоспособность
def user_logout(func):
    @wraps(func)
    def inner (self, current_user, *args, **kwargs):
        if current_user is not None:
            current_user['authenticated'] = 0
        return func (self, current_user, *args, **kwargs)
    return inner

