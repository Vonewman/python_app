## We will use the module Turtle
## to draw a square. Here is a way to do that:
## - Move Forward
## - Turn Right
## - Move Forward
## - Turn Right
## - Move Forward
## - Turn Right
## - Move Forward
## - Turn Right

import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")


    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()


draw_square()
