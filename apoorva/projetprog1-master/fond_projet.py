import turtle
scale=[2,2]
def apply_scale_line(x,y,x1,y1):
    return x * scale[0], y * scale[1],x1*scale[0],y1*scale[1]
def apply_scale(x,y):
    return x * scale[0], y * scale[1]

def draw_line(x,y,x1,y1):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.goto(x1,y1)


def draw(rad):
    # rad --> radius of arc
    for i in range(2):
        # two arcs
        turtle.circle(rad, 90)
        turtle.circle(rad // 2, 90)

    # Main section



def Sapin():
    #tronc du sapin
    a,b,c,d=apply_scale_line(150,20,170,-40)
    turtle.up()
    turtle.goto(a,b)
    turtle.fillcolor("#D19755")
    turtle.begin_fill()
    draw_line(a,b,a,d)
    draw_line(c,d,c,b)
    turtle.end_fill()
    #feuillage du sapin
    i=0
    while i<3:
        x,y,x1,y1=apply_scale_line(120,20+20*i,160,90+20*i)
        turtle.up()
        turtle.goto(x,y)
        turtle.fillcolor("#108108")
        turtle.begin_fill()
        draw_line(x,y,x1,y1)
        draw_line(x1,y1,x+((x1-x)*2),y)
        turtle.end_fill()
        i=i+1
def Table():
    #table
    x,y,x1,y1=apply_scale_line(-300,-178,-200,-50)
    turtle.up()
    turtle.goto(x,y)
    turtle.fillcolor("#D19755")
    turtle.begin_fill()
    draw_line(x,y,x1,y1)
    draw_line(-x1,y1,-x,y)
    turtle.end_fill()
    #assiettes
    p,c=apply_scale(125,25)
    turtle.fillcolor("white")
    turtle.up()
    turtle.goto(1.2*p,-p)
    turtle.begin_fill()
    turtle.down()
    turtle.circle(c)
    turtle.end_fill()
    turtle.up()
    turtle.goto(1.2*p,-p+c/2)
    turtle.down()
    turtle.circle(c/2)
    turtle.up()
    turtle.goto(-1.2*p,-p)
    turtle.begin_fill()
    turtle.down()
    turtle.circle(c)
    turtle.end_fill()
    turtle.up()
    turtle.goto(-1.2*p,-p+c/2)
    turtle.down()
    turtle.circle(c/2)
    #plateau
    xp,yp,xp1,yp1=apply_scale_line(-85,-115,-77,-90)
    turtle.up()
    turtle.goto(xp,yp)
    turtle.fillcolor("white")
    turtle.begin_fill()
    draw_line(xp,yp,xp1,yp1)
    draw_line(-xp1,yp1,-xp,yp)
    turtle.end_fill()
if __name__ == '__main__':
    print(turtle.window_height(),turtle.window_width())

    Sapin()
    Table()
    turtle.mainloop()