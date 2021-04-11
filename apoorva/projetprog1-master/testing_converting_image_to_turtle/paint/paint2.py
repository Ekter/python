import importlib.util
import os
import turtle


HEADER='''
WriteStep = 20
Height = 500
Width = 500
scale=[1,1]
def apply_scale(x, y):
    return x * scale[0], y * scale[1]
def apply_scale_bezier_2(x1, y1, x2, y2, x3, y3,tu):
    return x1*scale[0], y1*scale[1], x2*scale[0], y2*scale[1], x3*scale[0], y3*scale[1],tu
def apply_scale_bezier_3(x1, y1, x2, y2, x3, y3, x4, y4,tu):
    return x1*scale[0], y1*scale[1], x2*scale[0], y2*scale[1], x3*scale[0], y3*scale[1],x4*scale[0], y4*scale[1],tu
def Bezier(p1, p2, t):  
    return p1 * (1 - t) + p2 * t


def Bezier_2(x1, y1, x2, y2, x3, y3,tu):  
    tu.goto(x1, y1)
    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4,tu):  

    tu.goto(x1, y1)
    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()
# STARTOFDRAW
def draw(tu):

'''
def _save_file(input_filename=None):
    """Loads a turtle save file or creates ones if none is passed"""
    global f, current_filename
    f.close()
    if input_filename:
        # parsing file name
        filename = input_filename
        filename = filename.split('.')
        filename = filename[0].split('_')
        filename_index = filename[2]

        # read file and extract draw function
        save_file = open(f'paint_save_{filename_index}.py', 'r')
        draw_func = []
        add_to_fuc = False
        for line in save_file.readlines():
            if line == '# STARTOFDRAW\n':
                add_to_fuc = True
            if line == '# ENDOFDRAW\n':
                add_to_fuc = False
            if add_to_fuc:
                draw_func.append(line)
        print(draw_func)
        draw_func.pop(0)
        draw_func.pop(0)
        print(draw_func)
        save_file.close()
        # importing draw from save file
        spec = importlib.util.spec_from_file_location('input_module', f'paint_save_{filename_index}.py')
        input_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(input_module)
        # draw func
        input_module.draw(tu)
        # naming next file name
        current_filename = f'paint_save_{int(filename_index) + 1}.py'
        f = open(f'paint_save_{int(filename_index) + 1}.py', 'w')
        f.write(HEADER)
        f.writelines(draw_func)

    else:
        f = open('paint_save_0.py', 'w')
        current_filename = 'paint_save_0.py'
        f.write(HEADER)
        f.write('''    tu.goto(0,0)\n''')


def apply_scale(x, y):
    return x * scale[0], y * scale[1]


def reverse():
    """ reverses inputs by loading old save file"""
    global _inputs
    _inputs = []
    tu.clear()

    filename = current_filename
    filename = filename.split('.')
    filename = filename[0].split('_')
    filename_index = filename[2]
    _save_file(f'paint_save_{int(filename_index) - 2}.py')
    screen.update()


def draw_line(x, y, x1, y1):
    """draws lines and writes to save file"""
    tu.up()
    f.write(f'''    tu.up()\n''')
    tu.goto(x, y)
    f.write(f'''    tu.goto(apply_scale({x},{y}))\n''')
    tu.down()
    f.write(f'''    tu.down()\n''')
    tu.goto(x1, y1)
    f.write(f'''    tu.goto(apply_scale({x1},{y1}))\n''')
    tu.up()
    f.write(f'''    tu.up()\n''')
    f.close()
    screen.update()
    _save_file(current_filename)


def Bezier(p1, p2, t):
    return p1 * (1 - t) + p2 * t


def Bezier_2(x1, y1, x2, y2, x3, y3):
    """draws Bezier2 and writes to save file"""
    f.write('    #tracing bezier2\n')

    f.write(f'''
    x1, y1, x2, y2, x3, y3, tu = apply_scale_bezier_2({x1}, {y1}, {x2}, {y2}, {x3}, {y3},tu)
    Bezier_2(x1, y1, x2, y2, x3, y3,tu)\n''')
    tu.goto(x1, y1)

    tu.pendown()

    # f.write(f'''    tu.goto(apply_scale({x1},{y2}))\n''')

    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        tu.goto(x, y)
    tu.penup()
    screen.update()
    f.close()
    _save_file(current_filename)


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4):
    """draws Bezier3 and writes to save file"""
    f.write('    #tracing bezier3\n')
    f.write(f'''
    x1, y1, x2, y2, x3, y3, x4, y4, tu = apply_scale_bezier_3({x1}, {y1}, {x2}, {y2}, {x3}, {y3}, {x4}, {y4},tu)
    Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4,tu)\n''')
    # f.write(f'''  tu.goto(apply_scale({x1},{y1}))\n''')
    tu.goto(x1, y1)

    tu.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)

        tu.goto(x, y)

    tu.penup()
    screen.update()
    f.close()
    _save_file(current_filename)


