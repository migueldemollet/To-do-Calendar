from tkinter import *
root = Tk()
root.geometry("250x100")
root.title("Root Window")
 
 
def open_popup(num):
   popup = Toplevel()
   popup.title("PopUp")
   popup.geometry("250x100")
   
   value = Entry(popup)
   value.place(height=25, width=25, x=100, y=10)
   value.insert(0, str(num))
   
   btn_ok = Button(popup, text="Return", command=popup.destroy)
   btn_ok.place(height=30, width=60, x=90, y=45)
   
   
   main_entry = Entry(root)
   main_entry.place(height=25, width=30, x=110, y=10)
   main_entry.insert(0, "111")
 
   button_ok = Button(
   root, text="OK", command=lambda: open_popup(main_entry.get()))
   button_ok.place(height=30, width=30, x=110, y=45)
 
root.mainloop()