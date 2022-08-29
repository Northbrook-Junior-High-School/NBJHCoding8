import tkinter

print("To draw, hold down the left mouse button and move your mouse around.")
print("To change you brush color, click on on of the colors.")
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=750, height=500, bg='white')
canvas.pack()
lastX, lastY = 0, 0
color = 'black'


def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y


def on_click(event):
    store_position(event)


def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=color, width=3)
    store_position(event)


canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
red_id = canvas.create_rectangle(10, 10, 30, 30, fill='red')
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill='blue')
black_id = canvas.create_rectangle(10, 60, 30, 80, fill='black')
white_id = canvas.create_rectangle(10, 85, 30, 105, fill='white')
green_id = canvas.create_rectangle(10, 110, 30, 130, fill='green')
yellow_id = canvas.create_rectangle(10, 135, 30, 155, fill='yellow')

def set_color_red(event):
    global color
    color = 'red'


def set_color_blue(event):
    global color
    color = 'blue'


def set_color_black(event):
    global color
    color = 'black'


def set_color_white(event):
    global color
    color = 'white'

def set_color_green(event):
    global color
    color = 'green'

def set_color_yellow(event):
    global color
    color = 'yellow'


canvas.tag_bind(red_id, "<Button-1>", set_color_red)
canvas.tag_bind(blue_id, "<Button-1>", set_color_blue)
canvas.tag_bind(black_id, "<Button-1>", set_color_black)
canvas.tag_bind(white_id, "<Button-1>", set_color_white)
canvas.tag_bind(green_id, "<Button-1>", set_color_green)
canvas.tag_bind(yellow_id, "<Button-1>", set_color_yellow)
tkinter.mainloop()
