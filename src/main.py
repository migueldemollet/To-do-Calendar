from View.calendar_view import *
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1200x500")
    
    agenda = Agenda(root, selectmode='day')
    agenda.pack(fill="both", expand=True)
    
    root.mainloop()    
