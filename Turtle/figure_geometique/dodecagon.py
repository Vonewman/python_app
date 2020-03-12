from turtle import *

width(5)
color("purple")
n = 12
angle = 360/n
for i in range(n):
    forward(100)
    left(angle)

exitonclick()
