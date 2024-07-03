import tkinter as tk
from collections import UserDict
from app_db import *
from validator import *

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class App:
    def __init__(self, root):
        self.root = root
        self.current_user = None
        self.book = AddressBook()
        self.window_param()
        self.main(self.current_user)


    def window_param(self):
        # очищуємо вікно
        for widget in self.root.winfo_children():
            widget.destroy()

        # Параметри вікна
        self.root.title('Messanger')
        self.root.geometry("400x500")
        self.root.minsize(width=400, height=500)
        self.root.maxsize(width=400, height=500)
        self.root.configure(bg='#8c6e00')

    @user_logout
    def main(self, current_user):
    # Главное окно 
        self.window_param()

        # Ініціалізація тексту 
        welcm_label = tk.Label(text='Welcome to Messanger\nPlease sing in or sign up', bg='#8c6e00', font=('Arial', 20), padx=5, pady=5)
        welcm_label.place(x=100, y=130)

        #Кнопка для входу та реєстрації
        btn_login = tk.Button(root, text='Login', bg='#0519f5', command=self.login, bd=0, highlightthickness=0, width=10, height=2)
        btn_registr = tk.Button(root, text='Registration', command=self.registration, bd=0, highlightthickness=0, width=10, height=2)
        btn_login.place(x=150, y=200)
        btn_registr.place(x=150, y=240) 

    def login(self):
    # Окно входа
        self.window_param()

        self.label_log = tk.Label(root, text="Login", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
        self.entry_log = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
        self.label_pass = tk.Label(root, text="Password", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
        self.entry_pass = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))

        self.label_log.place(x=120, y=140)
        self.entry_log.place(x=120, y=170, width=160, height=30) 
        self.label_pass.place(x=120, y=200)
        self.entry_pass.place(x=120, y=230, width=160, height=30)

        # Добавление кнопки для возврата к главному окну и кнопки входа
        self.btn_login = tk.Button(root, text='Sign in', bg='#0519f5', command=lambda: self.user_menu(self.entry_log, self.current_user), bd=0, highlightthickness=0, width=5, height=2)
        self.btn_back = tk.Button(root, text='Back', bg='#0519f5', command=self.main, bd=0, highlightthickness=0, width=5, height=2)
        self.btn_login.place(x=120, y=260)
        self.btn_back.place(x=200, y=260)


    def registration(self):
    # Окно регистрации
        self.window_param()

        self.label_log = tk.Label(root, text="Login", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
        self.entry_log = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
        self.label_pass = tk.Label(root, text="Password", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
        self.entry_pass = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
        self.label_pass_conf = tk.Label(root, text="Confirme password", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
        self.entry_pass_conf = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
        self.label_error = tk.Label(root, bg='#8c6e00')

        self.label_error.pack()
        self.label_log.place(x=120, y=130)
        self.entry_log.place(x=120, y=160, width=160, height=30) 
        self.label_pass.place(x=120, y=190)
        self.entry_pass.place(x=120, y=220, width=160, height=30)
        self.label_pass_conf.place(x=120, y=250)
        self.entry_pass_conf.place(x=120, y=280, width=160, height=30)
    # Кнопка регистрации отправляет на валидатор для проверки и добавления пользователя 
        self.btn_regist = tk.Button(root, text='Sign up', bg='#0519f5', command=lambda: validator(self.entry_log, self.entry_pass, self.entry_pass_conf, self.label_error), bd=0, highlightthickness=0, width=5, height=2)
        self.btn_back = tk.Button(root, text='Back', bg='#0519f5', command=lambda: self.main(), bd=0, highlightthickness=0, width=5, height=2)
        self.btn_regist.place(x=120, y=320)
        self.btn_back.place(x=200, y=320)
        self.error_label = tk.Label(root, text="", fg="red")
        self.error_label.place()


    @user_required
    def user_menu(self, login, current_user):
        self.window_param()
        # Add contacts and logout manu
        self.add_label = tk.Label(root, text="Add contact", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
        self.name_entry = PlaceholderEntry(root, placeholder='Name contact', bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
        self.phone_entry = PlaceholderEntry(root, placeholder='Numer contact', bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
        self.add_btn = tk.Button(root, text='Sign up', bg='#0519f5', command=lambda: self.add_contact(self.name_entry, self.phone_entry), bd=0, highlightthickness=0, width=5, height=2)
        self.logout_btn = tk.Button(self.root, text='Logout', bg='#0519f5', command=lambda: self.main(self.current_user), bd=0, highlightthickness=0, width=5, height=2)

        self.add_label.place(x=20, y=10)
        self.name_entry.place(x=20, y=40)
        self.phone_entry.place(x=20, y= 70)
        self.add_btn.place(x=20, y= 100)
        self.logout_btn.place(x=320, y=10)


    def add_contact(self, name, phone):
        name = name.get()
        phone = phone.get()
        contact = Record(name)
        contact.add_phone(phone)
        self.book.add_record(contact)

        cont_label = tk.Label(root, text="All contacts", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
        cont_label.place(x=20, y=130)

        y_position = 160
        for contact in self.book:
            contact_btn = tk.Button(root, text=contact, bg='#8c6e00', font=('Arial', 14), bd=0, highlightthickness=0, width=5, height=2)
            contact_btn.place(x=20, y=y_position)
            y_position += 40
        


class Field:  #Клас що використовується для базовий клас для зберігання та обробки імя та номеру
    def __init__(self, value):
        self.value = value
    
    
    def __str__(self):
        return str(self.value)
        

class Name(Field): # Клас що використовується для сберігання та обробки імені контакта
    def __init__(self, value):
        self.value = value
        super().__init__(value)


class Phone(Field): # Клас що використовується для сберігання та обробки номеру контакта
    def __init__(self, phone_number:str):
        if not phone_number.isdigit() or len(phone_number) != 10: # Перевірка на правельний запис номеру, викликає виняток 
            raise ValueError("Номер телефону має складатися з 10 цифр і містити лише цифри.")
        super().__init__(phone_number)


class Record: # Клас що використовується для роботи з контактом
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        

    def add_phone(self, phone: str) -> None:
          #Метод для додавання номеру контакта 
        self.phones.append(Phone(phone))


    def remove_phone(self, phone: str) -> None: #Метод для видалення номеру контакта
        for numer in self.phones:
            if numer.value == phone:
                self.phones.remove(numer)
                break


    def edit_phone(self, phone: str, new_phone:str) -> None: # Метод для зміни номеру контакта
        for numer in self.phones: # Ітеруємось по списку номерів для контакту
            if numer.value == phone: # Якщо значення відповідає вказаному номеру то присвоюється новий номер
                numer.value = new_phone
                break


    def find_phone(self, phone: str) -> str: # Метод для пошуку контакта за номером
        for numer in self.phones:
            if numer.value == phone: # Якщо значення відповідає вказаному номеру то повертається номер
                return phone 
            else: # Або викликається вийняток який вказує що номер не знайжено
                raise ValueError(f'Номер контакту "{phone}" не знайдено.')


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict): # Клас для зберігання всіх контатів 
    def __init__(self):
        self.data = {}
        super().__init__()


    def add_record(self, contact): # Метод що використовується для добавлення нового контакту
        self.data[contact.name.value] = contact


    def find(self, contact): # Метод що використовується для знаходження контакта та повертає інформацію про його
        return self.data.get(contact)
    
    
    def delete(self, contact): # Метод для видалення контакту з контактонї книги
        del self.data[contact.name.value]


    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


if __name__ == '__main__':

    if not table_exist('user'):
        create_table()

    root = tk.Tk()
    app = App(root)
    root.mainloop()
