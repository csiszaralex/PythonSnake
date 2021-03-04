import turtle
import time


def jobbra():
    fej.right(90)


def balra():
    fej.left(90)


def die():
    kijelzo = turtle.Turtle()
    kijelzo.hideturtle()
    kijelzo.color("white")
    kijelzo.goto(-30, 240)
    kijelzo.clear()
    kijelzo.write("Meghaltál!", font=("Arial", 35, "bold"), align="center")


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(jobbra, "Right")
palya.onkey(balra, "Left")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

while True:
    fej.forward(20)

    if abs(fej.xcor()) > 400 or abs(fej.ycor()) > 300:
        die()

    palya.update()
    time.sleep(0.3)
