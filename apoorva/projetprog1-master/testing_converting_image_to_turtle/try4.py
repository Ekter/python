
import turtle
tu =turtle.Turtle()
screen = turtle.Screen()
tu.penup()
scale=[1,1]
def apply_scale(x, y):
    return x * scale[0], y * scale[1]
# STARTOFDRAW
def draw(tu):
    tu.color("red")
    tu.pensize(3)
    tu.up()
    tu.goto(apply_scale(0,0))
    tu.down()
    tu.goto(apply_scale(175.0,100.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(175.0,100.0))
    tu.down()
    tu.goto(apply_scale(-42.0,161.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-42.0,161.0))
    tu.down()
    tu.goto(apply_scale(-142.0,16.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-142.0,16.0))
    tu.down()
    tu.goto(apply_scale(77.0,-112.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(77.0,-112.0))
    tu.down()
    tu.goto(apply_scale(141.0,-21.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(141.0,-21.0))
    tu.down()
    tu.goto(apply_scale(-125.0,-91.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-125.0,-91.0))
    tu.down()
    tu.goto(apply_scale(-43.0,101.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-43.0,101.0))
    tu.down()
    tu.goto(apply_scale(-33.0,-104.0))
    tu.up()
    tu.up()
    tu.goto(apply_scale(-33.0,-104.0))
    tu.down()
    tu.goto(apply_scale(-260.0,12.0))
    tu.up()
    tu.color("red")
    tu.pensize(3)
# ENDOFDRAW
if __name__ == '__main__':
    draw(tu)