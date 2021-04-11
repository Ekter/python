from turtle import Turtle
from modules.drawing import bezier_2

scale = [1, 1]
pos = (0, 0)
WriteStep = 60
angle = 0


def apply_scale_bezier_2(x1, y1, x2, y2, x3, y3, tu):
    """applies scale to bezier 2 coordinates"""
    x1 = (x1 + pos[0]) * scale[0]
    y1 = (y1 + pos[1]) * scale[1]
    x2 = (x2 + pos[0]) * scale[0]
    y2 = (y2 + pos[1]) * scale[1]
    x3 = (x3 + pos[0]) * scale[0]
    y3 = (y3 + pos[1]) * scale[1]
    return x1, y1, x2, y2, x3, y3, tu


def get_star_turtle(screen, size):
    global scale
    tu = Turtle(undobuffersize=0)
    tu.ht()
    a, b, c = (0, 100), (-100, 0), (0, 100)
    distance = 100, 0
    tu.up()
    scale = [0 + size, 0 + size]
    scale_dict = {
        0: [1 * scale[0], 1 * scale[1]],
        1: [-1 * scale[0], 1 * scale[1]],
        2: [-1 * scale[0], -1 * scale[1]],
        3: [1 * scale[0], -1 * scale[1]]
    }
    tu.begin_poly()
    for loop in range(4):
        tu.up()
        tu.goto(0, 0)
        scale = scale_dict[loop]
        x1, y1, x2, y2, x3, y3, tu = apply_scale_bezier_2(b[0], b[1], b[0] + distance[0], b[1] + distance[1],
                                                          c[0],
                                                          c[1], tu)
        bezier_2(x1, y1, x2, y2, x3, y3, tu)
        tu.up()
    tu.end_poly()
    star_shape = tu.get_poly()
    screen.addshape('star_shape', shape=star_shape)
