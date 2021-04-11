from turtle import Turtle

import sys
sys.path.insert(1, '/home/mat/Documents/python/apoorva/projetprog1-master/modules')
import plate_circular
from drawing import bezier_2


class Table:
    """ Table stores information about the scale and handles every static object on the table( 2 plates)"""
    def __init__(self, _screen, scale=(1, 1), start_pos=(0, -200)):
        self.screen = _screen
        self.scale = scale
        self.tu = Turtle()
        self.tu.penup()
        self.pos = start_pos
        # init plates
        self.plate = plate_circular.Plate(
            scale=(1 * self.screen.window_width() / 1366, 1 * self.screen.window_height() / 768),
            start_pos=(-400, -300))
        self.plate2 = plate_circular.Plate(
            scale=(1 * self.screen.window_width() / 1366, 1 * self.screen.window_height() / 768),
            start_pos=(400, -300))

    """ apply_scale functions apply a defined scale to a specific input type"""
    def apply_scale(self, x, y):
        return (x + self.pos[0]) * self.scale[0], (y + self.pos[1]) * self.scale[1]

    def apply_scale_custom(self, x, y, scale_custom):
        return x * self.scale[0] * scale_custom[0] + self.pos[0], y * self.scale[1] * scale_custom[1] + self.pos[1]

    def apply_scale_line(self, x, y, x1, y1):
        x = (x + self.pos[0]) * self.scale[0]
        y = (y + self.pos[1]) * self.scale[1]
        x1 = (x1 + self.pos[0]) * self.scale[0]
        y1 = (y1 + self.pos[1]) * self.scale[1]
        return x, y, x1, y1

    def apply_scale_bezier_2(self, x1, y1, x2, y2, x3, y3, tu):
        x1 = (x1 + self.pos[0]) * self.scale[0]
        y1 = (y1 + self.pos[1]) * self.scale[1]
        x2 = (x2 + self.pos[0]) * self.scale[0]
        y2 = (y2 + self.pos[1]) * self.scale[1]
        x3 = (x3 + self.pos[0]) * self.scale[0]
        y3 = (y3 + self.pos[1]) * self.scale[1]
        return x1, y1, x2, y2, x3, y3, tu
    """ apply_scale functions apply a defined scale to a specific input type"""

    def draw(self, tu=None):
        """ draws table takes in tu if a specific tu is chosen to draw the table"""
        if not tu:
            tu = self.tu
        # draw table
        x1, x2 = -557, -433
        a, b = (x1, (175 / 124) * x1 + 79123 / 124), (x2, (175 / 124) * x2 + 79123 / 124)
        c = (b[0] + 120 * self.scale[0], b[1] + 20 * self.scale[1])
        tu.goto(0, 0)
        tu.color('black')
        tu.fillcolor('#D19755')
        tu.up()
        tu.goto(self.apply_scale(a[0], a[1]))
        tu.begin_fill()
        tu.down()
        tu.goto(self.apply_scale(b[0], b[1]))
        tu.up()

        # tracing bezier2
        x1, y1, x2, y2, x3, y3, tu = self.apply_scale_bezier_2(b[0], b[1], b[0] + 20 * self.scale[0],
                                                               b[1] + 20 * self.scale[1], c[0], c[1], tu)
        bezier_2(x1, y1, x2, y2, x3, y3, tu)
        tu.down()
        tu.goto(self.apply_scale(c[0], c[1]))
        x1, y1, x2, y2, x3, y3, tu = self.apply_scale_bezier_2(-c[0], c[1], -b[0] - 10 * self.scale[0],
                                                               b[1] + 20 * self.scale[1], -b[0], b[1], tu)
        bezier_2(x1, y1, x2, y2, x3, y3, tu)
        tu.down()
        tu.goto(self.apply_scale(-a[0], a[1]))
        tu.end_fill()

        # draw plates
        self.plate.draw()
        self.plate2.draw()


if __name__ == '__main__':
    from turtle import Screen, mainloop, update, tracer
    print('is main')
    _tu = Turtle()
    screen = Screen()
    screen.setup(width=1.0, height=1.0, startx=0, starty=0)
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()

    root.attributes('-fullscreen', True)
    # screen.bgpic('background.png')
    tracer(0)
    table = Table(screen, scale=(1 * screen.window_width() / 1366, 1.2 * screen.window_height() / 768))
    _tu.penup()
    table.draw(_tu)
    update()
    mainloop()
