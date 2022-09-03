from tkinter import *


def draw(event):
    global brushape
    r = 5
    xy = event.x - r, event.y - r, event.x + r, event.y + r

    if brushape == 'R':
        cnv.create_rectangle(xy, fill='black', outline='black')
    elif brushape == 'O':
        cnv.create_oval(xy, fill='black', outline='black')
    elif brushape == 'L':
        cnv.create_line(xy, fill='black')


window = Tk()
window.geometry('400x500')

cnv = Canvas(window)
cnv.pack(fill=BOTH, expand=1)
cnv.bind('<B1-Motion>', draw)

brushape = 'O'


class BrushButton(Button):
    master = window
    width = 5


class Brush:
    def __init__(self, shape):
        self.shape = shape

    def change_shape(self):
        global brushape, cnv
        cnv.config(cursor='cross')
        brushape = self.shape


BrushButton(text='o', command=Brush('O').change_shape).pack()
BrushButton(text='п', command=Brush('R').change_shape).pack()
BrushButton(text='///', command=Brush('L').change_shape).pack()

window.mainloop()





