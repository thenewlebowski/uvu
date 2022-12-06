import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("black")
color = ['red','yellow','green','blue']

pen = turtle.Turtle()
pen.hideturtle()

pen.color("#AA00AA")
pen.pensize(1)
pen.speed(0)


pen.penup()

A = 400
B = 400

k = int(input("please provide how many pedals you would like?\n"))
t=0

for i in range(0,1000):
    t+=0.01
    pen.color(color[i%4])
    x = A * cos(k*t) * cos(t)
    y = A * cos(k*t) * sin(t)

    pen.goto(x,y)
    pen.pendown()
    pen.getscreen().update() 

sleep(100)
