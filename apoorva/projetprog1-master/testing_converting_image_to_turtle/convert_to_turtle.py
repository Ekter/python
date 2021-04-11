# -*- coding: utf-8 -*-
# Author: tfx2001
# License: GNU GPLv3
# Time: 2018-08-09 18:27
import os
import sys
import turtle as tu

import cv2
import numpy as np
from bs4 import BeautifulSoup
from win32.win32api import GetSystemMetrics

WriteStep = 15  # 贝塞尔函数的取样次数
Speed = 1000
Width = 600  # 界面宽度
Height = 600  # 界面高度
Xh = 0  # 记录前一个贝塞尔函数的手柄
Yh = 0
scale = (1, 1)
first = True
K = 32
Outfile = 'testgun.py'
file = open(Outfile, "a")


def Bezier(p1, p2, t):
    return p1 * (1 - t) + p2 * t


def Bezier_2(x1, y1, x2, y2, x3, y3):
    tu.goto(x1, y1)
    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4):
    x1 = -Width / 2 + x1
    y1 = Height / 2 - y1
    x2 = -Width / 2 + x2
    y2 = Height / 2 - y2
    x3 = -Width / 2 + x3
    y3 = Height / 2 - y3
    x4 = -Width / 2 + x4
    y4 = Height / 2 - y4
    tu.goto(x1, y1)
    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()


def Moveto(x, y):
    tu.penup()
    tu.goto(-Width / 2 + x, Height / 2 - y)
    tu.pendown()


def Moveto_r(dx, dy):
    tu.penup()
    tu.goto(tu.xcor() + dx, tu.ycor() - dy)
    tu.pendown()


def line(x1, y1, x2, y2):
    tu.penup()
    tu.goto(-Width / 2 + x1, Height / 2 - y1)
    tu.pendown()
    tu.goto(-Width / 2 + x2, Height / 2 - y2)
    tu.penup()


def Lineto_r(dx, dy):  # 连接当前点和相对坐标（dx，dy）的点
    tu.pendown()
    tu.goto(tu.xcor() + dx, tu.ycor() - dy)
    tu.penup()


def Lineto(x, y):  # 连接当前点和svg坐标下（x，y）
    tu.pendown()
    tu.goto(-Width / 2 + x, Height / 2 - y)
    tu.penup()


