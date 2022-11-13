from tkinter import *

class Widget(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self._str    = StringVar()
        self._widget = Entry(self)

        self._widget.config(textvariable=self._str, borderwidth=1, width=0)
        self._widget.pack(expand=True, fill=X)

    def settext(self, str_):
        self._str.set(str_)

    def gettext(self):
        return self._str.get()


class Application(Frame):
    def __init__(self, rows, cols, master=None):
        Frame.__init__(self, master)

        yScroll = Scrollbar(self)
        xScroll = Scrollbar(self, orient=HORIZONTAL)

        self._canvas = Canvas(self,
                yscrollcommand=yScroll.set, xscrollcommand=xScroll.set)
        yScroll.config(command=self._canvas.yview)
        xScroll.config(command=self._canvas.xview)

        self._table      = [[0 for x in range(rows)] for x in range(cols)]
        self._tableFrame = Frame(self._canvas)

        for col in range(cols):
            self._tableFrame.grid_columnconfigure(col, weight=1)
            for row in range(rows):
                self._table[row][col] = Widget(master=self._tableFrame)
                self._table[row][col].settext("(%d, %d)" % (row, col))
                self._table[row][col].grid(row=row, column=col, sticky=E+W)

        # For debugging
        self._canvas.config(background="blue")
        self._tableFrame.config(background="red")

        yScroll.pack(side=RIGHT, fill=Y)
        xScroll.pack(side=BOTTOM, fill=X)

        self._canvas.create_window(0, 0, window=self._tableFrame, anchor=N+W)
        self._canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self._frame_id = self._canvas.create_window(0, 0, window=self._tableFrame, anchor=N+W)
        self._canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self._canvas.bind("<Configure>", self.resize_frame)

    def resize_frame(self, e):
        self._canvas.itemconfig(self._frame_id, height=e.height, width=e.width)

tkRoot  = Tk()

# Application Size and Center the Application
appSize = (800, 600)
w       = tkRoot.winfo_screenwidth()
h       = tkRoot.winfo_screenheight()

x = w / 2 - appSize[0] / 2
y = h / 2 - appSize[1] / 2
tkRoot.geometry("%dx%d+%d+%d" % (appSize + (x, y)))
tkRoot.update_idletasks() # Force geometry update

app = Application(5, 5, master=tkRoot)
app.pack(side=TOP, fill=BOTH, expand=True)
tkRoot.mainloop()