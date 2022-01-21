from turtle import Turtle
from random import normalvariate
from pynput import mouse


tu = Turtle()
lis=[]

def click(*args, **kwargs):
    "NIK"
    print("pas encore ok")
    lis.append((*args,{**kwargs}))
    print("ok")

tu.speed(0)
tu.pendown()
tu.getscreen().window_height()
listener = mouse.Listener(on_click=click)
listener.start()
while True:
    tu.goto(normalvariate(0, 500), normalvariate(0, 500))
    if len(lis)>0:
        tu.clear()
        print(lis.pop(0))

