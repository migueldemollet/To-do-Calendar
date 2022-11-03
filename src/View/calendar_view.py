from tkcalendar import Calendar
from tkinter import *
import tkinter.font as tkFont

class Agenda(Calendar):

    def __init__(self, master=None,  **kw):
        
        WINDOW_WIDTH = int(master.winfo_screenwidth()*80/100)
        WINDOW_HEIGHT = int(master.winfo_screenheight()*60/100)
        WINDOW_MARGIN_X = int((master.winfo_screenwidth()-WINDOW_WIDTH)/2)
        WINDOW_MARGIN_Y = int((master.winfo_screenheight()-WINDOW_HEIGHT-60)/2)
        
        master.geometry(str(WINDOW_WIDTH)+'x'+str(WINDOW_HEIGHT)+"+"+str(WINDOW_MARGIN_X)+"+"+str(WINDOW_MARGIN_Y)+"")
        
        
        Calendar.__init__(self, master, **kw)
        self.normal_Font = tkFont.Font(family="Segoe", size=10, slant='roman', overstrike = 0)
        self.completed_Font = tkFont.Font(family="Segoe", size=10, slant='italic', overstrike = 1)
        self.icon_Font = tkFont.Font(family="Console", size=10)
        self.alert_Font = tkFont.Font(family="Console", size=12)
        
        
        self._CONTROLLER_getTags()
        self._CONTROLLER_getTasks()

        self.list_buttons = []
        
        """ self.left_frame = Frame(master, background="red",
        borderwidth=5,  relief=RIDGE,
        height=500, 
        width=50, 
        )
        self.left_frame.pack(side=LEFT,
        fill=BOTH, 
        expand=True,
        )"""
        
        
        self.message_label = Label(master, font=self.alert_Font, fg='red')
        self.message_label.pack(side=BOTTOM)

        self.right_frame = Frame(master, background="AliceBlue",
            borderwidth=15,  relief=RIDGE,
            width=100,
        )
        self.right_frame.pack(side=RIGHT,
            fill=BOTH, 
            expand=True,
            padx=20,
            pady=30
        ) 
        
        """self.sb = Scrollbar(master, command=self.right_frame.yview)
        self.sb.pack(side="right")
        self.right_frame.configure(yscrollcommand=self.sb.set)"""
        
        

        

        # change a bit the options of the labels to improve display
        for i, row in enumerate(self._calendar):
            for j, label in enumerate(row):
                self._cal_frame.rowconfigure(i + 1, uniform=1)
                self._cal_frame.columnconfigure(j + 1, uniform=1)
                label.configure(justify="center", anchor="n", padding=(1, 4))
                
        
    
    
  
    def _CONTROLLER_complete_task(self,ev_id,event):
        if(self.calevents[ev_id]['completed'] == 0):
            self.calevents[ev_id]['completed'] = 1
        else:
            self.calevents[ev_id]['completed'] = 0
        
        self._on_click(event,1)
        
        self.message_label.configure(text=(self.calevents[ev_id]['text'] + "switched to " + str(self.calevents[ev_id]['completed'])))
        self.message_label.update()
        

    def _CONTROLLER_show_description(self,event_id,event):
        self.message_label.configure(text='NOT IMPLEMENTED!')
        self.update()
        
    def _CONTROLLER_edit_task(self,event_id,event):
        self.message_label.configure(text='NOT IMPLEMENTED!')
        self.update()
        
        
    def _CONTROLLER_delete_task(self,event_id,event):
        self.message_label.configure(text='NOT IMPLEMENTED!')
        self.update()
        
     
    def _CONTROLLER_getTags(self):
        self.tag_config('UNIVERSITAT', background='DarkOliveGreen1', foreground='black')
        self.tag_config('TRABAJO', background='bisque', foreground='black')
        self.tag_config('mix',background='grey',foreground='black')
        
       
        
    def _CONTROLLER_getTasks(self):
        date = self.datetime.today()# + self.timedelta(days=2)
        self.calevent_create(date, 'Llamar jefe', 'TRABAJO')
        self.calevent_create(date, 'Revisar correo', 'TRABAJO')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=3), 'Fichar al salir', 'TRABAJO')
        self.calevent_create(date + self.timedelta(days=3), 'Llamar al delegado!!', 'UNIVERSITAT')
        #self.calevent_remove(date + self.timedelta(days=3))

        
        for event_id,ev in self.calevents.items():
            if(event_id%2 == 0):
                ev['completed'] = 0
            else:
                ev['completed'] = 1
            
    
    
    
    def _show_event(self, date):
        """Display events on date if visible."""
        w, d = self._get_day_coords(date)
        if w is not None:
            label = self._calendar[w][d]
            label.configure(width=15)
            if not label.cget('text'):
                # this is an other month's day and showothermonth is False
                return
            ev_ids = self._calevent_dates[date]
            i = len(ev_ids) - 1
            while i >= 0 and not self.calevents[ev_ids[i]]['tags']:
                i -= 1
                

            if i >= 0:
                tag = self.calevents[ev_ids[i]]['tags'][-1]
                label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))
                
                

            taglist_show=[]
            for item in ev_ids:
                if(self.calevents[item]['tags'] not in taglist_show):
                        taglist_show.append(self.calevents[item]['tags'])

            if len(taglist_show) > 1:
                label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))

            # modified lines:
            
            #text = '%s\n' % date.day + '\n'.join([self.calevents[ev]['text'][0:17] for ev in ev_ids])
            text = str(date.day)+'\n'
            for ev in ev_ids[0:2]:
                text = text + self.calevents[ev]['text'][0:17] + '\n'
                    
            if(len(ev_ids)>3):
                text = text+'...'


            label.configure(text=text)
            
    def _display_days_without_othermonthdays(self):
        year, month = self._date.year, self._date.month

        cal = self._cal.monthdays2calendar(year, month)
        while len(cal) < 6:
            cal.append([(0, i) for i in range(7)])

        week_days = {i: 'normal.%s.TLabel' % self._style_prefixe for i in range(7)}  # style names depending on the type of day
        week_days[self['weekenddays'][0] - 1] = 'we.%s.TLabel' % self._style_prefixe
        week_days[self['weekenddays'][1] - 1] = 'we.%s.TLabel' % self._style_prefixe
        _, week_nb, d = self._date.isocalendar()
        if d == 7 and self['firstweekday'] == 'sunday':
            week_nb += 1
        modulo = max(week_nb, 52)
        for i_week in range(6):
            if i_week == 0 or cal[i_week][0][0]:
                self._week_nbs[i_week].configure(text=str((week_nb + i_week - 1) % modulo + 1))
            else:
                self._week_nbs[i_week].configure(text='')
            for i_day in range(7):
                day_number, week_day = cal[i_week][i_day]
                style = week_days[i_day]
                label = self._calendar[i_week][i_day]
                label.state(['!disabled'])
                if day_number:
                    txt = str(day_number)
                    label.configure(text=txt, style=style)
                    date = self.date(year, month, day_number)
                    if date in self._calevent_dates:
                        ev_ids = self._calevent_dates[date]
                        i = len(ev_ids) - 1
                        while i >= 0 and not self.calevents[ev_ids[i]]['tags']:
                            i -= 1
                        if i >= 0:
                            tag = self.calevents[ev_ids[i]]['tags'][-1]
                            label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))

                        taglist_show=[]
                        for item in ev_ids:
                            if(self.calevents[item]['tags'] not in taglist_show):
                                    taglist_show.append(self.calevents[item]['tags'])

                        if len(taglist_show) > 1:
                            label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))
                        # modified lines:
                        #text = '%s\n' % day_number + '\n'.join([self.calevents[ev]['text'][0:17] for ev in ev_ids])
                        text = str(date.day)+'\n'
                        for ev in ev_ids[0:2]:
                            text = text + self.calevents[ev]['text'][0:17] + '\n'
                    
                        if(len(ev_ids)>3):
                            text = text+'...'
                            
                        label.configure(text=text)
                else:
                    label.configure(text='', style=style)

    def _display_days_with_othermonthdays(self):
        year, month = self._date.year, self._date.month

        cal = self._cal.monthdatescalendar(year, month)

        next_m = month + 1
        y = year
        if next_m == 13:
            next_m = 1
            y += 1
        if len(cal) < 6:
            if cal[-1][-1].month == month:
                i = 0
            else:
                i = 1
            cal.append(self._cal.monthdatescalendar(y, next_m)[i])
            if len(cal) < 6:
                cal.append(self._cal.monthdatescalendar(y, next_m)[i + 1])

        week_days = {i: 'normal' for i in range(7)}  # style names depending on the type of day
        week_days[self['weekenddays'][0] - 1] = 'we'
        week_days[self['weekenddays'][1] - 1] = 'we'
        prev_m = (month - 2) % 12 + 1
        months = {month: '.%s.TLabel' % self._style_prefixe,
                  next_m: '_om.%s.TLabel' % self._style_prefixe,
                  prev_m: '_om.%s.TLabel' % self._style_prefixe}

        week_nb = cal[0][1].isocalendar()[1]
        modulo = max(week_nb, 52)
        for i_week in range(6):
            self._week_nbs[i_week].configure(text=str((week_nb + i_week - 1) % modulo + 1))
            for i_day in range(7):
                style = week_days[i_day] + months[cal[i_week][i_day].month]
                label = self._calendar[i_week][i_day]
                label.state(['!disabled'])
                txt = str(cal[i_week][i_day].day)
                label.configure(text=txt, style=style)
                if cal[i_week][i_day] in self._calevent_dates:
                    date = cal[i_week][i_day]
                    ev_ids = self._calevent_dates[date]
                    i = len(ev_ids) - 1
                    while i >= 0 and not self.calevents[ev_ids[i]]['tags']:
                        i -= 1
                    if i >= 0:
                        tag = self.calevents[ev_ids[i]]['tags'][-1]
                        label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))

                    taglist_show=[]
                    for item in ev_ids:
                        if(self.calevents[item]['tags'] not in taglist_show):
                                taglist_show.append(self.calevents[item]['tags'])

                    if len(taglist_show) > 1:
                        label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))

                    # modified lines:
                    #text = '%s\n' % date.day + '\n'.join([self.calevents[ev]['text'][0:17] for ev in ev_ids])
                    text = str(date.day)+'\n'
                    for ev in ev_ids[0:2]:
                        text = text + self.calevents[ev]['text'][0:17] + '\n'
                    
                    if(len(ev_ids)>3):
                        text = text+'...'
                        
                    label.configure(text=text)
            
    def _on_click(self, event,option=0):
        """Select the day on which the user clicked."""
        #To clear Message bottom label:
        self.message_label.configure(text='')
        
        if self._properties['state'] == 'normal':
            if(option==1):
                self._remove_selection()
                self._display_selection()
                self.event_generate("<<CalendarSelected>>")
            else:
                label = event.widget
                if "disabled" not in label.state():
                    day = int(label.cget("text").split("\n")[0])
                    style = label.cget("style")
                    
                    
                    if option == 0:
                        if day > 20 and label in self._calendar[0]:
                            self._prev_month()
                        elif day < 10 and (label in self._calendar[4] or label in self._calendar[5]):
                            self._next_month()
                    
                    if day:
                        
                        if isinstance(day,str):
                            day = int(day.split("\n")[0])
                        day = int(day)
                        year, month = self._date.year, self._date.month
                        self._remove_selection()
                        self._sel_date = self.date(year, month, day)
                        self._display_selection()
                        if self._textvariable is not None:
                            self._textvariable.set(self.format_date(self._sel_date))
                        self.event_generate("<<CalendarSelected>>")

        #limpiamos el frame de tareas del dia seleccionado
        for widget_i in self.right_frame.winfo_children():
            widget_i.destroy()

        self.list_buttons.clear()
        
        #Mostramos las tareas del dia seleccionado
        selected_day_tasks = 0
        for event_id,ev in self.calevents.items():
            if (self._sel_date == ev['date']):
                if(ev['completed']==0):
                    task_font = self.normal_Font
                else:
                    task_font = self.completed_Font
                    
                #self.right_frame.rowconfigure(selected_day_tasks, weight=1)
                self.right_frame.columnconfigure(0, weight=1000)
                    
                #button_ch = Checkbutton(self.right_frame, text=ev['tags'][0]+": "+ev['text']  , font=('Segoe', 10) ,  bg = (self._tags[ev['tags'][0]]['background']), foreground='black')
                button_ch = Button(self.right_frame, command=lambda event_id=event_id: \
                    [self._CONTROLLER_complete_task(event_id,event)], \
                    text=ev['tags'][0]+": "+ev['text']  , font=task_font ,  \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1,pady=0,padx=0)
                button_ch.grid(row=selected_day_tasks,column=0, sticky='ew')#pack(fill=X)
                self.list_buttons.append(button_ch)
                
                Button(self.right_frame, command=lambda selected_day_tasks=selected_day_tasks: \
                    [self._CONTROLLER_show_description(event_id,event)], \
                    text="☰"  , font=self.icon_Font, \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1).grid(row=selected_day_tasks,column=1, sticky="ew",pady=0,padx=0)#pack(side=LEFT)
                
                
                Button(self.right_frame, command=lambda selected_day_tasks=selected_day_tasks: \
                    [self._CONTROLLER_edit_task(event_id,event)], \
                    text="✎"  , font=self.icon_Font, \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1).grid(row=selected_day_tasks,column=2, sticky="ew",pady=0,padx=0)#pack(side=LEFT)
                
                Button(self.right_frame, command=lambda selected_day_tasks=selected_day_tasks: \
                    [self._CONTROLLER_delete_task(event_id,event)], \
                    text="❌"  ,  font=self.icon_Font,\
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1).grid(row=selected_day_tasks,column=3, sticky="ew",pady=0,padx=0)#.pack(side=LEFT)
                
                """Button(self.right_frame, command=lambda selected_day_tasks=selected_day_tasks: \
                    [self._CONTROLLER_complete_task(selected_day_tasks)], \
                    text="edit"  ,  \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black').grid(row=selected_day_tasks,column=3, sticky="nsew")#.pack(side=LEFT)
                """
                selected_day_tasks += 1
                
                
                
        #button_ch.config(text="hello")
            
    
"""averaaa=self.left_frame.cget('borderwidth')
        self.left_frame.configure(borderwidth=self.left_frame.cget('borderwidth')+1)"""