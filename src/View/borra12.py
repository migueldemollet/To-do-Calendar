import tkinter as tk
my_w = tk.Tk()
my_w.geometry("400x300") 

f_done=('Times',22,'overstrike')
f_normal=('Times',22,'normal')

def my_upd(k): # k is the key of the reference dictionary 
    if(my_ref[k][1].get()==True): # checkbox is checked 
        my_ref[k][0].config(font=f_done,fg='green')
    else: # Checkbox is unchecked
        my_ref[k][0].config(font=f_normal,fg='blue')
    
l1=tk.Label(my_w,text='Task List',
	font=('Times',32,('bold','underline')),fg='red')
l1.grid(row=0,column=0,padx=5,pady=10)        
my_dict={'a':'My Task No 1','b':'My Task No 2','c':'My Task No 3'}
my_ref={} # Storing the references 
i=1 # row number ( after using 0 row number for Label at top)
for k in my_dict.keys(): # Number of checkbuttons or tasks 
    var=tk.BooleanVar() # variable connected to Checkbutton 
    ck = tk.Checkbutton(my_w, text=my_dict[k], 
    variable=var,onvalue=True,offvalue=False,font=f_normal,fg='blue',
        command=lambda k=k: my_upd(k))
    ck.grid(row=i,column=0,padx=80,pady=5,sticky='e') 

    my_ref[k]=[ck,var] # to hold the references 
    i=i+1 # increase the row number 

my_ref['b'][0].select()

my_w.mainloop()