from turtle import Turtle, fillcolor

import sys
sys.path.insert(1, '/home/mat/Documents/python/apoorva/projetprog1-master/modules')
from drawing import bezier_2, rgb2hex


class Tree:
    """ Class that stores the scale information of a Tree and then draws it when called"""
    def __init__(self, scale=(1, 1), start_pos=(0, 0)):
        self.scale = scale
        self.scale_mean = (scale[0] + scale[1]) / 2
        self.tu = Turtle(undobuffersize=0)
        self.tu.penup()
        self.pos = start_pos
        self.original_pos = start_pos
        self.original_scale = scale
        self.counter = 0  # used for gradient

    def apply_scale(self, x, y):
        return (x + self.pos[0]) * self.scale[0], (y + self.pos[1]) * self.scale[1]

    def apply_scale_bezier_2(self, x1, y1, x2, y2, x3, y3):
        x1 = (x1 + self.pos[0]) * self.scale[0]
        y1 = (y1 + self.pos[1]) * self.scale[1]
        x2 = (x2 + self.pos[0]) * self.scale[0]
        y2 = (y2 + self.pos[1]) * self.scale[1]
        x3 = (x3 + self.pos[0]) * self.scale[0]
        y3 = (y3 + self.pos[1]) * self.scale[1]
        return x1, y1, x2, y2, x3, y3,

    def draw(self, amount=10, tu=None):
        if not tu:
            tu = self.tu
        # trunk
        rect_tu = Turtle()
        rect_tu.up()
        rect_tu.ht()
        rect_tu.goto(self.apply_scale(0, 0))
        rect_tu.pensize(10 * self.scale_mean)
        rect_tu.fillcolor('#582900')
        rect_tu.goto(self.apply_scale(-25, 100))
        rect_tu.down()
        rect_tu.begin_fill()
        rect_tu.goto(self.apply_scale(-25, 100))
        rect_tu.goto(self.apply_scale(25, 100))
        rect_tu.goto(self.apply_scale(25, -25))
        rect_tu.goto(self.apply_scale(-25, -25))
        rect_tu.goto(self.apply_scale(-25, 100))
        rect_tu.end_fill()

        # tree
        tu.ht()
        tu.color('black')
        tu.fillcolor('green')
        # drawing leaves
        for scale_scale in range(1, amount + 1):
            self.counter += 1
            tu.fillcolor(rgb2hex((0, (int(100 + self.counter * 255 / (amount * 5))), 0)))
            tree_scale = (0.9 ** scale_scale, 0)
            self.pos = (self.pos[0] * 1.1111111111111111111, self.pos[1] + 500 / amount)
            tu.goto(self.tu.pos())
            tu.begin_fill()
            for loop in range(2):
                # tracing bezier2
                x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(0, 0, -49.0, -66.0, -94.0, -2.0)
                x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
                bezier_2(x1, y1, x2, y2, x3, y3, tu)

                # tracing bezier2
                x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(-94.0, -2.0, -155.0, -48.0, -216.0, -2.0)
                x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
                bezier_2(x1, y1, x2, y2, x3, y3, tu)
                # tracing bezier2
                x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(-216.0, -2.0, -108.0, 4.0, -80.0, 64.0)
                x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
                bezier_2(x1, y1, x2, y2, x3, y3, tu)
                # mirrored other half
                # tracing bezier2
                x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(80.0, 64.0, 108.0, 4.0, 216.0, -2.0)
                x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
                bezier_2(x1, y1, x2, y2, x3, y3, tu)
                # tracing bezier2
                x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(216.0, -2.0, 155.0, -48.0, 94.0, -2.0)
                x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
                bezier_2(x1, y1, x2, y2, x3, y3, tu)
                # tracing bezier2
                x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(94.0, -2.0, 49.0, -66.0, 0, 0)
                x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
                bezier_2(x1, y1, x2, y2, x3, y3, tu)

            tu.end_fill()

        # Drawing top
        tree_scale = (0.9 ** scale_scale, 0)
        fillcolor("green")
        print(fillcolor())
        tu.begin_fill()
        for loop in range(2):
            # tracing bezier2
            x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(0, 0, -49.0, -66.0, -94.0, -2.0)
            x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
            bezier_2(x1, y1, x2, y2, x3, y3, tu)
            # tracing bezier2

            x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(-94.0, -2.0, -155.0, -48.0, -216.0, -2.0)
            x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
            bezier_2(x1, y1, x2, y2, x3, y3, tu)
            # tracing bezier2

            x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(-216.0, -2.0, -108.0, 4.0, 0, 150)
            x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
            bezier_2(x1, y1, x2, y2, x3, y3, tu)

            # tracing bezier2
            x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(0, 0, 49.0, -66.0, 94.0, -2.0)
            x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
            bezier_2(x1, y1, x2, y2, x3, y3, tu)
            # tracing bezier2

            x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(94.0, -2.0, 155.0, -48.0, 216.0, -2.0)
            x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
            bezier_2(x1, y1, x2, y2, x3, y3, tu)
            # tracing bezier2

            x1, y1, x2, y2, x3, y3 = self.apply_scale_bezier_2(216.0, -2.0, 108.0, 4.0, 0, 150)
            x1, x2, x3 = x1 * tree_scale[0], x2 * tree_scale[0], x3 * tree_scale[0]
            bezier_2(x1, y1, x2, y2, x3, y3, tu)
        tu.end_fill()

        # star
        self.scale = self.original_scale
        star = Turtle()
        star.pensize(5 * self.scale_mean)
        star.ht()
        star.color('black')
        star.fillcolor('yellow')
        star.up()
        star.goto(tu.pos())
        star.down()
        star.begin_fill()
        star.backward(45 * self.scale_mean)
        for i in range(5):
            star.forward(90 * self.scale_mean)
            star.right(144)
        star.end_fill()
        self.pos = self.original_pos
        self.counter = 0


if __name__ == '__main__':
    from turtle import Screen, mainloop, update

    screen = Screen()
    screen.tracer(0)
    print('is main')
    _tu = Turtle()
    _tu.penup()
    tree = Tree(scale=(1.5 * screen.window_width() / 1366, 0.8 * screen.window_height() / 768), start_pos=(0, -100))
    tree.draw(10)
    tree.draw(20)
    update()

    mainloop()
