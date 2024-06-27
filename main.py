import tkinter as tk

root = tk.Tk()

def window_param():
    # очищуємо вікно
    for widget in root.winfo_children():
        widget.destroy()

    # Параметри вікна
    root.title('Messanger')
    root.geometry("400x500")
    root.minsize(width=400, height=500)
    root.maxsize(width=400, height=500)
    root.configure(bg='#8c6e00')

def main():

    window_param()

    # Ініціалізація тексту 
    welcm_label = tk.Label(text='Welcome to Messanger\nPlease sing in or sign up', bg='#8c6e00', font=('Arial', 20), padx=5, pady=5)
    welcm_label.place(x=100, y=130)

    #Кнопка для входу та реєстрації
    btn_login = tk.Button(root, text='Login', bg='#0519f5', command=login, bd=0, highlightthickness=0, width=10, height=2)
    btn_registr = tk.Button(root, text='Registration', command=registration, bd=0, highlightthickness=0, width=10, height=2)
    btn_login.place(x=150, y=200)
    btn_registr.place(x=150, y=240) 

def login():

    window_param()

    label_log = tk.Label(root, text="Login", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
    entry_log = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
    label_pass = tk.Label(root, text="Password", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
    entry_pass = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))

    label_log.place(x=120, y=140)
    entry_log.place(x=120, y=170, width=160, height=30) 
    label_pass.place(x=120, y=200)
    entry_pass.place(x=120, y=230, width=160, height=30)

    # Добавление кнопки для возврата к главному окну и кнопки входа
    btn_login = tk.Button(root, text='Sign in', bg='#0519f5', command=login, bd=0, highlightthickness=0, width=5, height=2)
    btn_back = tk.Button(root, text='Back', bg='#0519f5', command=main, bd=0, highlightthickness=0, width=5, height=2)
    btn_login.place(x=120, y=260)
    btn_back.place(x=200, y=260)


def registration():

    window_param()

    label_log = tk.Label(root, text="Login", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
    entry_log = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
    label_pass = tk.Label(root, text="Password", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
    entry_pass = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))
    label_pass_conf = tk.Label(root, text="Confirme password", bg='#8c6e00', font=('Arial', 14), padx=5, pady=5)
    entry_pass_conf = tk.Entry(root, bg='#64c7f5', fg='black', bd=0, font=('Arial', 12))

    label_log.place(x=120, y=130)
    entry_log.place(x=120, y=160, width=160, height=30) 
    label_pass.place(x=120, y=190)
    entry_pass.place(x=120, y=220, width=160, height=30)
    label_pass_conf.place(x=120, y=250)
    entry_pass_conf.place(x=120, y=280, width=160, height=30)

    btn_regist = tk.Button(root, text='Sign up', bg='#0519f5', command=login, bd=0, highlightthickness=0, width=5, height=2)
    btn_back = tk.Button(root, text='Back', bg='#0519f5', command=main, bd=0, highlightthickness=0, width=5, height=2)
    btn_regist.place(x=120, y=320)
    btn_back.place(x=200, y=320)

if __name__ == '__main__':
    main()
    root.mainloop()