def Curveto(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到（x，y）
    tu.penup()
    X_now = tu.xcor() + Width / 2
    Y_now = Height / 2 - tu.ycor()
    Bezier_3(X_now, Y_now, x1, y1, x2, y2, x, y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def Curveto_r(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到相对坐标（x，y）
    tu.penup()
    X_now = tu.xcor() + Width / 2
    Y_now = Height / 2 - tu.ycor()
    Bezier_3(X_now, Y_now, X_now + x1, Y_now + y1,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def transform(w_attr):
    funcs = w_attr.split(' ')
    for func in funcs:
        func_name = func[0: func.find('(')]
        if func_name == 'scale':
            global scale
            scale = (float(func[func.find('(') + 1: -1].split(',')[0]),
                     -float(func[func.find('(') + 1: -1].split(',')[1]))


def readPathAttrD(w_attr):
    ulist = w_attr.split(' ')
    for i in ulist:
        # print("now cmd:", i)
        if i.isdigit() or i.isalpha():
            yield float(i)
        elif i[0].isalpha():
            yield i[0]
            yield float(i[1:])
        elif i[-1].isalpha():
            yield float(i[0: -1])
        elif i[0] == '-':
            yield float(i)


def drawSVG(filename, w_color):
    global first
    SVGFile = open(filename, 'r')
    SVG = BeautifulSoup(SVGFile.read(), 'lxml')
    Height = float(SVG.svg.attrs['height'][0: -2])
    Width = float(SVG.svg.attrs['width'][0: -2])
    try:
        transform(SVG.g.attrs['transform'])
    except KeyError:
        print('transform failed')
    if first:
        tu.setup(height=Height, width=Width)
        tu.setworldcoordinates(-Width / 2, 300, Width -
                               Width / 2, -Height + 300)
        first = False
    tu.tracer(1000000)
    tu.pensize(1)
    tu.speed(Speed)
    tu.penup()
    tu.color(w_color)
    file.write(f'te.tracer(1000000)\nte.pensize(1)\nte.speed({Speed})\nte.penup()\nte.color("{w_color}")\n')

    for i in SVG.find_all('path'):
        attr = i.attrs['d'].replace('\n', ' ')
        f = readPathAttrD(attr)
        lastI = ''
        for i in f:
            if i == 'M':
                tu.end_fill()
                tmp1 = next(f) * scale[0]
                tmp2 = next(f) * scale[1]
                Moveto(tmp1, tmp2)
                tu.begin_fill()
                file.write(f'''te.end_fill()\nMoveto({tmp1},{tmp2})\nte.begin_fill()\n''')
            elif i == 'm':
                tmp1 = next(f) * scale[0]
                tmp2 = next(f) * scale[1]
                tu.end_fill()
                Moveto_r(tmp1, tmp2)
                tu.begin_fill()
                file.write(f'''te.end_fill()\nMoveto_r({tmp1},{tmp2})\nte.begin_fill()\n''')
            elif i == 'C':
                tmp1 = next(f) * scale[0]
                tmp2 = next(f) * scale[1]
                tmp3 = next(f) * scale[0]
                tmp4 = next(f) * scale[1]
                tmp5 = next(f) * scale[0]
                tmp6 = next(f) * scale[1]
                Curveto(tmp1, tmp2,
                        tmp3, tmp4,
                        tmp5, tmp6)
                file.write(f'Curveto({tmp1}, {tmp2},{tmp3}, {tmp4},{tmp5}, {tmp6})\n')
                lastI = i
            elif i == 'c':
                tmp1 = next(f) * scale[0]
                tmp2 = next(f) * scale[1]
                tmp3 = next(f) * scale[0]
                tmp4 = next(f) * scale[1]
                tmp5 = next(f) * scale[0]
                tmp6 = next(f) * scale[1]
                Curveto_r(tmp1, tmp2,
                          tmp3, tmp4,
                          tmp5, tmp6)
                file.write(f'Curveto_r({tmp1}, {tmp2},{tmp3}, {tmp4},{tmp5}, {tmp6})\n')
                lastI = i
            elif i == 'L':
                tmp1 = next(f) * scale[0]
                tmp2 = next(f) * scale[1]
                Lineto(tmp1, tmp2)
                file.write(f'Lineto({tmp1}, {tmp2})\n')
            elif i == 'l':
                tmp1 = next(f) * scale[0]
                tmp2 = next(f) * scale[1]
                Lineto_r(tmp1, tmp2)
                file.write(f'Lineto_r({tmp1}, {tmp2})\n')
                lastI = i
            elif lastI == 'C':
                tmp1 = i * scale[0]
                tmp2 = next(f) * scale[1]
                tmp3 = next(f) * scale[0]
                tmp4 = next(f) * scale[1]
                tmp5 = next(f) * scale[0]
                tmp6 = next(f) * scale[1]
                Curveto(tmp1, tmp2,
                        tmp3, tmp4,
                        tmp5, tmp6)
                file.write(f'Curveto({tmp1}, {tmp2},{tmp3}, {tmp4},{tmp5}, {tmp6})\n')
            elif lastI == 'c':
                tmp1 = i * scale[0]
                tmp2 = next(f) * scale[1]
                tmp3 = next(f) * scale[0]
                tmp4 = next(f) * scale[1]
                tmp5 = next(f) * scale[0]
                tmp6 = next(f) * scale[1]
                Curveto_r(tmp1, tmp2,
                          tmp3, tmp4,
                          tmp5, tmp6)
                file.write(f'Curveto_r({tmp1}, {tmp2},{tmp3}, {tmp4},{tmp5}, {tmp6})\n')
            elif lastI == 'L':
                tmp1 = i * scale[0]
                tmp2 = next(f) * scale[1]
                Lineto(tmp1, tmp2)
                file.write(f'Lineto({tmp1}, {tmp2})\n')
            elif lastI == 'l':
                tmp1 = i * scale[0]
                tmp2 = next(f) * scale[1]
                Lineto_r(tmp1, tmp2)
                file.write(f'Lineto_r({tmp1}, {tmp2})\n')
    tu.penup()
    tu.hideturtle()
    tu.update()
    SVGFile.close()


def drawBitmap(w_image):
    print('Reducing the colors...')
    Z = w_image.reshape((-1, 3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)
    global K
    ret, label, center = cv2.kmeans(
        Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res = res.reshape(w_image.shape)
    no = 1
    for i in center:
        sys.stdout.write('\rDrawing: %.2f%% [' % (
                no / K * 100) + '#' * no + ' ' * (K - no) + ']')
        no += 1
        res2 = cv2.inRange(res, i, i)
        res2 = cv2.bitwise_not(res2)
        cv2.imwrite('.tmp.bmp', res2)
        os.system('potrace.exe .tmp.bmp -s --flat')
        print(i)
        drawSVG('.tmp.svg', '#%02x%02x%02x' % (i[2], i[1], i[0]))
    os.remove('.tmp.bmp')
    os.remove('.tmp.svg')
    print('\n\rFinished, close the window to exit.')
    tu.done()


# drawSVG('example00.svg',(255,255,255))

if __name__ == '__main__':
    K = 8
    filename = 'testgun.png'
    bitmapFile = open(filename, mode='r')
    bitmap = cv2.imread(filename)
    if bitmap.shape[0] > GetSystemMetrics(1):
        bitmap = cv2.resize(bitmap, (int(bitmap.shape[1] * (
                (GetSystemMetrics(1) - 50) / bitmap.shape[0])), GetSystemMetrics(1) - 50))
    drawBitmap(bitmap)
