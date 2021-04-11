import turtle as te

WriteStep = 15  # resolution
Speed = 1000
Width = 600
Height = 600
Xh = 0
Yh = 0
scale = (1, 1)
first = True
K = 32
te.setup(height=Height, width=Width)
te.setworldcoordinates(-Width / 2, 300, Width -
                       Width / 2, -Height + 300)


def Bezier(p1, p2, t):  # 一阶贝塞尔函数
    return p1 * (1 - t) + p2 * t


def Bezier_2(x1, y1, x2, y2, x3, y3):  # 二阶贝塞尔函数
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4):  # 三阶贝塞尔函数
    x1 = -Width / 2 + x1
    y1 = Height / 2 - y1
    x2 = -Width / 2 + x2
    y2 = Height / 2 - y2
    x3 = -Width / 2 + x3
    y3 = Height / 2 - y3
    x4 = -Width / 2 + x4
    y4 = Height / 2 - y4  # 坐标变换
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


def Moveto(x, y):  # 移动到svg坐标下（x，y）
    te.penup()
    te.goto(-Width / 2 + x, Height / 2 - y)
    te.pendown()


def Moveto_r(dx, dy):
    te.penup()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    te.pendown()


def line(x1, y1, x2, y2):  # 连接svg坐标下两点
    te.penup()
    te.goto(-Width / 2 + x1, Height / 2 - y1)
    te.pendown()
    te.goto(-Width / 2 + x2, Height / 2 - y2)
    te.penup()


def Lineto_r(dx, dy):  # 连接当前点和相对坐标（dx，dy）的点
    te.pendown()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    te.penup()


def Lineto(x, y):  # 连接当前点和svg坐标下（x，y）
    te.pendown()
    te.goto(-Width / 2 + x, Height / 2 - y)
    te.penup()


def Curveto(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到（x，y）
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, x1, y1, x2, y2, x, y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def Curveto_r(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到相对坐标（x，y）
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, X_now + x1, Y_now + y1,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2
