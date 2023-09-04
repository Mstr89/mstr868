import turtle

def draw_heart():
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(100)
    turtle.circle(50, 180)
    turtle.right(90)
    turtle.circle(50, 180)
    turtle.forward(100)
    turtle.end_fill()

turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()


draw_heart()


turtle.penup()
turtle.goto(-70, -120)
turtle.write("Pedaret", font=("Arial", 16, "normal"))


turtle.done()
