import random
from turtle import Turtle

from modules import star_tu


class Background:
    """ Class used to handle all background objects
    (background stars(small and big) and the perspective lines on the side and floor)"""
    def __init__(self, _screen, scale=(1, 1), start_pos=(0, 0), bg_star_count=20):
        self.bg_star_count = bg_star_count
        self.scale = scale
        self.screen = _screen
        self.pos = start_pos
        # init main turtles
        self.tu = Turtle()
        self.tu.ht()
        self.tu.penup()
        star_tu.get_star_turtle(self.screen, 1)
        self.star = Turtle(undobuffersize=0, shape='star_shape')
        self.star.shapesize(stretch_wid=self.scale[0], stretch_len=self.scale[1])
        self.star.goto(self.apply_scale(0, 100))
        self.star.color('white', 'black')
        self.star2 = Turtle(undobuffersize=0, shape='star_shape')
        self.star2.shapesize(stretch_wid=self.scale[0], stretch_len=self.scale[1])
        self.star2.color('yellow')
        self.star2.left(45)
        self.star2.goto(self.apply_scale(0, 100))

        # background stars list
        self.stars_bg = []

        # update screen
        self.screen.update()

        # start the loops of the functions to add and update the stars
        self.screen.ontimer(self.update_fractal, t=100)
        self.screen.ontimer(self.add_stars_bg, t=10)

    """ apply_scale functions apply a defined scale to a specific input type"""

    def apply_scale(self, x, y):
        return (x + self.pos[0]) * self.scale[0], (y + self.pos[1]) * self.scale[1]

    def apply_scale_line(self, x, y, x1, y1):
        x = (x + self.pos[0]) * self.scale[0]
        y = (y + self.pos[1]) * self.scale[1]
        x1 = (x1 + self.pos[0]) * self.scale[0]
        y1 = (y1 + self.pos[1]) * self.scale[1]
        return x, y, x1, y1
    """ apply_scale functions apply a defined scale to a specific input type"""

    def add_stars_bg(self):
        """ add more of the background stars"""
        star_temp = Turtle(undobuffersize=0, shape='star_shape')
        star_temp.shapesize(stretch_wid=0.1 * self.scale[0], stretch_len=0.1 * self.scale[1])
        star_temp.up()
        star_temp.color('white')
        _range = (-32, 252)
        _range = (int(_range[0]), int(_range[1]))
        star_temp.goto(self.apply_scale(-427.0, random.randint(_range[0], _range[1])))
        self.stars_bg.append(star_temp)
        self.screen.update()
        if len(self.stars_bg) > self.bg_star_count:
            pass
        else:
            self.screen.ontimer(self.add_stars_bg, t=50)

    def update_fractal(self):
        """ Update the stars on the screen"""
        # update bg_stars
        left, top, right, bottom = self.apply_scale_line(-427, 252, 427, -32)
        for star_object in self.stars_bg:
            # check for out of bounds
            if star_object.pos()[0] > right or star_object.pos()[0] < left or star_object.pos()[1] < bottom or \
                    star_object.pos()[1] > top:
                # reset
                _range = (-32, 252)
                _range = (int(_range[0]), int(_range[1]))
                star_object.goto(self.apply_scale(-427.0, random.randint(_range[0], _range[1])))
                star_object.setheading(random.randint(-10, 10))

            else:
                # update position
                star_object.left(random.randint(-2, 2))
                star_object.forward(5)
        # jiggle to main star
        # point = random.uniform(-1, 1), random.uniform(99, 101)
        # self.star.goto(self.apply_scale(point[0], point[1]))
        # self.star2.goto(self.apply_scale(point[0], point[1]))
        # update main star
        self.star.left(2)
        self.star2.left(4)
        self.screen.update()
        self.screen.ontimer(self.update_fractal, t=1)

    def draw(self):
        """ draw background without stars"""
        tu = self.tu
        tu.goto(0, 0)
        tu.pensize(5)
        tu.color('white', 'black', )
        # middle
        tu.up()
        tu.goto(self.apply_scale(-427.0, -32.0))
        tu.begin_fill()
        tu.down()
        tu.goto(self.apply_scale(-447.0, 252.0))
        tu.goto(self.apply_scale(447.0, 252.0))
        tu.goto(self.apply_scale(427.0, -32.0))
        tu.end_fill()

        # floor
        tu.up()
        tu.goto(self.apply_scale(-427.0, -32.0))
        tu.down()
        tu.begin_fill()
        tu.goto(self.apply_scale(427.0, -32.0))
        tu.goto(self.apply_scale(449.0, -46.0))
        tu.goto(self.apply_scale(600.0, -600.0))
        tu.goto(self.apply_scale(-600.0, -600.0))
        tu.goto(self.apply_scale(-449.0, -46.0))
        tu.goto(self.apply_scale(-427.0, -32.0))
        tu.end_fill()

        # draw sides
        self.draw_sides()

    def draw_sides(self):
        """ draw sides of the background"""
        tu = self.tu
        # left side
        tu.up()
        tu.goto(self.apply_scale(-447.0, 252.0))
        tu.begin_fill()
        tu.goto(self.apply_scale(-427.0, -32.0))
        tu.down()
        tu.goto(self.apply_scale(-449.0, -46.0))
        tu.goto(self.apply_scale(-500.0, 252.0))
        tu.end_fill()

        # right side
        tu.goto(self.apply_scale(447.0, 252.0))
        tu.begin_fill()
        tu.goto(self.apply_scale(427.0, -32.0))
        tu.down()
        tu.goto(self.apply_scale(449.0, -46.0))
        tu.goto(self.apply_scale(500.0, 252.0))
        tu.end_fill()


if __name__ == '__main__':
    from turtle import Screen, mainloop
    print('is main')
    _tu = Turtle()
    screen = Screen()
    screen.setup(width=0.5, height=1.0, startx=0, starty=0)
    table = Background(screen, scale=(1.52 * screen.window_width() / 1366, 1.52 * screen.window_height() / 768),
                       start_pos=(0, 0))

    _tu.penup()
    table.draw()
    mainloop()
