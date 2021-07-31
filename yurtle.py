# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 21:20:33 2021

@author: Gobinda
"""

import turtle

# turtle.setup(100,100)

u = turtle.Screen()
u = turtle.getscreen()
# t = turtle.speed(-4000)
t = turtle.Turtle()
s = turtle.Turtle()
# s.title('Canvas')

s.speed(1)


x = [27,63,22]

y = [26,17,98]

for i in range(len(x)):
    s.penup()
    s.goto(x[i], y[i])
    s.dot(20, "blue")

t.speed(1)

x = [0,27,29,27,13,27,32,27,56,63,76,63,73,63,99,63,15,22,38,22,0]

y = [0,26,12,26,14,26,45,26,2,17,24,17,4,17,46,17,63,98,85,98,0]

for i in range(len(x)):
    
    t.goto(x[i], y[i])
    t.dot(10, "red")
u.getcanvas().postscript(file="test.gif")
turtle.done()
turtle.bye()