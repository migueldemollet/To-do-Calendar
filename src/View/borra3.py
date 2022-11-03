import tkinter as tk
import tkinter.font as tkFont
from tkinter import Tk, ttk, IntVar, Frame

class Application(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


        self.normal_Font = tkFont.Font(family="Helvetica", size=12, overstrike = 0)
        self.strike_Font = tkFont.Font(family="Helvetica", size=12, overstrike = 1)

        self.popup = Popup(self)


    '''When a checkbutton is checked, change the label to strikethrough and move it and
    the checkbox to the bottom (if unchecked). If checked, remove strikethrough.'''           



    def check_off(self, num):                 

        # If the checkbutton is NOT checked, change the font, but don't sort.
        if self.popup.button_vars[num].get() == 0:
            self.popup.checkbuttons[num]['font'] = self.normal_Font
            # Leave positions where they are (don't sort)
            return


        # Strikeout font.
        self.popup.checkbuttons[num]['font'] = self.strike_Font
        current_row = self.popup.checkbuttons[num].grid_info()['row']
        if current_row == len(self.popup.checkbuttons):
            # Already at the bottom. No movement required.
            return

        # Temporarily remove this checkbutton so it is not gridded.
        self.popup.checkbuttons[num].grid_remove()

        # Sort the remaining checkbuttons. Note that the grid_slaves
        # function returns slaves in the most recent grid order. This
        # means that [num] checkbutton is returned first in the list.
        order = {}
        for child in self.popup.grid_slaves():
            # Key is the sequence/index, value is the widget object.
            order[child.grid_info()['row']] = child

        for index,old_row in enumerate(sorted(order.keys())):
            order[old_row].grid(row=index + 1)
            print(order[old_row]['text'],index + 1)

        # Finally, regrid the checkbutton we removed earlier to the bottom.
        self.popup.checkbuttons[num].grid(row=len(self.popup.checkbuttons))


class Popup(tk.Toplevel):

    def __init__(self, controller):

        tk.Toplevel.__init__(self,controller)

        self.controller = controller     


        #self.checklist_labels = []
        self.checkbuttons = []
        self.button_vars = []


        #In the full version, these are created with the press of a button        
        self.checklist_details = ["A", "B", "C"]

        '''For each item in the checklist, create an IntVar, checkbuttons, labels for the checklists
       (checkbutton text can't be struckthrough) and grid them'''
        # Well, ttk.checkbuttons require themes to change their fonts, but tk.checkbuttons don't.
        # But in either case, you CAN change their font attributes.

        for i, item in enumerate(self.checklist_details):

            self.button_vars.append(IntVar())
            self.checkbuttons.append(tk.Checkbutton(self, variable = self.button_vars[i],
              onvalue = 1, offvalue = 0, command = lambda i=i: controller.check_off(i),
              text = item, font = controller.normal_Font))

            self.checkbuttons[i].grid(column = 0, row = i+1)
            
            
            
if __name__ == '__main__':

    root = Tk()
    root.withdraw()
    Application(root)
    root.mainloop()