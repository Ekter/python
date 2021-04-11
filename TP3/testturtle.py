from turtle import *

l=int(input("Longeur des côtés:"))
n=int(input("nombre de côtés:"))
down()
for k in range(n):
    forward(100)
    left(360/n)