import random
import turtle
from turtle import *
colors = ['blue', 'purple', 'cyan', 'white', 'yellow', 'green', 'orange']
colormode(255)
shape("turtle")
speed(10)
pensize(6)
Screen().bgcolor("black")
Screen().colormode('rgb')
turtle.screensize(400,400)
def vshape(size, turn):

    right(turn)
    forward(size)
    backward(size)
    left(turn*2)
    forward(size)
    backward(size)
    right(turn)
def snowflakearm(size):
    turn = random.randint(25, 90)
    for i in range(4):
        forward(size)
        vshape(size, turn+10)
    backward(size*4)
def snowflake():
    armcount= random.randint(3,16)
    size = random.randint(5,50)
    for i in range(armcount):
        snowflakearm(size)
        right(360/armcount)
while True:
    x = random.randint(-300,300)
    y = random.randint(-200,200)
#    size = random.randint(5,10)
    penup()
    goto(x,y)
    pendown()
    color([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    snowflake()
mainloop()