import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.fillcolor("white")
turtle.begin_fill()

for x in range(36):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(5)

turtle.end_fill()
turtle.done()