def change_input_to_bezier():
    """handle input :change to bezier"""
    global input_type, _inputs, last_pos_snapping
    input_type = 'bezier'
    if last_pos_snapping:
        _inputs = [last_pos[0], last_pos[1]]
    else:
        _inputs = []
    info_turtle.clear()
    info_turtle.write('mode ' + input_type)
    screen.onscreenclick(stack_bezier_inputs)


def change_input_to_point():
    """handle input :change to point"""
    global input_type, _inputs, last_pos_snapping
    input_type = 'point'
    if last_pos_snapping:
        _inputs = [last_pos[0], last_pos[1]]
    else:
        _inputs = []
    info_turtle.clear()
    info_turtle.write('mode ' + input_type)
    screen.onscreenclick(stack_line_inputs)


def change_input_to_bezier_3():
    """handle input :change to bezier3"""
    global input_type, _inputs, last_pos_snapping
    input_type = 'bezier3'
    if last_pos_snapping:
        _inputs = [last_pos[0], last_pos[1]]
    else:
        _inputs = []
    info_turtle.clear()
    info_turtle.write('mode ' + input_type)
    print('bezeir', _inputs)
    screen.onscreenclick(stack_bezier3_inputs)


def dragging(x, y):  # These parameters will be the mouse position
    """freedraw function"""
    global last_pos
    tu.ondrag(None)
    tu.setheading(tu.towards(x, y))
    tu.goto(x, y)
    f.write(f'''    tu.goto(apply_scale({x},{y}))\n''')
    last_pos = [x, y]
    tu.ondrag(dragging)
    screen.update()


def change_input_to_free_draw():
    """handle input :change to free draw"""
    global input_type
    input_type = 'freedraw'
    info_turtle.clear()
    screen.onscreenclick(tu.goto)
    screen.onkeypress(tu_down, 'z')
    screen.onkeyrelease(tu_up, 'z')
    info_turtle.write('mode ' + input_type)
    tu.ondrag(dragging)
    screen.update()
    f.close()
    _save_file(current_filename)


def stack_bezier_inputs(x, y):
    """handle input :stack bezier inputs"""
    global _inputs, last_pos, last_pos_snapping
    _inputs.append(x)
    _inputs.append(y)

    if len(_inputs) == 6:
        Bezier_2(_inputs[0], _inputs[1], _inputs[2], _inputs[3], _inputs[4],
                 _inputs[5])
        last_pos = [_inputs[4], _inputs[5]]
        if last_pos_snapping:
            _inputs = [last_pos[0], last_pos[1]]
        else:
            _inputs = []


def stack_bezier3_inputs(x, y):
    """handle input :stack bezier3 inputs"""
    global _inputs, last_pos, last_pos_snapping
    if last_pos_snapping:
        print(_inputs)
    _inputs.append(x)
    _inputs.append(y)

    if len(_inputs) == 8:
        Bezier_3(_inputs[0], _inputs[1], _inputs[2], _inputs[3], _inputs[4],
                 _inputs[5], _inputs[6], _inputs[7])
        last_pos = [_inputs[6], _inputs[7]]
        if last_pos_snapping:
            _inputs = [last_pos[0], last_pos[1]]
        else:
            _inputs = []


def stack_line_inputs(x, y):
    """handle input :stack line inputs"""
    global _inputs, last_pos, last_pos_snapping
    if last_pos_snapping:
        print(_inputs)
    if x_snapping:
        _inputs.append(x)
        _inputs.append(last_pos[1])
    elif y_snapping:
        _inputs.append(last_pos[0])
        _inputs.append(y)
    else:
        _inputs.append(x)
        _inputs.append(y)

    if len(_inputs) == 4:
        draw_line(_inputs[0], _inputs[1], _inputs[2], _inputs[3])
        last_pos = [_inputs[2], _inputs[3]]
        if last_pos_snapping:
            _inputs = [last_pos[0], last_pos[1]]
        else:
            _inputs = []


def snap_to_last_pos():
    """update last point snapping"""
    global last_pos_snapping
    info_turtle2.clear()
    last_pos_snapping = not last_pos_snapping
    info_turtle2.write('last point snapping ' + str(last_pos_snapping))
    screen.update()


def snap_y():
    """snap the y axis"""
    global y_snapping, x_snapping
    if x_snapping:
        x_snapping = not x_snapping
    y_snapping = not y_snapping
    info_turtle3.clear()
    info_turtle3.write('y_snapping ' + str(y_snapping))
    info_turtle4.clear()
    info_turtle4.write('x_snapping ' + str(x_snapping))
    screen.update()


def snap_x():
    """snap the x axis"""
    global x_snapping, y_snapping
    if y_snapping:
        y_snapping = not y_snapping
    x_snapping = not x_snapping
    info_turtle3.clear()
    info_turtle3.write('y_snapping ' + str(y_snapping))
    info_turtle4.clear()
    info_turtle4.write('x_snapping ' + str(x_snapping))
    screen.update()


