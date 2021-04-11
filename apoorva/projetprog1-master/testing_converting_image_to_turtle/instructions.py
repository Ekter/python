import math
import random
import turtle

scale = [1, 1]
pos=(0,100)
WriteStep = 60
angle = 0


def rgb2hex(color):
    return f"#{''.join(f'{hex(c)[2:].upper():0>2}' for c in color)}"


def apply_scale_bezier_2( x1, y1, x2, y2, x3, y3, tu):
    x1 = (x1 +pos[0]) * scale[0]
    y1 = (y1 + pos[1]) *scale[1]
    x2 = (x2 + pos[0]) * scale[0]
    y2 = (y2 + pos[1]) * scale[1]
    x3 = (x3 + pos[0]) * scale[0]
    y3 = (y3 + pos[1]) * scale[1]
    return x1, y1, x2, y2, x3, y3, tu


def apply_scale_bezier_3(x1, y1, x2, y2, x3, y3, x4, y4, tu):
    return x1 * scale[0], y1 * scale[1], x2 * scale[0], y2 * scale[1], x3 * scale[0], y3 * scale[1], x4 * scale[0], y4 * \
           scale[1], tu


def bezier(p1, p2, t):
    return p1 * (1 - t) + p2 * t


def bezier_2(x1, y1, x2, y2, x3, y3, tu):
    tu.goto(x1, y1)

    for t in range(0, WriteStep + 1):
        x = bezier(bezier(x1, x2, t / WriteStep),
                   bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = bezier(bezier(y1, y2, t / WriteStep),
                   bezier(y2, y3, t / WriteStep), t / WriteStep)
        x, y = rotate((0, 0), (x, y), angle)

        tu.goto(x, y)
        tu.pendown()
    tu.penup()


def draw_line(x, y, x1, y1, tu):
    """draws line """
    tu.up()
    tu.goto(x, y)
    tu.down()
    tu.goto(x1, y1)
    tu.up()


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def draw(tu,size):
    global scale
    global angle
    a, b, c = (0, 100), (-100, 0), (0, 100)
    distance = 100, 0
    tu.up()
    turtle.tracer(0)
    tu.speed(0)
    # for size in range(0,10):
    scale = [0 + size, 0 + size]
    scale_dict = {
        0: [1 * scale[0], 1 * scale[1]],
        1: [-1 * scale[0], 1 * scale[1]],
        2: [-1 * scale[0], -1 * scale[1]],
        3: [1 * scale[0], -1 * scale[1]]
    }
    angle += 0.01
    for loop1 in range(1):
        distance = loop1 + 90, 0
        tu.color(rgb2hex((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
        for loop in range(4):
            # tu.begin_fill()
            tu.up()

            scale = scale_dict[loop]
            x1, y1, x2, y2, x3, y3, tu = apply_scale_bezier_2(b[0], b[1], b[0] + distance[0], b[1] + distance[1],
                                                              c[0],
                                                              c[1], tu)
            bezier_2(x1, y1, x2, y2, x3, y3, tu)
            tu.up()
            #turtle.update()

            # tu.end_fill()


    print('finished')
    #ts = turtle.getscreen()
    #ts.getcanvas().postscript(file="ochinchin.eps")


if __name__ == '__main__':
    screen = turtle.Screen()
    _tu = turtle.Turtle(undobuffersize=0)
    x=0
    while True:
        x+=1
        draw(_tu,x/100)
        screen.update()
    turtle.mainloop()
