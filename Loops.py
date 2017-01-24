"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
shape = turtle.Turtle()
shape.pu()
shape.left(90)
shape.forward(200)
shape.right(90)
shape.pd()
for i in range(150):
    shape.forward(10)
    shape.right(2.4)
input()
