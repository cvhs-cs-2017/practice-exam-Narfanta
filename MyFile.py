import turtle
def shape(sides):
    poly = turtle.Turtle()
    poly.speed(0)
    poly.pu()
    poly.forward(200)
    poly.left(270)
    poly.pd()
    for i in range(sides):
        poly.forward(5)
        poly.right(360/sides)

shape(150)
input()
shape(200)
input()
