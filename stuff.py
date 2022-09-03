from tkinter import *
from tkinter.colorchooser import askcolor


def draw(event):
    global brushape
    n, m = height_scl.get(), width_scl.get()
    xy = event.x - n, event.y - n, event.x + n, event.y + n

    if brushape == 'R':
        cnv.create_rectangle(xy, fill=color[1], outline=color[1])
    elif brushape == 'O':
        cnv.create_oval(xy, fill=color[1], outline=color[1])
    elif brushape == 'L':
        cnv.create_line(xy, fill=color[1])


brushape = 'O'
color, act_color, bg_color = (0, 'Black'), (0, 'Black'), (0, 'White')

# window
window = Tk()
window.geometry('600x500')
window.title('Paint Tool SASAI')

# working panes
toolbarPane = Frame(window)
brushPane = Frame(toolbarPane)
canvasPane = Frame(window, relief=RAISED, bd=3, cursor='cross')
toolbarPane.pack(side=LEFT)
brushPane.pack()
canvasPane.pack()

# canvas
wd, ht = 1500, 1500
cnv = Canvas(canvasPane, width=wd, height=ht, bg=bg_color[1])
cnv.pack()

cnv.bind('<B1-Motion>', draw)


class Brush:
    def __init__(self, shape):
        self.shape = shape

    def change_shape(self):
        global brushape, cnv, color, act_color
        cnv.config(cursor='cross')
        brushape = self.shape
        color = act_color

    def choose_color(self):
        global color, act_color
        act_color = askcolor('Blue')
        color = act_color

    def erase(self):
        global color, cnv
        cnv.config(cursor='circle')
        color = (0, 'White')


# tool buttons
Label(toolbarPane, text='\nTools', font=("Arial", 10, "bold"), width=15).pack()
Button(toolbarPane, text='Eraser', width=15, command=Brush('').erase).pack()
Button(toolbarPane, text='Color', width=15, command=Brush('').choose_color).pack()
Button(toolbarPane, text='Reset', width=15, command=lambda:cnv.delete('all')).pack()
# pipette_btn = Button(text='Pipette', command=get_color).pack()

# brush buttons
Label(brushPane, text='Brushes', font=("Arial", 10, "bold"), width=15).pack()
Button(brushPane, text='〇', width=5, command=Brush('O').change_shape).pack(side=LEFT)
Button(brushPane, text='☐', width=5, command=Brush('R').change_shape).pack(side=LEFT)
Button(brushPane, text='///', width=5, command=Brush('L').change_shape).pack(side=LEFT)

# parameters
Label(toolbarPane, text='\nHeight', font=("Arial", 10, "bold"), width=15).pack()
height_scl = Scale(toolbarPane, from_=0, to=100, width=15, orient=HORIZONTAL)
height_scl.pack()
Label(toolbarPane, text='\nWidth', font=("Arial", 10, "bold"), width=15).pack()
width_scl = Scale(toolbarPane, from_=0, to=100, width=15, orient=HORIZONTAL)
width_scl.pack()


window.mainloop()