# rewriting turtle functions to save to file
def begin_fill():
    tu.begin_fill()
    screen.update()
    f.write('    tu.begin_fill()\n')


def begin_poly():
    global in_poly
    tu.begin_fill()
    tu.begin_poly()
    screen.update()
    in_poly = True
    f.write('    tu.begin_poly()\n')
    info_turtle_in_poly.clear()
    info_turtle_in_poly.write('in_poly:' + str(in_poly))


def end_fill():
    tu.end_fill()
    screen.update()
    f.write('    tu.end_fill()\n')
    f.close()
    _save_file(current_filename)


def end_poly():
    global in_poly
    if in_poly:
        tu.end_fill()
        tu.end_poly()
        f.write('    tu.end_poly()\n')
        shape_name = screen.textinput('name of shape', 'onegai snepai')
        shape = tu.get_poly()
        f.write(f'    shape=tu.get_poly()\n')
        print(shape_name, shape)
        screen.addshape(shape_name, shape=shape)
        f.write(f'    screen.addshape("{shape_name}", shape=shape)\n')
        f.write(f'    print(screen._shapes)\n')
        in_poly = False
    else:
        print('poly has not started')
    info_turtle_in_poly.clear()
    info_turtle_in_poly.write('in_poly:' + str(in_poly))
    screen.update()
    f.close()
    _save_file(current_filename)


def tu_up():
    tu.up()
    f.write(f'    tu.up()\n')


def tu_down():
    tu.down()
    f.write(f'    tu.down()\n')


def change_color():
    color = screen.textinput('hexcolor', 'onegai snepai')
    tu.color(color)
    screen.update()
    f.write(f'    tu.color("{color}")\n')
    screen.listen()
    screen.mainloop()
    f.close()
    _save_file(current_filename)


def change_pensize():
    pensize = screen.textinput('pensize', 'onegai snepai')
    tu.pensize(pensize)
    screen.update()
    f.write(f'    tu.pensize("{pensize}")\n')
    screen.listen()
    screen.mainloop()
    f.close()
    _save_file(current_filename)


# end of rewriting turtle functions to save to file


# init file class
f = open('dummy.tmp', 'w')
f.close()
os.remove('dummy.tmp')
current_filename = ''
# init global state variables
last_pos = [0, 0]
last_pos_snapping = False
y_snapping = False
x_snapping = False
in_poly = False
scale = [1, 1]
_inputs = []  # global var to store stacking inputs
input_type = 'point'  # global var to store current input type

WriteStep = 20
Height = 500
Width = 500

# init screen and main turtle
screen = turtle.Screen()
screen.tracer(0)
screen.bgpic(picname='background_resised.png')
tu = turtle.Turtle()
tu.up()

# init info turtles
info_turtle = turtle.Turtle()
info_turtle.penup()
info_turtle.goto(-Width / 2 + 100, Height / 2 - 100)
info_turtle.write('mode ' + input_type)
info_turtle2 = turtle.Turtle()
info_turtle2.penup()
info_turtle2.goto(-Width / 2 + 50, Height / 2 - 50)
info_turtle2.write('last point snapping ' + str(last_pos_snapping))
info_turtle3 = turtle.Turtle()
info_turtle3.penup()
info_turtle3.goto(-Width / 2 + 150, Height / 2 - 150)
info_turtle3.write('y_snapping ' + str(y_snapping))
info_turtle4 = turtle.Turtle()
info_turtle4.penup()
info_turtle4.goto(-Width / 2 + 200, Height / 2 - 200)
info_turtle4.write('x_snapping ' + str(x_snapping))
info_turtle_in_poly = turtle.Turtle()
info_turtle_in_poly.penup()
info_turtle_in_poly.goto(-Width / 2 + 40, Height / 2 - 40)
info_turtle_in_poly.write('in_poly:' + str(in_poly))
screen.update()
_save_file('')
tu.color('black')
f.write('''    tu.color('black')\n''')

# handling inputs
change_input_to_point()
screen.onkey(change_input_to_bezier, "q")
screen.onkey(change_input_to_point, "w")
screen.onkey(change_input_to_bezier_3, "e")
screen.onkey(change_input_to_free_draw, 'f')
screen.onkey(snap_to_last_pos, 'a')
screen.onkey(snap_y, 'z')
screen.onkey(snap_x, 'x')
screen.onkey(begin_fill, '1')
screen.onkey(end_fill, '2')
screen.onkey(change_color, 'c')
screen.onkey(change_pensize, 'l')
screen.onkey(begin_poly, 's')
screen.onkey(end_poly, 'd')
screen.onkey(reverse, 'v')
screen.listen()
screen.mainloop()
# writing to file
f.write('''# ENDOFDRAW\n''')
f.write('''if __name__ == '__main__':
    import turtle
    print('is main')
    tu =turtle.Turtle()
    screen = turtle.Screen()
    tu.penup()
    draw(tu)
    ''')
f.close()
