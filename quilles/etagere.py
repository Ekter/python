from turtle import *
from random import *
def etagere(taille,x,y,longueur=1,hauteurdesfondation=1,hauteurdunetage=1,nombrederayon=6,nombredelivre=15,proportion=1):

    up()
    goto(x,y)
    down()

    t=taille
    l=longueur
    hdf=hauteurdesfondation
    hde=hauteurdunetage
    nbr=nombrederayon
    nbl=nombredelivre
    pro=proportion

    tracer(0)

    up()
    backward(t*137*l)
    
    right(90)
    forward(t*180*hde+hdf*20)
    left(90)
    down()

    width(1*t)
    pencolor('#6e8895')

    
    #Base de l'étagère
    fillcolor('#809caa')
    begin_fill()
    for k in range (4):
        r,x=pos()
        for j in range(5):
            u,n=pos()
            for i in range(2):
                forward(t*67.5*l)
                left(90)
                up()
                forward(t*3*hdf)
                down()
                dot(3*hdf)
                up()
                forward(t*3*hdf)
                down()
                left(90)
            up()
            goto(u,n)
            left(90)
            forward(t*6*hdf)
            down()
            right(90)
        up()
        goto(r,x)
        down()
        forward(t*67.5*l)
    
    end_fill()

    up()
    left(90)
    forward(t*6*hdf*5)
    down()
    begin_fill()
    for i in range(5):
        right(60)
        forward(20*t)
        right(30)
        right(90)
        forward(t*6*hdf)
        right(60)
        forward(20*t)
        right(120)
    forward(t*6*hdf*5)
    backward(t*6*hdf*5)
    right(90)
    end_fill()
        
    
    

    pencolor('#8f8c84')
    left(90)
    up()
    forward(t*30*hdf)
    left(90)
    forward(t*-5*l)
    down()

    for z in range(nbr):
        a,z=pos()
        for m in range(2):
            
            up()
            forward(t*280*l)
            right(90)
            forward(t*10*hde)
            right(90)
            down()
            
        up()
        right(90)
        forward(t*10*hde)
        left(90)
        forward(t*5*l)
        down()
        fillcolor('#dddcc9')
        begin_fill()
        for m in range(2):
            forward(t*270*l)
            right(90)
            forward(t*50*hde)
            right(90)
        end_fill()
        up()
        right(90)
        forward(20*t*hde)
        left(90)
        down()
        forward(254*pro*l*t)
        left(50)
        forward(25*t*hde)
        backward(25*t*hde)
        right(50)
        right(90)
        forward(30*t*hde)
        left(90)
        
        
        up()
        goto(a,z)
        right(90)
        forward(t*60*hde)
        left(90)
        down()

    fillcolor('#cacba0')
    begin_fill()
    up()
    forward(275*l*t)
    left(210)
    down()
    forward(t*24)
    right(30)
    forward(270*l*t)
    left(210)
    forward(t*24)
    backward(t*24)
    left(60)
    forward(t*nbr*hde*60)
    right(60)
    forward(24*t)
    right(30)
    right(90)
    forward(t*nbr*hde*60)
    end_fill()
    up()
    backward(t*nbr*hde*60)
    left(90)
    backward(5*l*t)
    down()

    to,ny=pos()

    up()
    forward(5*t*l)
    down()

    fillcolor('#cacba0')
    begin_fill()
    right(90)
    forward(t*nbr*hde*60)
    left(90)
    forward(270*t*l)
    left(90)
    forward(t*nbr*hde*60)
    left(90)
    forward(7*t)
    left(90)
    forward(t*nbr*hde*60-7*t)
    right(90)
    forward(270*t*l-14*t)
    right(90)
    forward(t*nbr*hde*60-7*t)
    left(90)
    forward(7*t)
    end_fill()
    left(180)
    

    up()
    goto(to,ny)
    
    p,s=pos()
    up()
    forward(265*t*l)
    right(90)
    forward(10*hde*t)
    down()
    for g in range(2):
        a,y=pos()
        maxx=0
        
        while maxx<(240*l*t):
            pencolor('black')
            
            e,r=pos()
            fillcolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
            ep=randint(6,15)
            hdl=randint(30,45)
            saut=[1,1,2,2,1,3,4,3]
            st=choice(saut)
            
            begin_fill()
            for j in range(2):
                forward(hdl*hde*t)
                right(90)
                forward(ep*t)
                right(90)
            end_fill()
            begin_fill()
            right(90)
            forward(ep*t)
            left(30)
            forward(20*t)
            left(60)
            forward(hdl*hde*t)
            left(120)
            forward(20*t)
            left(60)
            forward(t*hde*hdl)
            backward(t*hde*hdl)
            right(60)
            end_fill()
            pencolor('#6e8895')
            fillcolor('white')
            begin_fill()
            for i in range(3):
                right(30)
                forward((ep/3)*t)
                d,f=pos()
                right(150)
                forward(20*t)
                right(30)
                forward((ep/3)*t)
                left(210)
                forward(20*t)

                up()
                goto(d,f)
                down()
            end_fill()
            up()
            goto(e,r)
            right(210)
            forward(st*ep*t)
            down()
            left(90)
            maxx+=ep*t*st
                
        
        up()
        goto(a,y)
        forward(60*t*hde)
        down()

    left(90)
    up()
    goto(p,s)
    down()
    
    for z in range(nbr):
        a,z=pos()
        up()
        forward(3*t*l)
        down()
        fillcolor('#ebece6')
        begin_fill()
        for m in range(2):

            forward(t*270*l+5*t)
            right(90)
            forward(t*10*hde)
            right(90)
            
        end_fill()
        up()
        right(90)
        forward(t*10*hde)
        left(90)
        forward(t*5*l)
        
        
        for m in range(2):
            forward(t*270*l)
            right(90)
            forward(t*50*hde)
            right(90)

        
        goto(a,z)
        right(90)
        forward(t*60*hde)
        left(90)
    
        down()
    
    update()

