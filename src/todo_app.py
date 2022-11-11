from View.calendar_view import *
import tkinter as tk
from tkinter import ttk

class App_todo():
    def __init__(self):
        self.user_global=""
        self.password_global=""
        self.controller_user = UserController()

    def _user_login_(self):
        log_tk = tk.Tk()
        log_tk.title('Login')
        log_tk.resizable(0,0)

        self.username = StringVar()
        self.password = StringVar()
        
        notebook = ttk.Notebook(log_tk)
        notebook.pack()
        
        login_window = Frame(notebook,
                borderwidth=2,  relief=RIDGE,
                width=100,
            )
        notebook.add(login_window, text='Login')
        
        register_window = Frame(notebook,
                borderwidth=2,  relief=RIDGE,
                width=100,
            )
        notebook.add(register_window, text='Register')
        
        
        
        
        login_Font = tkFont.Font(family="Segoe", size=12)

        #username label and text entry box
        self.usernameLabel = Label(login_window, text="User Name",font=login_Font).grid(row=0, column=0)
        
        self.usernameEntry = Entry(login_window, textvariable=self.username,font=login_Font)
        self.usernameEntry.grid(row=0, column=1)  

        #password label and password entry box
        self.passwordLabel = Label(login_window,text="Password",font=login_Font).grid(row=1, column=0)  
        
        self.passwordEntry = Entry(login_window, textvariable=self.password, show='*',font=login_Font).grid(row=1, column=1)  
        
        
        Button(login_window,text="Inicia Sessió",font=login_Font, command=lambda : [self.login()]).grid(row=3,columnspan=2)
        
        
        #username label and text entry box
        self.usernameLabel2 = Label(register_window, text="User Name",font=login_Font).grid(row=0, column=0)
        self.username2 = StringVar()
        self.usernameEntry2 = Entry(register_window, textvariable=self.username2,font=login_Font).grid(row=0, column=1)  

        #email
        self.emailLabel = Label(register_window, text="Email",font=login_Font).grid(row=1, column=0)
        self.email = StringVar()
        self.emailentry = Entry(register_window, textvariable=self.email,font=login_Font).grid(row=1, column=1)  


        #password label and password entry box
        self.passwordLabel2 = Label(register_window,text="Password",font=login_Font).grid(row=2, column=0)  
        self.password2 = StringVar()
        self.passwordEntry2 = Entry(register_window, textvariable=self.password2, show='*',font=login_Font).grid(row=2, column=1)  
        
        
        Button(register_window,text="Registre",font=login_Font, command=lambda : [self.register()]).grid(row=3,columnspan=2)
        
        
        alert_Font = tkFont.Font(family="Console", size=12)
        message_label = Label(log_tk, font=alert_Font, fg='red').pack()
        
        log_tk.mainloop()

    def login(self):
        
        print(self.usernameEntry.get())

if __name__ == '__main__':
    app = App_todo()
    app._user_login_()