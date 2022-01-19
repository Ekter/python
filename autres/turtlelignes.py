
from time import sleep
from turtle import *
from random import randint


tu=Turtle()
tu.speed(0)
tu.pendown()
tu.getscreen().window_height()
while True:
    while randint(1,500000000)!=1:
        tu.goto(randint(-1000,1000),randint(-700,700))
    sleep(3)
    tu.clear()