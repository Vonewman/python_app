from turtle import *

width(5)
color('green')
length = 10
for i in range(25):
    forward(length)
    left(40)
    length = length + 10

exitonclick()
