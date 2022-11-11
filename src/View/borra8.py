import tkinter as tk

root = tk.Tk()

variable = tk.IntVar(root)

for onvalue in range(1, 5 + 1):
    checkbutton = tk.Checkbutton(
        root,
        onvalue=onvalue,
        variable=variable,
        text="hola"
    )
    checkbutton.pack()

root.mainloop()