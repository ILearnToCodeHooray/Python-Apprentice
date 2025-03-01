"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error


# TODO)
#   1. Create a turtle.
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

t = turtle.Turtle()   
def triangle():
    for i in range(3):
        t.left(120)
        t.forward(80)

def square():
    for i in range(4):
        t.left(90)
        t.forward(80)

def circle():
    for i in range(360):
        t.left(1)
        t.forward(1)

shape = input("What shape do you want to make?")
done = 1
while done == 1: 
    if shape == "triangle":
        triangle()
        done = 0
    elif shape == "square":
        square()
        done = 0
    elif shape == "circle":
        circle()
        done = 0
    else:
        shape = input("Please enter a real shape.")