from tkinter import *
from random import *

# tkinter window
root = Tk()


canvas = Canvas(root, width=400, height=200, background="while")
canvas.pack(fill="booth", expand=True)

# A rectangle
canvas.create_rectangle(50, 50, 150, 100, width=2)


# A rectangle with thick blue edges
canvas.create_rectangle(200, 50, 300, 150, width=5,outline="blue")

# A rectangle filled with purple

