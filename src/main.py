from View.calendar_view import *
import tkinter as tk
from tkinter import ttk
import sys



if __name__ == '__main__':
    root = Tk()
    root.title("TODO-Calendar")
    root.resizable(0,0)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='public\img\logo_sm.ico'))
            
    #cursor="hand1"
    agenda = Agenda(root, selectmode='day',id_user=1)
    agenda.pack(fill="both",expand=True)



    root.mainloop()