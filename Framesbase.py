import tkinter as tk
from tkinter import *
from Interface import *
from config import *


def create_header_text(window):
    row = Label(window, text='Choisissez les dimensions de la grille', font=('arial', 10),
                justify='center', anchor='n')
    row.grid(row=0, columnspan=1, padx=5, pady=5)

def create_row_width(window):
    row = Label(window, text='Longueur de la grille : ')
    row.grid(row=1, column=0)
    width_scale = Scale(window, from_=50, to=150, orient="horizontal", variable=IntVar(), resolution=5)
    width_scale.grid(row=1, column=1)
    return width_scale

def create_row_height(window):
    row = Label(window, text='Hauteur de la grille : ')
    row.grid(row=2, column=0, pady=2)
    height_scale = Scale(window, from_=50, to=150, orient="horizontal", variable=IntVar(), resolution=5)
    height_scale.grid(row=2, column=1, pady=2)
    return height_scale

def create_button_validate(window, width_scale, height_scale):
    def validate_user_input():
        set_width_grid(width_scale.get())
        set_height_grid(height_scale.get())
        width_scale.config(state='disabled')
        height_scale.config(state='disabled')
        window.destroy()

    button = Button(window, text='Valider', command=validate_user_input)
    button.grid(row=3, column=2, sticky='se')

def getWidthGrid():
    return 

def show_start_frame():
    window = Tk()
    window.title('Langton grid')
    width = 500
    height = 300

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)

    window.geometry('%dx%d+%d+%d' % (width, height, x0, y0))
    window.resizable(False, False)

    create_header_text(window)
    width_scale = create_row_width(window)
    height_scale = create_row_height(window)
    create_button_validate(window, width_scale, height_scale)
    window.mainloop()