import ctypes
import turtle

from PIL import Image


class RenderingEngine:
    def __init___(self, _object_num):
        self.screen = turtle.Screen()
        self.screen.tracer(0)
        print(self.screen.screensize())
        user32 = ctypes.windll.user32
        # Getting screensize
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        # Setting up screen
        self.screen.setup(screensize[0], screensize[1])
        print(screensize)
        self._object_num = _object_num
        self.turtles = []

    def initialise_turtles(self):
        for _ in range(self._object_num):
            self.turtles.append(turtle.Turtle())
        self.screen.addshape("quille_update.gif")
        for i, tu in enumerate(turtles):
            tu.up()
            tu.goto(i * (screensize[0] / (_object_num * 2)) - screensize[0] / 4, 0)
            tu.shape("quille_update.gif")
        self.screen.update()

    def update(self, _render_list):
        for i, _object in enumerate(_render_list):
            if _object == '.':
                self.turtles[i].ht()
            else:
                self.turtles[i].st()
        self.screen.update()


screen = turtle.Screen()
screen.tracer(0)
print(screen.screensize())
user32 = ctypes.windll.user32
# Getting screensize
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# Setting up screen
screen.setup(screensize[0], screensize[1])
print(screensize)


def resize_image(x, y, _screensize, _input, _output):
    # Opens a image in RGB mode  
    im = Image.open(_input)
    im = im.resize((int(x * screensize[0]), int(y * screensize[1])))
    im.save(_output)
    im.close()


resize_image(1 / 6, 1 / 4, screensize, "quille.gif", "quille_update.gif")

_object_num = 10
turtles = []


def initialise_turtles():
    for _ in range(_object_num):
        turtles.append(turtle.Turtle())
    screen.addshape("quille_update.gif")
    for i, tu in enumerate(turtles):
        tu.up()
        tu.goto(i * (screensize[0] / (_object_num * 2)) - screensize[0] / 4, 0)
        tu.shape("quille_update.gif")
    screen.update()


def update(_render_list):
    for i, _object in enumerate(_render_list):
        if _object == '.':
            turtles[i].ht()
        else:
            turtles[i].st()
    screen.update()


initialise_turtles()

# shape = screen.addshape("source.gif")
# turtle.shape("source.gif")
# for loop in range(10):
#    turtle.forward(100)
#    screen.update()
screen.listen()
screen.mainloop()
