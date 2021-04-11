
from turtle import Turtle
import sys
sys.path.insert(1, '/home/mat/Documents/python/apoorva/projetprog1-master/modules')
from drawing import ellipse

class Plate:
    """ Plate stores the information about the scale of the Plate and draws it with draw"""

    def __init__(self, scale=(1, 1), start_pos=(0, 0), tilt=0):
        self.scale = scale
        self.global_pos = None  # pos in absolute coordinates used for animations in gateau.py
        # init tu
        self.tu = Turtle()
        self.tu.ht()
        self.tu.penup()
        self.tilt = tilt
        self.pos = start_pos
        self.center_pos = self.apply_scale(0, 0)

    def apply_scale(self, x, y):
        """ apply scale to a point"""
        return (x + self.pos[0]) * self.scale[0], (y + self.pos[1]) * self.scale[1]

    def draw(self, tu=None):
        """draws 2 ellipses for the plate"""
        if not tu:
            tu = self.tu
        tu.color('black', 'white', )
        x, y = self.center_pos
        self.global_pos = tu.pos()
        tu.begin_fill()
        ellipse(x, y, 80 * self.scale[0], 70 * self.scale[1], self.tilt, tu)
        tu.end_fill()
        tu.begin_fill()
        ellipse(x, y, 60 * self.scale[0], 50 * self.scale[1], self.tilt, tu)
        tu.end_fill()


if __name__ == '__main__':
    from turtle import Turtle, Screen, mainloop

    print('is main')
    _tu = Turtle()
    screen = Screen()
    screen.setup(1000, 700)
    # screen.bgpic('background.png')
    table = Plate(scale=(1 * screen.window_width() / 1366, 1 * screen.window_height() / 768), start_pos=(0, -200))
    _tu.penup()
    table.draw(_tu)
    mainloop()
