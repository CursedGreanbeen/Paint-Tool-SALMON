from tkinter import *


def draw_oval(event):
    cnv.create_oval(event.x - 5,
                    event.y - 5,
                    event.x + 5,
                    event.y + 5,
                    fill='black',
                    outline='black')

def draw_rec(event):
    cnv.create_rectangle(event.x - 5,
                         event.y - 5,
                         event.x + 5,
                         event.y + 5,
                         fill='black',
                         outline='black')

window = Tk()
window.geometry('400x500')
cnv = Canvas(window)

cnv.pack(fill=BOTH, expand=1)
cnv.bind('<B1-Motion>', draw_oval)


class BrushButton(Button):
    master = window
    width = 5


BrushButton(text='o', command=draw_oval).pack()
BrushButton(text='п', command=draw_rec).pack()

window.mainloop()





