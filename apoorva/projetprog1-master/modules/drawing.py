import math

# resolution of the lines
WriteStep = 20


def rgb2hex(color):
    """converts rgb to hex source: stackoverflow"""
    return f"#{''.join(f'{hex(c)[2:].upper():0>2}' for c in color)}"


def bezier(p1, p2, t):
    """ equation used to draw beziers source: stackoverflow"""
    return p1 * (1 - t) + p2 * t


def bezier_2(x1, y1, x2, y2, x3, y3, tu):
    """ takes 3 points and a turtle and draws a bezier 2    source: stackoverflow"""
    tu.goto(x1, y1)
    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = bezier(bezier(x1, x2, t / WriteStep),
                   bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = bezier(bezier(y1, y2, t / WriteStep),
                   bezier(y2, y3, t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()


def bezier_3(x1, y1, x2, y2, x3, y3, x4, y4, tu):
    """ takes 4 points and a turtle and draws a bezier 3    source: stackoverflow"""
    tu.goto(x1, y1)
    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = bezier(bezier(bezier(x1, x2, t / WriteStep), bezier(x2, x3, t / WriteStep), t / WriteStep),
                   bezier(bezier(x2, x3, t / WriteStep), bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = bezier(bezier(bezier(y1, y2, t / WriteStep), bezier(y2, y3, t / WriteStep), t / WriteStep),
                   bezier(bezier(y2, y3, t / WriteStep), bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()


def draw_line(x, y, x1, y1, tu):
    """takes in 2 points and a turtle and draws line """
    tu.up()
    tu.goto(x, y)
    tu.down()
    tu.goto(x1, y1)
    tu.up()


write_step_ellipse = 20


# (cx,cy): center of ellipse, a: width, b:height, angle: tilt
def ellipse(cx, cy, a, b, angle, tu):
    """code from https://pythonturtle.academy/drawing-general-ellipse-with-python-turtle/"""
    # draw the first point with pen up
    t = 0
    x = cx + a * math.cos(t) * math.cos(math.radians(angle)) - b * math.sin(t) * math.sin(math.radians(angle))
    y = cy + a * math.cos(t) * math.sin(math.radians(angle)) + b * math.sin(t) * math.cos(math.radians(angle))
    tu.up()
    tu.goto(x, y)
    tu.down()
    # draw the rest with pen down
    for i in range(write_step_ellipse + 1):
        x = cx + a * math.cos(t) * math.cos(math.radians(angle)) - b * math.sin(t) * math.sin(math.radians(angle))
        y = cy + a * math.cos(t) * math.sin(math.radians(angle)) + b * math.sin(t) * math.cos(math.radians(angle))
        tu.goto(x, y)
        t += 2 * math.pi / write_step_ellipse
