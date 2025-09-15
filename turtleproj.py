import turtle
import random

t = turtle.Turtle()
t.speed(40)
t2 = turtle.Turtle()
t2.speed(20)
t3 = turtle.Turtle()
t3.speed(20)
t4 = turtle.Turtle()
t4.speed(20)
t.circle(50,180)
t2.circle(50,-180)
turtle.setworldcoordinates(500,500,-500,-500)
while True:
 degree = random.randint(0,360)
 x = random.randint(-500,500)
 y = random.randint(-500,500)
 t.goto(x,y)
 t2.goto(-x,y)
 t3.goto(-x,-y)
 t4.goto(x,-y)


