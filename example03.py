from tkinter import *
from rgb import Colors
import random


TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=1)


exit_button = Button(root, text = "Exit")
add_button = Button(root, text = 'Add')

def close_window(event):
	TKroot.destroy()


def new_button_label(event):
    global row_
    def change_color(event):
            lab.config(bg = random.choice(tuple(Colors)))
            lab.config(fg = random.choice(tuple(Colors)))
                
    butt = Button(root, text = 'Button' + str(row_))
    butt.grid(row = row_, column = 0, sticky=E+W+S+N)
    lab = Label(root, text = 'Label' + str(row_))
    lab.grid(row = row_, column = 1, sticky=E+W+S+N)
    butt.bind('<Button-1>', change_color)
    row_ += 1

root.pack()

exit_button.bind('<Button-1>', close_window)
add_button.bind('<Button-1>', new_button_label)

row_ = 1 

exit_button.grid(row = 0, column = 1, ipadx = 10, sticky=E+W+S+N)
add_button.grid(row = 0, column = 0, ipadx = 10, ipady = 10, sticky=E+W+S+N)

TKroot.mainloop()

