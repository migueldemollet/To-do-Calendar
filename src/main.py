from View.calendar_view import *
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1200x500")
    
    agenda = Agenda(root, selectmode='day')
    date = agenda.datetime.today()# + agenda.timedelta(days=2)
    agenda.calevent_create(date, 'Llamar jefe', 'TRABAJO')
    agenda.calevent_create(date, 'Revisar correo', 'TRABAJO')
    agenda.calevent_create(date + agenda.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
    agenda.calevent_create(date + agenda.timedelta(days=3), 'Fichar al salir', 'TRABAJO')
    agenda.calevent_create(date + agenda.timedelta(days=3), 'Llamar al delegado!!', 'UNIVERSITAT')
    #agenda.calevent_remove(date + agenda.timedelta(days=3))

    agenda.tag_config('UNIVERSITAT', background='DarkOliveGreen1', foreground='black')
    agenda.tag_config('TRABAJO', background='bisque', foreground='black')
    agenda.tag_config('mix',background='grey',foreground='black')

    agenda.pack(fill="both", expand=True)
    
    labelsito = tk.Label(text='hey')
    labelsito.pack()
    root.mainloop()    
