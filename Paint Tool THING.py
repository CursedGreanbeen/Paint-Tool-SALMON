from tkinter import *
from PIL import Image, ImageTk, ImageGrab
from tkinter.colorchooser import askcolor


def choose_color():
    global color
    color = askcolor('Red')

# menu functions
def file():
    pass

def cnv_size():
    pass

def cnv_bg():
    global bg_color, canvasPane
    bg_color = askcolor('Red')
    cnv.config(bg=bg_color)

# tools
def erase():
    global color, bg_color, canvasPane
    color = bg_color
    canvasPane.config(cursor='circle')


def input_text():
    root = Tk()
    root.title('Text')
    root.geometry('200x200')

    enter_text = Entry(root)
    enter_text.place(relx=.5, rely=.1, anchor="c")

    def get_text():
        global cnv
        message = StringVar()
        cnv.create_text(150, 400, text=message.get(),
                        justify=CENTER, font=("Times", "40"))

    but = Button(root, text='OK', command=get_text)
    but.place(relx=.5, rely=.3, anchor='c')

    root.mainloop()


def get_color():
    pass

# brush settings
def choose_recBrush():
    global brushape, shape, canvasPane
    brushape, shape = 'R', ''
    canvasPane.config(cursor='cross')

def choose_ovalBrush():
    global brushape, shape, canvasPane
    brushape, shape = 'O', ''
    canvasPane.config(cursor='cross')

def choose_polyBrush():
    global brushape, shape, canvasPane
    brushape, shape = 'P', ''
    canvasPane.config(cursor='cross')

def brush(event):
    global brushape
    r = height_scl.get()
    xy = event.x - r, event.y - r, event.x + r, event.y + r

    if brushape == 'R':
        cnv.create_rectangle(xy, fill=color[1], outline=color[1])
    elif brushape == 'O':
        cnv.create_oval(xy, fill=color[1], outline=color[1])
    elif brushape == 'P':
        cnv.create_polygon(xy, fill=color[1], outline=color[1])


# shape settings
def choose_rectangle():
    global shape, brushape
    shape, brushape = 'R', ''

def choose_oval():
    global shape, brushape
    shape, brushape = 'O', ''

def choose_line():
    global shape, brushape
    shape, brushape = 'L', ''

def draw_shape(event):
    global shape
    w = width_scl.get()
    h = height_scl.get()
    xy = event.x - w/2, event.y - h/2, event.x + w/2, event.y + h/2

    if shape == 'R':
        cnv.create_rectangle(xy, fill=color[1], outline=color[1])
    elif shape == 'O':
        cnv.create_oval(xy, fill=color[1], outline=color[1])
    elif shape == 'L':
        cnv.create_line(xy, fill=color[1])

color, bg_color = (0, 'Black'), (0, 'White')
brushape, shape = 'O', ''

# window
window = Tk()
window.geometry('600x500')
window.title('Paint Tool THING')

# working panes
toolbarPane = Frame(window)
imagePane = Frame(toolbarPane)
brushPane = Frame(toolbarPane)
canvasPane = Frame(window, relief=RAISED, bd=3, cursor='cross')
toolbarPane.pack(side=LEFT)
imagePane.pack()
brushPane.pack()
canvasPane.pack()

# canvas
wd, ht = 500, 500
cnv = Canvas(canvasPane, width=wd, height=ht, bg=bg_color[1])
cnv.pack()

# menu
menu_bar = Menu(window)
cnv_manager = Menu(menu_bar)
window.config(menu=menu_bar)
menu_bar.add_command(label='File', command=file)
menu_bar.add_cascade(label='Canvas', menu=cnv_manager)
cnv_manager.add_command(label='Size', command=cnv_size)
cnv_manager.add_command(label='Background', command=cnv_bg)
menu_bar.add_command(label='Reset', command=lambda : cnv.delete('all'))

# tool buttons
tools_label = Label(toolbarPane, text='\nTools', font=("Arial", 10, "bold"), width=15)
eraser_btn = Button(toolbarPane, text='Eraser', width=15, command=erase)
text_button = Button(toolbarPane, text='Text', width=15, command=input_text)
pipette_btn = Button(toolbarPane, text='Pipette', width=15, command=get_color)

# brush buttons
brushes_lbl = Label(brushPane, text='Brushes', font=("Arial", 10, "bold"), width=15)
rec_brush_btn = Button(brushPane, text='☐', width=5, command=choose_recBrush)
oval_brush_button = Button(brushPane, text='〇', width=5, command=choose_ovalBrush)
poly_brush_btn = Button(brushPane, text='///', width=5, command=choose_polyBrush)

# shape buttons
shapes_lbl = Label(toolbarPane, text='\nShapes', font=("Arial", 10, "bold"), width=15)
rec_btn = Button(toolbarPane, text='Rectangle', width=15, command=choose_rectangle)
oval_btn = Button(toolbarPane, text='Oval', width=15, command=choose_oval)
line_btn = Button(toolbarPane, text='Line', width=15, command=choose_line)

# parameter buttons
col_btn = Button(toolbarPane, text='Color', width=15, command=choose_color)
height_lbl = Label(toolbarPane, text='\nHeight', font=("Arial", 10, "bold"), width=15)
height_scl = Scale(toolbarPane, from_=0, to=100, width=15, orient=HORIZONTAL)
width_lbl = Label(toolbarPane, text='\nWidth', font=("Arial", 10, "bold"), width=15)
width_scl = Scale(toolbarPane, from_=0, to=100, width=15, orient=HORIZONTAL)

# packpackpack
tools_label.pack()
eraser_btn.pack()
text_button.pack()
pipette_btn.pack()

brushes_lbl.pack()
rec_brush_btn.pack(side=LEFT)
oval_brush_button.pack(side=LEFT)
poly_brush_btn.pack(side=LEFT)

shapes_lbl.pack()
rec_btn.pack()
oval_btn.pack()
line_btn.pack()

col_btn.pack()
height_lbl.pack()
height_scl.pack()
width_lbl.pack()
width_scl.pack()

cnv.bind('<B1-Motion>', brush)
cnv.bind('<Button-1>', draw_shape)

window.mainloop()