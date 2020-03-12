from turtle import *
from math import *

speed("fastest")
width(3)
color("red")
up()


for x in range(-200, 200):
    if x == -199:
        down()
    y = 100*sin(1/20*x)
    goto(x, y)


exitonclick()
