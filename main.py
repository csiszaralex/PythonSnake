import turtle
import time
from random import randint

height = 600
width = 800
pont = 0


def jobbra():
    fej.right(90)


def balra():
    fej.left(90)


def die():
    pontszam.clear()
    kijelzo = turtle.Turtle()
    kijelzo.hideturtle()
    kijelzo.color("white")
    kijelzo.goto(-30, 240)
    kijelzo.clear()
    kijelzo.write("Meghaltál!", font=("Arial", 35, "bold"), align="center")
    turtle.done()


def gyumolcs_kirak():
    x = randint(-380, 380)
    y = randint(-280, 280)
    gyumolcs.goto(x, y)


def kiir():
    pontszam.clear()
    pontszam.write(f"{pont} pont", font=("Arial", 35, "bold"), align="center")


def ujTest(x, y):
    time.sleep(0.2)
    uj = turtle.Turtle()
    uj.shape("circle")
    uj.penup()
    uj.color("yellow")
    uj.goto(x, y)
    test.append(uj)


palya = turtle.Screen()
palya.setup(width=width, height=height)
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

gyumolcs = turtle.Turtle()
gyumolcs.penup()
gyumolcs.shape('circle')
gyumolcs.color('red')
gyumolcs_kirak()

pontszam = turtle.Turtle()
pontszam.hideturtle()
pontszam.color("white")
pontszam.goto(-30, 240)
pontszam.clear()

test = []
ujTest(fej.xcor(), fej.ycor())
ujTest(fej.xcor(), fej.ycor())
ujTest(fej.xcor(), fej.ycor())
ujTest(fej.xcor(), fej.ycor())
ujTest(fej.xcor(), fej.ycor())
ujTest(fej.xcor(), fej.ycor())
ujTest(fej.xcor(), fej.ycor())

while True:
    fejX = fej.xcor()
    fejY = fej.ycor()
    fej.forward(20)
    test[-1].goto(fejX, fejY)
    test = [test[-1]] + test[:-1]
    if fej.distance(gyumolcs.xcor(), gyumolcs.ycor()) < 20:
        pont += 1
        ujTest(fejX, fejY)
        kiir()
        gyumolcs_kirak()
    if abs(fej.xcor()) > width/2 or abs(fej.ycor()) > height/2:
        die()
    palya.update()
    for t in test:
        if(fej.distance(t.xcor(), t.ycor()) < 15):
            die()
    time.sleep(0.3)
