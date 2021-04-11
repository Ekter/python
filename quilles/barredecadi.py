from turtle import *
from trait import *
def barre(poly,tortue,vrtc,hrzt,angle,taille,miroir=1,chuia=0):

    tracer(0)
    t=taille
    m=miroir
    
    tortue.up()
    j,k=tortue.pos()
    tortue.setheading(90+90*-m)
    tortue.right(90+90*-m)
    tortue.forward(t*vrtc*m)
    tortue.right(m*90)
    tortue.forward(t*hrzt*-m)
    tortue.down()
    tortue.begin_poly()
    tortue.right(180-angle*m)
    tortue.forward(t*120*m+t*(9+9*m))
    tortue.forward(chuia*m)
    tortue.right((90+20*m)*m)
    tortue.up()
    tortue.forward(t*15)
    tortue.right((90-20*m)*m+90+90*-m)
    tortue.forward(t*-(5-5*m))
    tortue.down()
    trait(tortue,m,5,t,180,0,1)
    tortue.forward(t*65-(5-5*m))
    tortue.up()
    tortue.forward(t*20)
    tortue.down()
    trait(tortue,m,5,t,180,0,1)
    tortue.forward(t*55)#*-m
    tortue.forward(chuia)

    tortue.end_poly()
    poly.addcomponent(tortue.get_poly(),'#E9DCA8', "black")


    tortue.setheading(0)
    tortue.up()
    tortue.goto(j,k)
    tortue.down()

    update()
