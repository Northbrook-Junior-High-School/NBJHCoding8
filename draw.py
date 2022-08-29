import random
from turtle import *
colors = ['blue', 'purple', 'cyan', 'white', 'yellow', 'green', 'orange']
shape("turtle")
speed(10)
pensize(6)
Screen().bgcolor("turquoise")
def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)
def snowflakearm():
    for i in range(4):
        forward(30)
        vshape()
    backward(120)
def snowflake():
    for i in range(6):
        colora = (random.choice(colors))
        color(colora)
        colors.remove(colora)
        snowflakearm()
        right(60)
snowflake()
mainloop()