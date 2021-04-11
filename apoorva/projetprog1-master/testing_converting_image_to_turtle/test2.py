import random
import turtle

te = turtle.Turtle()
WriteStep = 50
screen = turtle.Screen()
te.speed(0)
screen.tracer(0)


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def bezier(p1, p2, t):
    return p1 * (1 - t) + p2 * t


def bezier_2(x1, y1, x2, y2, x3, y3):
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = bezier(bezier(x1, x2, t / WriteStep),
                   bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = bezier(bezier(y1, y2, t / WriteStep),
                   bezier(y2, y3, t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


te.begin_poly()
te.goto(100, 0)
te.goto(100, 100)

for loop in range(400000):
    screen.update()
    te.goto(random.randint(-5000, 5000), random.randint(-5000, 5000))
    bezier_2(random.randint(-5000, 5000), random.randint(-5000, 5000), random.randint(-5000, 5000), random.randint(-5000, 5000), random.randint(-5000, 5000), random.randint(-5000, 5000))
    te.pensize(random.randint(0, 20))
    te.color(rgb2hex(random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)))
te.goto(0, 100)
te.goto(0, 0)
te.end_poly()
ploy = te.get_poly()
x = turtle.Shape('compound')
x.addcomponent(ploy, "black", "gray")
te.begin_poly()
te.goto(50, 0)
te.goto(50, 50)
te.goto(0, 50)
te.goto(0, 0)
te.end_poly()
ploy = te.get_poly()
x.addcomponent(ploy, "white", "gray")
screen.addshape('part', shape=x)
te.shape('part')
screen.tracer(1)
for loop in range(100):
    te.forward(random.randint(0, 100))
    te.left(random.randint(0, 100))
    te.forward(random.randint(0, 100))
    te.left(random.randint(0, 100))
screen.mainloop()
