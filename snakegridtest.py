from pygame import *

init()
window = display.set_mode((400, 400))

for y in range(200):
    for x in range(200):
        rect = Rect(x * 20, y * 20, 20, 20)
        draw.rect(window, (200, 200, 200), rect)
display.update()
