from turtle import *
speed(0)
pensize(2)
bgcolor('black')
for i in range(6):
    for colours in ["red", 'magenta', "blue", "cyan", "green", "yellow", "white"]:
        color(colours)
        circle(100)
        left(10)
done()