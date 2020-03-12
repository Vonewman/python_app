from turtle import *

# A pentagone
width(5)
color('blue')

for i in range(5):
    forward(100)
    left(72)

# An other pentagone
color('red')

longueur = 200
angle = 72
for i in range(5):
    forward(longueur)
    left(angle)

# A dodecagone(12 edges)

color("purple")
n = 12
angle = 360/n
for i in range(n):
    forward(100)
    left(angle)


# A spiral

color("green")
length = 10
for i in range(25):
    forward(length)
    left(40)
    length = length + 40

exitonclick()
