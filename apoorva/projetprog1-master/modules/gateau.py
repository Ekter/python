import time
from turtle import Turtle, update
from modules.drawing import WriteStep, bezier, bezier_2, draw_line


class Gateau:
    """ Class that stores information about a cake and draws and animates that cake"""
    def __init__(self, length, start_pos, scale=(1, 1), space_between=1, ):
        self.length = length
        self.start_pos = start_pos
        self.space_between = space_between
        self.scale = (scale[0] / self.length, scale[1])
        self.pos = -((100 * self.scale[0] * (self.length - 1) + self.space_between * (self.length - 1)) / 2) + \
                   start_pos[0], start_pos[1]
        self.old_list = ['|'] * self.length
        self.turtles_gateau = []

        # animations points
        self.end_point = -200, -200
        self.middle_pos = -200, 0

    def draw_init(self):
        # TODO check if we can merge those 2 loops together
        for _ in range(self.length):
            self.turtles_gateau.append(Turtle())
        for tu in self.turtles_gateau:
            tu.up()
            tu.ht()
        self.draw_ends(self.turtles_gateau[0], False)
        for middle_part_index in range(self.length - 2):
            self.pos = (self.pos[0] + 100 * self.scale[0] + self.space_between, self.pos[1])
            self.draw_middle(self.turtles_gateau[1 + middle_part_index])
        self.pos = (self.pos[0] + 100 * self.scale[0] + self.space_between, self.pos[1])
        self.draw_ends(self.turtles_gateau[self.length - 1], True)

    def apply_scale(self, x, y):
        return x * self.scale[0] + self.pos[0], y * self.scale[1] + self.pos[1]

    def apply_scale_line(self, x, y, x1, y1):
        x = x * self.scale[0] + self.pos[0]
        y = y * self.scale[1] + self.pos[1]
        x1 = x1 * self.scale[0] + self.pos[0]
        y1 = y1 * self.scale[1] + self.pos[1]
        return x, y, x1, y1

    def apply_scale_bezier_2(self, x1, y1, x2, y2, x3, y3, tu):
        x1 = x1 * self.scale[0] + self.pos[0]
        y1 = y1 * self.scale[1] + self.pos[1]
        x2 = x2 * self.scale[0] + self.pos[0]
        y2 = y2 * self.scale[1] + self.pos[1]
        x3 = x3 * self.scale[0] + self.pos[0]
        y3 = y3 * self.scale[1] + self.pos[1]
        return x1, y1, x2, y2, x3, y3, tu

    def draw_middle(self, tu):
        tu.color('#915817')
        tu.fillcolor('#d9a162')
        tu.pensize(5)
        tu.goto(self.apply_scale(-50, 100))
        tu.begin_fill()
        x, y, x1, x2 = self.apply_scale_line(-50, 100, 50, 100)
        draw_line(x, y, x1, x2, tu)
        x, y, x1, x2 = self.apply_scale_line(50, -100, -50, -100)
        draw_line(x, y, x1, x2, tu)
        tu.end_fill()
        tu.goto(self.pos)

    def draw_ends(self, tu, flip=False):
        tu.pensize(5)
        if flip:
            self.scale = (self.scale[0] * -1, self.scale[1])
        tu.goto(self.apply_scale(50, 100))
        tu.down()
        tu.color('#915817')
        tu.fillcolor('#d9a162')
        tu.begin_fill()
        x, y, x1, x2 = self.apply_scale_line(50, 100, -50, 100)
        draw_line(x, y, x1, x2, tu)
        x1, y1, tmp, tmp2, x3, y3, tu = self.apply_scale_bezier_2(-50, 100, -60, 0, -50, -100, tu)
        x2, y2 = -50 * self.scale[0] + x1, tmp2
        bezier_2(x1, y1, x2, y2, x3, y3, tu)
        x, y, x1, x2 = self.apply_scale_line(-50, -100, 50, -100)
        draw_line(x, y, x1, x2, tu)
        tu.end_fill()
        if flip:
            self.scale = (self.scale[0] * -1, self.scale[1])
        tu.goto(self.pos)

    def update(self, object_up_list):

        for i, _object in enumerate(object_up_list):
            if _object == '.' and self.old_list[i] != '.':
                self.animate(self.turtles_gateau[i], i)
                for loop in range(25):
                    self.turtles_gateau[i].undo()
                    update()
                self.turtles_gateau[i].clear()
        self.old_list = object_up_list

    def animate(self, turtle_object, pos_in_list):
        animation_step = 20
        current_pos = turtle_object.pos()
        self.pos = [current_pos[0], current_pos[1]]
        for loop in range(int(200 * self.scale[1] / animation_step)):
            self.pos[1] += animation_step
            turtle_object.clear()
            if pos_in_list == 0:
                self.draw_ends(turtle_object, False)
            elif pos_in_list == len(self.old_list) - 1:
                self.draw_ends(turtle_object, True)
            else:
                self.draw_middle(turtle_object)
            update()
            time.sleep(1 / 60)
        x1, y1 = self.pos
        x2, y2 = self.middle_pos
        x3, y3 = self.end_point

        for t in range(0, WriteStep + 1):
            x = bezier(bezier(x1, x2, t / WriteStep), bezier(x2, x3, t / WriteStep), t / WriteStep)
            y = bezier(bezier(y1, y2, t / WriteStep), bezier(y2, y3, t / WriteStep), t / WriteStep)
            turtle_object.clear()
            self.pos = [x, y]
            if pos_in_list == 0:
                self.draw_ends(turtle_object, False)
            elif pos_in_list == len(self.old_list) - 1:
                self.draw_ends(turtle_object, True)
            else:
                self.draw_middle(turtle_object)
            update()


if __name__ == '__main__':
    from turtle import mainloop, update, tracer

    tracer(0)
    gateau = Gateau(10, (0, 0), scale=(3, 0.6))
    update()

    gateau.update(list('||||..|..|'))
    gateau.update(list('|..|..|..|'))
    gateau.update(list('|..|..|...'))

    mainloop()
