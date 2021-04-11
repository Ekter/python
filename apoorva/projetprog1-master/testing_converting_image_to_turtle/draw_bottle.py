import turtle
import time
from PIL import Image
import math
tu = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0)
scale = [1,1]
screen.bgpic('resied_bottole.png')
def resize_image(x,_input, _output):
    # Opens a image in RGB mode
    im = Image.open(_input)
    width, height = im.size
    im = im.resize((width * 2, height * 2))
    im.save(_output)
    im.close()

def apply_scale(x, y):
    return x * scale[0], y * scale[1]

def gotoandprint(x, y):
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    return gotoresult
string='''0.0 -295.0
48.0 -296.0
58.0 -292.0
68.0 -288.0
72.0 -284.0
75.0 -278.0
77.0 17.0
41.0 81.0
31.0 240.0
35.0 252.0
33.0 263.0
31.0 271.0
37.0 274.0
31.0 293.0
-32.0 297.0
-40.0 276.0
-35.0 274.0
-31.0 269.0
-39.0 254.0
-32.0 240.0
-48.0 74.0
-70.0 47.0
-78.0 22.0
-78.0 -11.0
-77.0 -262.0
-72.0 -279.0
-67.0 -288.0
-59.0 -291.0
-49.0 -295.0
-22.0 -297.0
0.0 -295.0
'''

string=string.split('\n')
tu.begin_poly()
for part in string:
    try:
        x, y = part.split(' ')
        tu.goto(apply_scale(float(x), float(y)))
    except ValueError:
        pass
tu.end_poly()
shape=tu.get_poly()
screen.addshape('bottle',shape=shape)
tu.shape('bottle')
while True:
    scale=[1,1]
    for loop in range(1000):
        tu.left(10)
        time.sleep(1/24)
        tu.clear()
        tu.color('green')
        scale[1]=math.cos(loop/10)
        tu.begin_poly()
        for part in string:
            try:
                x,y=part.split(' ')
                tu.goto(apply_scale(float(x)*math.sin(loop-10)/10, float(y)*math.sin(loop-10)/10))
            except ValueError:
                pass
        tu.end_poly()
        screen.update()

resize_image(3,'beer-bottle-clip-art-9.png','resied_bottole.png')
screen.onscreenclick(gotoandprint)
screen.mainloop()