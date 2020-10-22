import turtle

sem = turtle.Turtle()
sem.getscreen().bgcolor("#994444")
sem.speed(100)
sem.penup()
sem.goto((-200,100))
sem.pendown()

def star(turtle, size):
	if size <= 10:
		return
	else:
		turtle.begin_fill()
		for i in range(5):

			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()

star(sem, 360)

turtle.done()
