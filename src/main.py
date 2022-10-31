from View.calendar_view import *

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.geometry("1200x500")
    
    agenda = Agenda(root, selectmode='day')
    date = agenda.datetime.today()# + agenda.timedelta(days=2)
    agenda.calevent_create(date, 'Hello World', 'message')
    agenda.calevent_create(date, 'Reminder 2', 'message')
    agenda.calevent_create(date + agenda.timedelta(days=-7), 'Reminder 1', 'reminder')
    agenda.calevent_create(date + agenda.timedelta(days=3), 'Message', 'message')
    agenda.calevent_create(date + agenda.timedelta(days=3), 'Another message', 'reminder')
    #agenda.calevent_remove(date + agenda.timedelta(days=3))

    agenda.tag_config('reminder', background='red', foreground='white')
    agenda.tag_config('message', background='blue', foreground='white')
    agenda.tag_config('mix',background='grey',foreground='white')

    agenda.pack(fill="both", expand=True)
    
    labelsito = tk.Label(text='hey')
    labelsito.pack()
    root.mainloop()    
