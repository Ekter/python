from turtle import *
up()
goto(-350,-300)
down()
l=int(input("Longueur:"))
n=int(input("nombre de carrés:"))
for i in range(n):
    left(90)
    forward(l)
    right(90)
    forward(l)
right(90)
for i in range(n):
    forward(l)
    right(90)
    forward(l)
    left(90)


input("")
