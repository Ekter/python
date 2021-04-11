import datetime
import math
from turtle import Turtle, Screen


class Clock:
    def __init__(self, _screen, scale, pos):
        self.screen = _screen
        self.currentDT = datetime.datetime.now()
        self.scale = scale
        self.pos = pos
        self.circle_scale = (self.scale[0] + self.scale[1]) / 2
        self.text_size = int(50 * self.circle_scale)
        # output current time
        self.currentHour = self.currentDT.hour
        if self.currentHour > 12:
            self.currentHour = self.currentHour - 12
        self.currentMinute = self.currentDT.minute
        if self.currentMinute < 10:
            print("Time logged in at - " + str(self.currentHour) + ":0" + str(self.currentMinute))
        else:
            print("Time logged in at - " + str(self.currentHour) + ":" + str(self.currentMinute))

        # outside circle
        circle = Turtle()
        circle.penup()
        circle.pencolor("black")
        circle.speed(0)
        circle.hideturtle()
        circle.goto(self.apply_scale(0, -370))
        circle.pendown()
        circle.fillcolor("gold")
        circle.begin_fill()
        circle.circle(380 * self.circle_scale)
        circle.end_fill()

        # outside outside circle
        circle = Turtle()
        circle.penup()
        circle.pencolor("black")
        circle.speed(0)
        circle.pensize(35 * self.circle_scale)
        circle.hideturtle()
        circle.goto(self.apply_scale(0, -390))
        circle.pendown()
        circle.fillcolor("gold")
        circle.begin_fill()
        circle.circle(400 * self.circle_scale)
        circle.end_fill()

        # hour hand
        self.hour_hand = Turtle()
        self.hour_hand.up()
        self.hour_hand.shape("arrow")
        self.hour_hand.color("black")
        self.hour_hand.speed(10)
        self.hour_hand.goto(self.apply_scale(0, 0))
        self.hour_hand.shapesize(stretch_wid=0.4 * self.circle_scale, stretch_len=18 * self.circle_scale)

        # minute hand
        self.minute_hand = Turtle()
        self.minute_hand.up()
        self.minute_hand.shape("arrow")
        self.minute_hand.color("black")
        self.minute_hand.speed(10)
        self.minute_hand.goto(self.apply_scale(0, 0))
        self.minute_hand.shapesize(stretch_wid=0.4 * self.circle_scale, stretch_len=26 * self.circle_scale)

        # second hand
        self.second_hand = Turtle()
        self.second_hand.up()
        self.second_hand.shape("arrow")
        self.second_hand.color("dark red")
        self.second_hand.speed(10)
        self.second_hand.goto(self.apply_scale(0, 0))
        self.second_hand.shapesize(stretch_wid=0.4 * self.circle_scale, stretch_len=36 * self.circle_scale)

        # inside circle
        self.inside_bore = Turtle()
        self.inside_bore.up()
        self.inside_bore.shape("circle")
        self.inside_bore.color("black")
        self.inside_bore.goto(self.apply_scale(0, 0))
        self.inside_bore.shapesize(stretch_wid=1.5 * self.circle_scale, stretch_len=1.5 * self.circle_scale)

        # numbers with pen
        pen = Turtle()
        pen.speed(0)
        pen.color("black")
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(0, 300))
        pen.write("12", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(340, -30))
        pen.write("3", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(0, -370))
        pen.write("6", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(-340, -30))
        pen.write("9", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(170, 260))
        pen.write("1", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(-160, 260))
        pen.write("11", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(300, 140))
        pen.write("2", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(-280, 140))
        pen.write("10", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(300, -200))
        pen.write("4", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(-300, -200))
        pen.write("8", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(170, -325))
        pen.write("5", align="center", font=("Courier", self.text_size, "normal"))
        pen.penup()
        pen.hideturtle()
        pen.goto(self.apply_scale(-170, -325))
        pen.write("7", align="center", font=("Courier", self.text_size, "normal"))
        #self.draw_graduations(1000, pen)
        # on timer infinite loop
        self.currentHourInternal = datetime.datetime.now().hour
        self.currentMinuteInternal = datetime.datetime.now().minute
        self.currentSecondInternal = datetime.datetime.now().second
        _screen.ontimer(self.move_hour_hand, 1)
        _screen.ontimer(self.move_minute_hand, 1)
        _screen.ontimer(self.move_second_hand, 1)

    def apply_scale(self, x, y):
        return (x + self.pos[0]) * self.scale[0], (y + self.pos[1]) * self.scale[1]

    def draw_graduations(self, resolution, tu):

        x, y = self.apply_scale(0, 0)
        radius = 380 * self.circle_scale
        tu.pendown()
        perimeter = math.pi * (2 * radius)
        cote = perimeter / resolution
        tu.penup()
        tu.goto(x, y - radius)
        tu.penup()
        tu.pendown()
        # tu.color(color[0], color[1])
        # tu.begin_fill()
        for counter in range(resolution):
            tu.forward(cote)
            tu.left(360 / resolution)
            if counter % 100 == 0:
                old_heading = tu.heading()
                old_pos = tu.pos()
                tu.setheading(tu.towards(self.apply_scale(0, 0)))
                tu.forward(10)
                tu.goto(old_pos)
                tu.setheading(old_heading)

        # tu.end_fill()
        tu.penup()
        tu.color(0, 0, 0)


    # moving hour hand
    def move_hour_hand(self):
        self.currentHourInternal = datetime.datetime.now().hour
        degree = (self.currentHourInternal - 15) * -30
        self.currentMinuteInternal = datetime.datetime.now().minute
        degree = degree + -0.5 * self.currentMinuteInternal
        self.hour_hand.setheading(degree)
        self.inside_bore.goto(self.apply_scale(0, 0))
        self.screen.ontimer(self.move_hour_hand, 60000)

    # moving minute hand
    def move_minute_hand(self):
        self.currentMinuteInternal = datetime.datetime.now().minute
        degree = (self.currentMinuteInternal - 15) * -6
        self.currentSecondInternal = datetime.datetime.now().second
        degree = degree + (-self.currentSecondInternal * 0.1)
        self.minute_hand.setheading(degree)
        self.inside_bore.goto(self.apply_scale(0, 0))
        self.screen.ontimer(self.move_minute_hand, 1000)

    # moving second hand
    def move_second_hand(self):
        self.currentSecondInternal = datetime.datetime.now().second
        degree = (self.currentSecondInternal - 15) * -6
        self.second_hand.setheading(degree)
        self.inside_bore.goto(self.apply_scale(0, 0))
        self.screen.ontimer(self.move_second_hand, 1000)


if __name__ == '__main__':
    screen = Screen()
    clock = Clock(screen, [0.5, 0.5], (0, 0))
    screen.mainloop()
