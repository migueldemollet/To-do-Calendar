from View.calendar_view import *
import tkinter as tk
from tkinter import ttk
import sys



if __name__ == '__main__':
    root = tk.Tk()
    root.title("TODO-Calendar")
    root.resizable(0,0)
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='public\img\logo_sm.ico'))
            
    #cursor="hand1"
    agenda = Agenda(root, selectmode='day',id_user='1')
    agenda.pack(fill="both",expand=True)



    root.mainloop()
    """ def exec_root():
        log_tk.destroy()
        
        
    def check_login():
        if(username.get()=='miguel' and password.get()=='putoamo'):
            exec_root()
        else:
            print("LOGIN ERRONEO")
            
    def check_register():
        exec_root()


    

    log_tk = tk.Tk()
    log_tk.title('Login')
    log_tk.resizable(0,0)

    
    notebook = ttk.Notebook(log_tk)
    notebook.pack()
    
    login_window = Frame(notebook, background="AliceBlue",
            borderwidth=2,  relief=RIDGE,
            width=100,
        )
    notebook.add(login_window, text='Login')
    
    register_window = Frame(notebook, background="AliceBlue",
            borderwidth=2,  relief=RIDGE,
            width=100,
        )
    notebook.add(register_window, text='Register')
    
    
    
    
    login_Font = tkFont.Font(family="Segoe", size=12)

    #username label and text entry box
    usernameLabel = Label(login_window, text="User Name",font=login_Font).grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(login_window, textvariable=username,font=login_Font).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(login_window,text="Password",font=login_Font).grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(login_window, textvariable=password, show='*',font=login_Font).grid(row=1, column=1)  
    
    
    Button(login_window,text="Inicia Sessió",font=login_Font, command=lambda : [check_login(),print("\n")]).grid(row=3,columnspan=2)
    
    
    #username label and text entry box
    usernameLabel2 = Label(register_window, text="User Name",font=login_Font).grid(row=0, column=0)
    username2 = StringVar()
    usernameEntry2 = Entry(register_window, textvariable=username2,font=login_Font).grid(row=0, column=1)  

    #email
    emailLabel = Label(register_window, text="Email",font=login_Font).grid(row=1, column=0)
    email = StringVar()
    emailentry = Entry(register_window, textvariable=email,font=login_Font).grid(row=1, column=1)  


    #password label and password entry box
    passwordLabel2 = Label(register_window,text="Password",font=login_Font).grid(row=2, column=0)  
    password2 = StringVar()
    passwordEntry2 = Entry(register_window, textvariable=password2, show='*',font=login_Font).grid(row=2, column=1)  
    
    
    Button(register_window,text="Registra",font=login_Font, command=lambda : [check_register(),print("\n")]).grid(row=3,columnspan=2)
    
    
    alert_Font = tkFont.Font(family="Console", size=12)
    message_label = Label(log_tk, font=alert_Font, fg='red').pack()
    
    log_tk.mainloop()"""