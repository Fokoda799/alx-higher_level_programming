#!/usr/bin/python3
from turtle import *
from math import *

setup(800, 500)
bgcolor("#01411C")
speed(0)
penup()
goto(-400, 250)
pendown()
color("white")
begin_fill()
for i in range(2):
    fd(200)
    rt(90)
    fd(500)
    rt(90)
end_fill()

done()
