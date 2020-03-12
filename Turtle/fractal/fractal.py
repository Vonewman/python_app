from turtle import *

width(5)
up()
goto(-100, -100)
down()

for i in range(3):
    color("blue")
    forward(256)
    left(120)
    
    for i in range(3):
        color("red")
        forward(128)
        left(120)
        
        for i in range(3):
            color("green")
            forward(68)
            left(120)
            
            for i in range(3):
                color("orange")
                forward(34)
                left(120)

exitonclick()
