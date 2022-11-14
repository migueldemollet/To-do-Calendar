from tkcalendar import Calendar
from tkinter import *
import tkinter.font as tkFont
from tkinter.colorchooser import askcolor
from tkinter import ttk

import sys
sys.path.insert(1, 'Src/Controller/')
from tag_controller import *
from task_controller import *

class Popup(Toplevel):
    """modal window requires a master"""
    def __init__(self, master, **kwargs):
        Toplevel.__init__(self, master, **kwargs)

        lbl = Label(self, text="this is the popup")
        lbl.pack()

        btn = Button(self, text="OK", command=self.destroy)
        btn.pack()

        # The following commands keep the popup on top.
        # Remove these if you want a program with 2 responding windows.
        # These commands must be at the end of __init__
        self.transient(master) # set to be on top of the main window
        self.grab_set() # hijack all commands from the master (clicks on the main window are ignored)
        master.wait_window(self) # pause anything on the main window until this one closes


class Agenda(Calendar):
    def resize_frame(self, e):
        self.canvas.itemconfig(self._frame_id, height=e.height, width=e.width)
    def __init__(self, master=None,  **kw):
        self.master = master
        self.kw = kw
        self.id_user = kw['id_user']
        Calendar.__init__(self, self.master, **self.kw)


        self.carrega_interface()
       
    
    def carrega_interface(self):

        self.WINDOW_WIDTH = int(self.master.winfo_screenwidth()*90/100)
        self.WINDOW_HEIGHT = int(self.master.winfo_screenheight()*60/100)
        self.WINDOW_MARGIN_X = int((self.master.winfo_screenwidth()-self.WINDOW_WIDTH)/2)
        self.WINDOW_MARGIN_Y = int((self.master.winfo_screenheight()-self.WINDOW_HEIGHT-60)/2)
        
        self.master.geometry(str(self.WINDOW_WIDTH)+'x'+str(self.WINDOW_HEIGHT)+"+"+str(self.WINDOW_MARGIN_X)+"+"+str(self.WINDOW_MARGIN_Y)+"")
        
        
       
        self.normal_Font = tkFont.Font(family="Segoe", size=10, slant='roman', overstrike = 0)
        self.completed_Font = tkFont.Font(family="Segoe", size=10, slant='italic', overstrike = 1)
        self.italic_Font = tkFont.Font(family="Segoe", size=16, slant='italic')
        self.icon_Font = tkFont.Font(family="Console", size=10)
        self.alert_Font = tkFont.Font(family="Console", size=12)
        

        self.Controller_TAG = TagController()
        self.Controller_USER = UserController()
        self.Controller_TASK = TaskController()
        self.tag_config('mix',background='gainsboro',foreground='black')

                    
        self.message_label = Label(self.master, font=self.alert_Font, fg='red')
        self.message_label.pack(side=BOTTOM)

        self.task_frame = Frame(self.master, background="AliceBlue",
            borderwidth=15,  relief=RIDGE,
            width=self.WINDOW_WIDTH*0.2,
        )
        self.task_frame.pack(side=RIGHT,
            fill=BOTH, 
            expand=True,
            padx=20,
            pady=30
        )

        self.canvas = Canvas(self.task_frame)
        self.scrollbar = Scrollbar(self.task_frame, orient="vertical", command=self.canvas.yview)

        self.button_add_task = Button(self.task_frame,text=" [ + ]  Create new task", \
                                    command= lambda : [self.add_task()])
        self.button_add_task["bg"] = "azure2"
        self.button_add_task["border"] = "4"
        self.button_add_task.pack()

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.right_frame = Frame(self.canvas)
        self.right_frame.pack(side=LEFT,fill=BOTH,expand=True)

        self.right_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self._frame_id = self.canvas.create_window((0, 0), window=self.right_frame, anchor="nw")
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.list_buttons_open_desc = {}
        self.list_desc = []

        # change a bit the options of the labels to improve display
        for i, row in enumerate(self._calendar):
            for j, label in enumerate(row):
                self._cal_frame.rowconfigure(i + 1, uniform=1)
                self._cal_frame.columnconfigure(j + 1, uniform=1)
                label.configure(justify="center", anchor="n", padding=(1, 4))
                
        self._CONTROLLER_getTags()
        self._CONTROLLER_getTasks()
        
        
        self._show_event(self.datetime.today())

        
        
        self._prev_month()
        self._next_month()
        self._on_click("<<CalendarSelected>>",1)
    
    def add_task(self):
        self.top_create_task = Toplevel() 
        #self.top_create_task.geometry("800x400+500+200") 
        self.top_create_task.geometry("+500+200")
        self.top_create_task.title("Crea una tasca") 

        self.top_create_task.transient(self.master)
        self.top_create_task.grab_set()

        left_frame = Frame(self.top_create_task)
        left_frame.pack(side=LEFT,padx=20,pady=20)

        rightt_frame = Frame(self.top_create_task)
        rightt_frame.pack(side=RIGHT,padx=20,pady=20, expand=True, fill=BOTH)

        variable = IntVar(self.top_create_task)   
        tags = self.Controller_TAG.get_by_user(self.id_user)
        
        for num,tag in enumerate(tags):
            checkbutton = Checkbutton(
                left_frame,
                onvalue=tag.id,
                variable=variable,
                text=tag.name,
                bg=tag.color,
                font=self.normal_Font
            )
            checkbutton.pack(expand=True,fill=BOTH)

        
        new_tag_but = Button(left_frame,text="[+] Nou tag", command=lambda : [self._create_tag()])
        new_tag_but.pack(expand=True,fill=BOTH)


        

        self.info_message_tl = Label(rightt_frame,text="",fg='red')
        self.info_message_tl.grid(row=0)

        l1 = Label(rightt_frame,  text='Nova tasca', width=10 ) 
        l1.grid(row=1,column=1) 
        self.entry_task_name_tl = Entry(rightt_frame, width=100) 
        self.entry_task_name_tl.grid(row=1,column=2)


        l2 = Label(rightt_frame,  text='Descripció', width=10 ) 
        l2.grid(row=2,column=1) 
        self.text_task_description_tl = Text(rightt_frame, height=4) 
        self.text_task_description_tl.grid(row=2,column=2,pady=10)


        b2 = Button(rightt_frame, text='Crea la tasca',
                command=lambda: self._CONTROLLER_create_task(self.entry_task_name_tl.get(),self.text_task_description_tl.get("1.0",'end'),variable.get()) )
        b2.grid(row=3,column=2) 
        b3 = Button(rightt_frame, text='Cancel·la',command=self.top_create_task.destroy)
        b3.grid(row=4,column=2)

        # A Label widget to show in toplevel 
        #print(self.get_date())

    def _CONTROLLER_create_task(self,name,description,id_tag):
        

        mes,dia,any = self.get_date().split('/')
        any = '20' + any
        data = dia+'/'+mes+'/'+any


        return_value = self.Controller_TASK.add(Task(999,name,description,0,data,1,'red',self.Controller_TAG.get_by_id(id_tag),self.Controller_USER.get_by_id(self.id_user)))
        """        Task(id: int, name: str, description: str, state: str, date: str, priority: int, color: str, tag: Tag, user: User, user_shared: Any = []) -> None)"""

        """dia,mes,any = self.get_date().split('/')
        date_task=datetime.date(year=int(any), month=int(mes), day=int(dia))"""
        
        if(return_value == True):
            task_id_c = self.Controller_TASK.get_by_name(name,self.id_user).id
            date_task=datetime.date(year=int(any), month=int(mes), day=int(dia))

            self.calevent_create(date_task, name, description,0,1,task_id_c,self.Controller_TAG.get_by_id(id_tag).name)
            self.top_create_task.destroy()
            self._on_click("<<CalendarSelected>>",1)
            self._prev_month()
            self._next_month()
            

    def _create_tag(self, var1 = -1):
        def canvia_fons():
            self.color12 = askcolor(title="Tria color fons")[1]
            entry_tag_name_tl2.configure({"background": self.color12})

        self.color12 = '#a0a0a0'
        self.top_create_tag = Toplevel() 
        #self.top_create_task.geometry("800x400+500+200") 
        self.top_create_tag.geometry("+500+200")
        self.top_create_tag.title("Crea una tag") 

        self.top_create_tag.transient(self.master)
        self.top_create_tag.grab_set()

        top_frame = Frame(self.top_create_tag)
        top_frame.pack(side=LEFT,padx=20,pady=20)

        entry_tag_name_tl2 = Entry(top_frame, width=20,font=self.italic_Font, justify='center') 
        entry_tag_name_tl2.grid(row=0,column=1)


        b2 = Button(top_frame, text='Fons',
                command=lambda: canvia_fons())
        b2.grid(row=0,column=0, sticky='nswe',pady=5) 

        #colors = askcolor(title="Tkinter Color Chooser")
        if var1 == -1:
            b2 = Button(top_frame, text='Crea el tag',
                command=lambda: self._CONTROLLER_create_tag(entry_tag_name_tl2.get(),self.color12))
        else:
            b2 = Button(top_frame, text='Crea el tag',
                command=lambda: self._CONTROLLER_create_tag(entry_tag_name_tl2.get(),self.color12,var1))
        
        b2.grid(row=3,column=1,pady=5) 
        b3 = Button(top_frame, text='Cancel·la',command=self.top_create_tag.destroy)
        b3.grid(row=4,column=1,pady=5)

    def _CONTROLLER_create_tag(self,name,color,var2=-1):
        print(color)
        self.Controller_TAG.add(Tag(999,name,color,self.Controller_USER.get_by_id(self.id_user)))
        self.tag_config(name, background=color, foreground='black')
        self.top_create_tag.destroy()
        if var2 == -1:
            self.top_create_task.destroy()
            self.add_task()
        else:
            self.top_edit_task.destroy()
            self._edit_task(var2)

    def _CONTROLLER_complete_task(self,ev_id,event):
        if(self.calevents[ev_id]['completed'] == 0):
            self.calevents[ev_id]['completed'] = 1
            self.Controller_TASK.change_state(self.Controller_TASK.get_by_id(self.calevents[ev_id]['taskid']),1)
        else:
            self.calevents[ev_id]['completed'] = 0
            self.Controller_TASK.change_state(self.Controller_TASK.get_by_id(self.calevents[ev_id]['taskid']),0)
       
        self._on_click(event,1)
        
        

    def _CONTROLLER_show_description(self,ev_id,selected_day_num,event):
        #calc_position = int(selected_day_num / 2)
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
            T = Text(self.right_frame, height = 5, width = 44)
            T.grid(row=selected_day_num*2+1,column=0, columnspan=4)
            T.insert(END, self.calevents[ev_id]['descripcion'])
            self.list_desc.append(T)
            self.list_buttons_open_desc[selected_day_num]=1

        self.message_label.configure(text='')

        
    def _edit_task(self,event_id):
        self.top_edit_task = Toplevel() 
        #self.top_edit_task.geometry("800x400+500+200") 
        self.top_edit_task.geometry("+500+200")
        self.top_edit_task.title("Edita la tasca") 

        self.top_edit_task.transient(self.master)
        self.top_edit_task.grab_set()

        left_frame_edit = Frame(self.top_edit_task)
        left_frame_edit.pack(side=LEFT,padx=20,pady=20)

        right_frame_edit = Frame(self.top_edit_task)
        right_frame_edit.pack(side=RIGHT,padx=20,pady=20, expand=True, fill=BOTH)

        self.variable2 = IntVar(self.top_edit_task)   
        tags = self.Controller_TAG.get_by_user(self.id_user)
        list_checks = {}
        list_checks = []
        

        for tag in tags:
            checkbutton_ed = Checkbutton(
                left_frame_edit,
                onvalue=tag.id,
                offvalue=False,
                variable=self.variable2,
                text=tag.name,
                background=tag.color,
                font=self.normal_Font
            )
            #list_checks[tag.id]=[checkbutton_ed,tag.name]
            list_checks.append(checkbutton_ed)
            checkbutton_ed.pack(expand=True,fill=BOTH)
              


        
        task_name = self.Controller_TASK.get_by_name(self.calevents[event_id]['text'],self.id_user).name
        tag_id = self.Controller_TAG.get_by_name(self.calevents[event_id]['tags'][0],self.id_user)[0].id
        tag_text = self.Controller_TAG.get_by_name(self.calevents[event_id]['tags'][0],self.id_user)[0].name


        for chk_but in list_checks:
            tag_chk = chk_but.cget("text")
            elonvalue = chk_but.cget("onvalue")

            if(chk_but.cget("text")==tag_text):
                chk_but.select()
                tag_name_mod = chk_but.cget("text")
                tag_id_mod = chk_but.cget("onvalue")
                break

        #list_checks[1].configure(variable=1)
        
        

        
        new_tag_but_edit = Button(left_frame_edit,text="[+] Nou tag", command=lambda : [self._create_tag(event_id)])
        new_tag_but_edit.pack(expand=True,fill=BOTH)


        

        self.info_edit = Label(right_frame_edit,text="",fg='red')
        self.info_edit.grid(row=0)

        l1 = Label(right_frame_edit,  text='Nom tasca', width=10 ) 
        l1.grid(row=1,column=1) 
        self.entry_task_name_edit = Entry(right_frame_edit, width=100) 
        self.entry_task_name_edit.grid(row=1,column=2)
        self.entry_task_name_edit.insert(0, self.calevents[event_id]['text'])


        l2 = Label(right_frame_edit,  text='Descripció', width=10 ) 
        l2.grid(row=2,column=1) 
        self.text_task_description_edit = Text(right_frame_edit, height=4) 
        self.text_task_description_edit.grid(row=2,column=2,pady=10)
        self.text_task_description_edit.insert(INSERT, self.calevents[event_id]['descripcion'])


        b2 = Button(right_frame_edit, text='Guardar canvis',
                command=lambda: self._CONTROLLER_modify_changes(event_id,self.entry_task_name_edit.get(),self.text_task_description_edit.get("1.0",'end'),list_checks[self.variable2.get()-1].cget("onvalue"),list_checks[self.variable2.get()-1].cget("text"),task_name) )
        b2.grid(row=3,column=2) 
        b3 = Button(right_frame_edit, text='Cancel·la',command=self.top_edit_task.destroy)
        b3.grid(row=4,column=2)

    def _CONTROLLER_modify_changes(self,event_id,event_name,event_description,tag_id,tag_text,task_name):
        
        """th_task = self.Controller_TASK.get_by_id(event_id)
        th_task = Task(event_id,event_name,event_description,0,'01/11/2022',1,'#121212',Tag())"""

        th_task = self.Controller_TASK.get_by_name(task_name,self.id_user)

        

        self.Controller_TASK.change_description(th_task,event_description)
        self.Controller_TASK.change_name(th_task,event_name)
        self.Controller_TASK.change_tag(th_task,tag_id)

        self.calevents[event_id]['tags'][0] = tag_text
        self.calevents[event_id]['descripcion'] = event_description
        self.calevents[event_id]['text'] = event_name

        self.top_edit_task.destroy()
        self._on_click('<<CalendarSelected>>',1)
        
        
    def _CONTROLLER_delete_task(self,event_id,event):
        hi =self.calevents[event_id]
        self.Controller_TASK.delete_by_id(self.calevents[event_id]['taskid'])

        self.calevent_remove(event_id)

        self._prev_month()
        self._next_month()


        self._on_click(event,1)


        
     
    def _CONTROLLER_getTags(self):
        for tag in self.Controller_TAG.get_by_user(self.id_user):
            self.tag_config(tag.name, background=tag.color, foreground='black')
        """self.tag_config('UNIVERSITAT', background='DarkOliveGreen1', foreground='black')
        self.tag_config('TRABAJO', background='bisque', foreground='black')
        self.tag_config('mix',background='grey',foreground='black')"""
        
       
        
    def _CONTROLLER_getTasks(self):
        date = self.datetime.today()# + self.timedelta(days=2)

        for task in self.Controller_TASK.get_by_user(self.id_user):
            dia,mes,any = task.date.split('/')
            date_task=datetime.date(year=int(any), month=int(mes), day=int(dia))
            


            self.calevent_create(date_task, task.name, task.description,task.state,task.priority,task.id,self.Controller_TAG.get_by_id(task.tag.id).name)
            
    
    
    
    def _show_event(self, date):
        """Display events on date if visible."""
        w, d = self._get_day_coords(date)
        if w is not None:
            label = self._calendar[w][d]
            label.configure(width=25)
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

                
                

            taglist_show=[]
            for item in ev_ids:
                if(self.calevents[item]['tags'] not in taglist_show and self.calevents[item]['completed']==0):
                        taglist_show.append(self.calevents[item]['tags'])

            if len(taglist_show) > 1:
                label.configure(style='tag_%s.%s.TLabel' % ('mix', self._style_prefixe))

            if len(taglist_show) == 0:
                if w is not None:
                    week_end = [0, 6] if self['firstweekday'] == 'sunday' else [5, 6]
                    if d in week_end:
                        label.configure(style='we.%s.TLabel' % self._style_prefixe)
                    else:
                        label.configure(style='normal.%s.TLabel' % self._style_prefixe)
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

                    text = str(date.day)+'\n'

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
        self.calevents[ev_id] = {'date': date, 'text': text, 'tags': tags_, 'descripcion':description.replace('\n',''), 'completed':state, 'priority':priority, 'taskid':taskid}
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
                self.canvas.yview_moveto(0)
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

        self.list_buttons_open_desc.clear()
        
        #Mostramos las tareas del dia seleccionado
        selected_day_tasks = 0

        #self.canvas.yview_moveto(1)

        for event_id,ev in self.calevents.items():
            if (self._sel_date == ev['date']):
                if(ev['completed']==0):
                    task_font = self.normal_Font
                else:
                    task_font = self.completed_Font
                    
                self.right_frame.columnconfigure(0, weight=1000)

                n_pos = 90 - len(self.calevents[event_id]['text'])-len(self.calevents[event_id]['tags'][0])
                
                    
                button_ch = Button(self.right_frame, highlightthickness=4, 
                       activebackground="#ffffff", activeforeground="#000000", relief="raised",  bd=4, command=lambda event_id=event_id: \
                    [self._CONTROLLER_complete_task(event_id,event)], \
                    text=ev['tags'][0]+": "+ev['text'][0:n_pos]  , font=task_font ,  \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1,pady=0,padx=0)
                button_ch.grid(row=selected_day_tasks*2,column=0, sticky='ew')
                
                b1=Button(self.right_frame, highlightthickness=4, 
                       activebackground="#ffffff", activeforeground="#000000", relief="raised",  bd=4,  command=lambda event_id=event_id,selected_day_tasks=selected_day_tasks: \
                    [self._CONTROLLER_show_description(event_id,selected_day_tasks,event)], \
                    text="☰"  , font=self.icon_Font, \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1).grid(row=selected_day_tasks*2,column=1, sticky="ew",pady=0,padx=0)#pack(side=LEFT)
                self.list_buttons_open_desc[selected_day_tasks]=0
                
                b2=Button(self.right_frame, highlightthickness=4, 
                       activebackground="#ffffff", activeforeground="#000000", relief="raised",  bd=4,  command=lambda event_id=event_id: \
                    [self._edit_task(event_id)], \
                    text="✎"  , font=self.icon_Font, \
                    bg = (self._tags[ev['tags'][0]]['background']), foreground='black', height=1).grid(row=selected_day_tasks*2,column=2, sticky="ew",pady=0,padx=0)#pack(side=LEFT)
                
                b3=Button(self.right_frame, highlightthickness=4, 
                       activebackground="#ffffff", activeforeground="#000000", relief="raised",  bd=4,  command=lambda event_id=event_id: \
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




