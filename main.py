import turtle
import time


def jobbra():
    fej.right(90)


def balra():
    fej.left(90)


# def fel():
#     fej


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(jobbra, "Right")
palya.onkey(balra, "Left")
# palya.onkey(fel, "Up")
# palya.onkey(le, "Down")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

while True:
    fej.forward(20)

    palya.update()
    time.sleep(0.3)
