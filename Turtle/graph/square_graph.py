from turtle import *

speed("fastest")
width(2)
color("blue")
up()

for x in range(-200, 200):
    if x == -199:
        down()
    y = (1/100) * x*x
    goto(x, y)

exitonclick()

