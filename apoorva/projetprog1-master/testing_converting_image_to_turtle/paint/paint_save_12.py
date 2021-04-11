
WriteStep = 20
Height = 500
Width = 500
scale=[1,1]
def apply_scale(x, y):
    return x * scale[0], y * scale[1]
def apply_scale_bezier_2(x1, y1, x2, y2, x3, y3,tu):
    return x1*scale[0], y1*scale[1], x2*scale[0], y2*scale[1], x3*scale[0], y3*scale[1],tu
def apply_scale_bezier_3(x1, y1, x2, y2, x3, y3, x4, y4,tu):
    return x1*scale[0], y1*scale[1], x2*scale[0], y2*scale[1], x3*scale[0], y3*scale[1],x4*scale[0], y4*scale[1],tu
def Bezier(p1, p2, t):  
    return p1 * (1 - t) + p2 * t


def Bezier_2(x1, y1, x2, y2, x3, y3,tu):  
    tu.goto(x1, y1)
    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4,tu):  

    tu.goto(x1, y1)
    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()
# STARTOFDRAW
def draw(tu):


    tu.pensize(4)
    tu.goto(0,0)
    tu.color('black')
    tu.up()
    tu.goto(apply_scale(-264.0,44.0))
    tu.down()
    tu.goto(apply_scale(-295.0,-62.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-295.0,-62.0))
    tu.down()
    tu.goto(apply_scale(299.0,-62.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(299.0,-62.0))
    tu.down()
    tu.goto(apply_scale(268.0,43.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(268.0,43.0))
    tu.down()
    tu.goto(apply_scale(-263.0,43.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-267.0,-61.0))
    tu.down()
    tu.goto(apply_scale(-243.0,32.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-243.0,32.0))
    tu.down()
    tu.goto(apply_scale(245.0,32.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(245.0,32.0))
    tu.down()
    tu.goto(apply_scale(270.0,-59.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-253.0,-59.0))
    tu.down()
    tu.goto(apply_scale(-231.0,24.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(230.0,24.0))
    tu.down()
    tu.goto(apply_scale(-232.0,24.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(254.0,-59.0))
    tu.down()
    tu.goto(apply_scale(229.0,23.0))
    tu.up()
    tu.color('black')
    tu.up()
    tu.goto(apply_scale(-264.0,45.0))
    tu.down()
    tu.goto(apply_scale(-243.0,32.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(246.0,32.0))
    tu.down()
    tu.goto(apply_scale(267.0,43.0))
    tu.up()
