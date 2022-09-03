from tkinter import *


def draw(event):
    global brushape
    r = 5
    xy = event.x - r, event.y - r, event.x + r, event.y + r

    if brushape == 'R':
        cnv.create_rectangle(xy, fill=color[1], outline=color[1])
    elif brushape == 'O':
        cnv.create_oval(xy, fill=color[1], outline=color[1])
    elif brushape == 'L':
        cnv.create_line(xy, fill=color[1])


window = Tk()
window.geometry('400x500')

cnv = Canvas(window, bg='white')
cnv.pack(fill=BOTH, expand=1)
cnv.bind('<B1-Motion>', draw)
cnv.config(cursor='cross')

brushape, color = 'O', (0, 'Black')


class BrushButton(Button):
    master = window
    width = 10


class Brush:
    def __init__(self, shape):
        self.shape = shape

    def change_shape(self):
        global brushape, cnv, color
        cnv.config(cursor='cross')
        brushape = self.shape
        color = (0, 'Black')


    def erase(self):
        global color, cnv
        cnv.config(cursor='circle')
        color = (0, 'White')


BrushButton(text='o', command=Brush('O').change_shape).pack()
BrushButton(text='п', command=Brush('R').change_shape).pack()
BrushButton(text='///', command=Brush('L').change_shape).pack()
BrushButton(text='er', command=Brush('').erase).pack()

window.mainloop()