from turtle import *
up()
h=window_height()
w=window_width()
up()
goto(-w/2+5,h/2+5)
down()
write("départ")
l=int(input("longueur des marches:"))
h=int(input("hauteur des marches:"))
n=int(input("nombre de marches:"))
x=-w/2
y=h/2
for i in range(n):
    if x+l>w/2 or y-h<-h/2:
        write("Tronqué")
        break
    forward(l)
    right(90)
    forward(h)
    left(90)
input("")