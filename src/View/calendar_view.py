from tkcalendar import Calendar
from tkinter import *
import tkinter.font as tkFont
from Controller.tag_controller import *
from Controller.task_controller import *



class Agenda(Calendar):

    def __init__(self, master=None,  **kw):
        
        self.WINDOW_WIDTH = int(master.winfo_screenwidth()*80/100)
        self.WINDOW_HEIGHT = int(master.winfo_screenheight()*60/100)
        self.WINDOW_MARGIN_X = int((master.winfo_screenwidth()-self.WINDOW_WIDTH)/2)
        self.WINDOW_MARGIN_Y = int((master.winfo_screenheight()-self.WINDOW_HEIGHT-60)/2)
        
        master.geometry(str(self.WINDOW_WIDTH)+'x'+str(self.WINDOW_HEIGHT)+"+"+str(self.WINDOW_MARGIN_X)+"+"+str(self.WINDOW_MARGIN_Y)+"")
        
        print(self.WINDOW_HEIGHT)
        print(self.WINDOW_WIDTH)
        
        Calendar.__init__(self, master, **kw)
        self.normal_Font = tkFont.Font(family="Segoe", size=10, slant='roman', overstrike = 0)
        self.completed_Font = tkFont.Font(family="Segoe", size=10, slant='italic', overstrike = 1)
        self.icon_Font = tkFont.Font(family="Console", size=10)
        self.alert_Font = tkFont.Font(family="Console", size=12)
        

        self.Controller_TAG = TagController()
        self.Controller_TASK = TaskController()

        self.tag_config('mix',background='grey',foreground='black')
        self._CONTROLLER_getTags()
        self._CONTROLLER_getTasks()
              
        #self._sel_date=self.datetime.today()
        #self._show_event(self._sel_date)

        
        
        
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
            width=self.WINDOW_WIDTH*0.2,
        )
        self.right_frame.pack(side=RIGHT,
            fill=BOTH, 
            expand=True,
            padx=20,
            pady=30
        ) 
        
        #self.top= Toplevel(self.right_frame)
        #self.top.geometry("200x100+"+str(int(self.WINDOW_WIDTH+self.WINDOW_MARGIN_X/2)-200)+"+"+str(int(self.WINDOW_HEIGHT+self.WINDOW_MARGIN_Y/2)-400)+"")
        
        self.list_buttons = []
        self.list_buttons_open_desc = {}

        self.list_desc = []

        """self.sb = Scrollbar(master, command=self.right_frame.yview)
        self.sb.pack(side="right")
        self.right_frame.configure(yscrollcommand=self.sb.set)"""
        
        

        

        # change a bit the options of the labels to improve display
        for i, row in enumerate(self._calendar):
            for j, label in enumerate(row):
                self._cal_frame.rowconfigure(i + 1, uniform=1)
                self._cal_frame.columnconfigure(j + 1, uniform=1)
                label.configure(justify="center", anchor="n", padding=(1, 4))
                
        self._prev_month()
        self._next_month()
    
    
  
    def _CONTROLLER_complete_task(self,ev_id,event):
        if(self.calevents[ev_id]['completed'] == 0):
            self.calevents[ev_id]['completed'] = 1
            self.Controller_TASK.change_state(self.Controller_TASK.get_by_id(self.calevents[ev_id]['taskid']),1)
        else:
            self.calevents[ev_id]['completed'] = 0
            self.Controller_TASK.change_state(self.Controller_TASK.get_by_id(self.calevents[ev_id]['taskid']),0)
       
        self._on_click(event,1)
        
        

    def _CONTROLLER_show_description(self,ev_id,selected_day_num,event):
        for i in self.list_desc:
            i.destroy()

        self.list_desc.clear()
        
        if (self.list_buttons_open_desc[selected_day_num]):
            self.list_buttons_open_desc[selected_day_num]=0
            for i in self.list_desc:
                i.destroy()

            self.list_desc.clear()
        else:
            for id in self.list_buttons_open_desc.keys():
                self.list_buttons_open_desc[id] = 0

            #self.top.title(self.calevents[ev_id]['text'])
            T = Text(self.right_frame, height = 5, width = 52)
            T.grid(row=selected_day_num*2+1,column=0, columnspan=4,sticky='ew')
            T.insert(END, self.calevents[ev_id]['descripcion'])
            self.list_desc.append(T)
            self.list_buttons_open_desc[selected_day_num]=1

        self.message_label.configure(text='')

        """self.message_label.configure(text='NOT IMPLEMENTED!')
        self.update()"""
        
    def _CONTROLLER_edit_task(self,event_id,event):
        self.message_label.configure(text='NOT IMPLEMENTED!')
        self.update()
        
        
    def _CONTROLLER_delete_task(self,event_id,event):
        hi =self.calevents[event_id]
        self.Controller_TASK.delete_by_id(self.calevents[event_id]['taskid'])

        self.calevent_remove(event_id)

        self._prev_month()
        self._next_month()

        """self.update()"""

        self._on_click(event,1)


        
     
    def _CONTROLLER_getTags(self):
        for tag in self.Controller_TAG.get_by_user(1):
            self.tag_config(tag.name, background=tag.color, foreground='black')

        """self.tag_config('UNIVERSITAT', background='DarkOliveGreen1', foreground='black')
        self.tag_config('TRABAJO', background='bisque', foreground='black')
        self.tag_config('mix',background='grey',foreground='black')"""
        
       
        
    def _CONTROLLER_getTasks(self):
        date = self.datetime.today()# + self.timedelta(days=2)

        for task in self.Controller_TASK.get_by_user(1):
            dia,mes,any = task.date.split('/')
            date_task=datetime.date(year=int(any), month=int(mes), day=int(dia))
            self.calevent_create(date_task, task.name, task.description,task.state,task.priority,task.id,self.Controller_TAG.get_by_id(task.tag.id).name)
            
    
        """   self.calevent_create(date + self.timedelta(days=-7), 'Trabajo TQS', 'UNIVERSITAT')
        self.calevent_create(date + self.timedelta(days=3), 'Llamar al delegado!!', 'tag2')"""

        
        """for event_id,ev in self.calevents.items():
            if(event_id%2 == 0):
                ev['completed'] = 0
            else:
                ev['completed'] = 1
            """
    
    
    
    def _show_event(self, date):
        """Display events on date if visible."""
        w, d = self._get_day_coords(date)
        if w is not None:
            label = self._calendar[w][d]
            label.configure(width=15)
            if not label.cget('text'):
                # this is an other month's day and showothermonth is False
                return
            ev_ids = {}

            if date in self._calevent_dates:
                ev_ids = self._calevent_dates[date]

            for x in range(len(ev_ids)):
                if self.calevents[ev_ids[x]]['completed']==0 and self.calevents[ev_ids[x]]['tags']:
                    tag = self.calevents[ev_ids[x]]['tags'][-1]
                    label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))
                    break


            """i = len(ev_ids) - 1
            while i >= 0 and not self.calevents[ev_ids[i]]['tags']:
                ' and self.calevents[ev_ids[i]]['completed']==1:'
                i -= 1
                

            if i >= 0:
                tag = self.calevents[ev_ids[i]]['tags'][-1]
                if (self.calevents[ev_ids[i]]['completed']==0):
                    label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))"""

            
                
                

            taglist_show=[]
            for item in ev_ids:
                if(self.calevents[item]['tags'] not in taglist_show and self.calevents[item]['completed']==0):
                        taglist_show.append(self.calevents[item]['tags'])

            if len(taglist_show) > 1:
                label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))

            if len(taglist_show) == 0:
                #w, d = self._get_day_coords(label)
                if w is not None:
                    week_end = [0, 6] if self['firstweekday'] == 'sunday' else [5, 6]
                    if d in week_end:
                        label.configure(style='we.%s.TLabel' % self._style_prefixe)
                    else:
                        label.configure(style='normal.%s.TLabel' % self._style_prefixe)

                #label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))

            #if len(taglist_show) == 0:
                #label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))

            # modified lines:
            
            #text = '%s\n' % date.day + '\n'.join([self.calevents[ev]['text'][0:17] for ev in ev_ids])

            

            text = str(date.day)+'\n'

            events_uncompleted = 0
            for ev in ev_ids:
                if(self.calevents[ev]['completed']==0):
                    if(events_uncompleted < 3):
                        text = text + self.calevents[ev]['text'][0:17] + '\n'
                    events_uncompleted += 1
                
                    
            if(events_uncompleted>3):
                text = text+'...'


            label.configure(text=text)
        #else:

            
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

                        for x in range(len(ev_ids)):
                            if self.calevents[ev_ids[x]]['completed']==0 and self.calevents[ev_ids[x]]['tags']:
                                tag = self.calevents[ev_ids[x]]['tags'][-1]
                                label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))
                                break

                        """i = len(ev_ids) - 1
                        while i >= 0 and not (self.calevents[ev_ids[i]]['tags']):
                            i -= 1
                        if i >= 0:
                            tag = self.calevents[ev_ids[i]]['tags'][-1]
                            if (self.calevents[ev_ids[i]]['completed']==0):
                                label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))"""

                        taglist_show=[]
                        for item in ev_ids:
                            if(self.calevents[item]['tags'] not in taglist_show and self.calevents[item]['completed']==0):
                                    taglist_show.append(self.calevents[item]['tags'])

                        if len(taglist_show) > 1:
                            label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))
                        # modified lines:
                        #text = '%s\n' % day_number + '\n'.join([self.calevents[ev]['text'][0:17] for ev in ev_ids])
                        text = str(date.day)+'\n'
                        """for ev in ev_ids[0:3]:
                            text = text + self.calevents[ev]['text'][0:17] + '\n'
                    
                        if(len(ev_ids)>3):
                            text = text+'...'"""


                        events_uncompleted = 0
                        for ev in ev_ids:
                            if(self.calevents[ev]['completed']==0):
                                if(events_uncompleted < 3):
                                    text = text + self.calevents[ev]['text'][0:17] + '\n'
                                events_uncompleted += 1
                                        
                        if(events_uncompleted>3):
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
                    """i = len(ev_ids) - 1
                    while i >= 0 and not self.calevents[ev_ids[i]]['tags']:
                        i -= 1
                    if i >= 0:
                        tag = self.calevents[ev_ids[i]]['tags'][-1]
                        if (self.calevents[ev_ids[i]]['completed']==0):
                            label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))
                    """

                    for x in range(len(ev_ids)):
                        if self.calevents[ev_ids[x]]['completed']==0 and self.calevents[ev_ids[x]]['tags']:
                            tag = self.calevents[ev_ids[x]]['tags'][-1]
                            label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))
                            break

                    taglist_show=[]
                    for item in ev_ids:
                        if(self.calevents[item]['tags'] not in taglist_show and self.calevents[item]['completed']==0):
                                taglist_show.append(self.calevents[item]['tags'])

                    if len(taglist_show) > 1:
                        label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))

                    # modified lines:
                    #text = '%s\n' % date.day + '\n'.join([self.calevents[ev]['text'][0:17] for ev in ev_ids])
                    text = str(date.day)+'\n'
                    """for ev in ev_ids[0:3]:
                        text = text + self.calevents[ev]['text'][0:17] + '\n'
                    
                    if(len(ev_ids)>3):
                        text = text+'...'"""

                    events_uncompleted = 0
                    for ev in ev_ids:
                        if(self.calevents[ev]['completed']==0):
                            if(events_uncompleted < 3):
                                text = text + self.calevents[ev]['text'][0:17] + '\n'
                            events_uncompleted += 1
                            
                    if(events_uncompleted>3):
                        text = text+'...'

                    if(events_uncompleted==0):
                        text = str(date.day)+'\n'
                        
                    label.configure(text=text)

    def calevent_create(self, date, text, description, state, priority, taskid, tags=[]):
        
        """
        Add new event in calendar and return event id.

        Options:

            date : datetime.date or datetime.datetime
                event date

            text : str
                text to put in the tooltip associated to date.

            tags : list
                list of tags to apply to the event. The last tag determines
                the way the event is displayed. If there are several events on
                the same day, the lowest one (on the tooltip list) which has
                tags determines the colors of the day.
        """
        if isinstance(date, Calendar.datetime):
            date = date.date()
        if not isinstance(date, Calendar.date):
            raise TypeError("date option should be a %s instance" % (Calendar.date))
        if self.calevents:
            ev_id = max(self.calevents) + 1
        else:
            ev_id = 0
        if isinstance(tags, str):
            tags_ = [tags]
        else:
            tags_ = list(tags)
        self.calevents[ev_id] = {'date': date, 'text': text, 'tags': tags_, 'descripcion':description, 'completed':state, 'priority':priority, 'taskid':taskid}
        for tag in tags_:
            if tag not in self._tags:
                self._tag_initialize(tag)
        if date not in self._calevent_dates:
            self._calevent_dates[date] = [ev_id]
        else:
            self._calevent_dates[date].append(ev_id)
        if(self.calevents[ev_id]['completed']==0):
            self._show_event(date)
        return ev_id

    def _remove_selection(self):
        if self._sel_date is not None:
            buit = 1
            for id,ev in self.calevents.items():
                hi = ev['date']
                jo = self._sel_date
                if ev['date']==self._sel_date and ev['completed']==0:
                    buit = 0
                    break
            #if self._sel_date in self._calevent_dates and buit ==0:
            if self._sel_date in self._calevent_dates:
                self._show_event(self._sel_date)
            else:
                """w1, d1 = self._get_day_coords(self._date)
                self._calendar[w1][d1].configure(text=str(d1))"""
                w, d = self._get_day_coords(self._sel_date)
                if w is not None:
                    week_end = [0, 6] if self['firstweekday'] == 'sunday' else [5, 6]
                    if self._sel_date.month == self._date.month:
                        if d in week_end:
                            self._calendar[w][d].configure(style='we.%s.TLabel' % self._style_prefixe)
                        else:
                            self._calendar[w][d].configure(style='normal.%s.TLabel' % self._style_prefixe)
                    else:
                        if d in week_end:
                            self._calendar[w][d].configure(style='we_om.%s.TLabel' % self._style_prefixe)
                        else:
                            self._calendar[w][d].configure(style='normal_om.%s.TLabel' % self._style_prefixe)    


    def _get_next_event_id(self):
        return(len(self.calevents))

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
        self.list_buttons_open_desc.clear()
        
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
                button_ch.grid(row=selected_day_tasks*2,column=0, sticky='ew')#pack(fill=X)
                self.list_buttons.append(button_ch)
                
                Button(self.right_frame, command=lambda event_id=event_id,selected_day_tasks=selected_day_tasks: \
                    [self._CONTROLLER_show_description(event_id,selected_day_tasks,event)], \
                    text="☰"  , font=self.icon_Font, \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1).grid(row=selected_day_tasks*2,column=1, sticky="ew",pady=0,padx=0)#pack(side=LEFT)
                self.list_buttons_open_desc[selected_day_tasks]=0
                
                Button(self.right_frame, command=lambda selected_day_tasks=selected_day_tasks: \
                    [self._CONTROLLER_edit_task(event_id,event)], \
                    text="✎"  , font=self.icon_Font, \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1).grid(row=selected_day_tasks*2,column=2, sticky="ew",pady=0,padx=0)#pack(side=LEFT)
                
                Button(self.right_frame, command=lambda event_id=event_id: \
                    [self._CONTROLLER_delete_task(event_id,event)], \
                    text="❌"  ,  font=self.icon_Font,\
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1).grid(row=selected_day_tasks*2,column=3, sticky="ew",pady=0,padx=0)#.pack(side=LEFT)
                
                """Button(self.right_frame, command=lambda selected_day_tasks=selected_day_tasks: \
                    [self._CONTROLLER_complete_task(selected_day_tasks)], \
                    text="edit"  ,  \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black').grid(row=selected_day_tasks,column=3, sticky="nsew")#.pack(side=LEFT)
                """
                selected_day_tasks += 1
                
                
                
        #button_ch.config(text="hello")
            
    
"""averaaa=self.left_frame.cget('borderwidth')
        self.left_frame.configure(borderwidth=self.left_frame.cget('borderwidth')+1)"""