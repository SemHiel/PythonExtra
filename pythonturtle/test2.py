import turtle
import math

sem = turtle.Turtle()
sem.color("red", "yellow")
sem.speed(10)

sem.begin_fill()
for i in range(100):
    sem.forward(300)
    sem.left(170)

sem.end_fill()
turtle.done()
