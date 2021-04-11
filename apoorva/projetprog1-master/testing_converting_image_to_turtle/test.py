# from main import *
import random
import turtle


def test_render_w_text():
    assert render_w_text([[0, 6]], 7) == '|||||||'
    assert render_w_text([[0, 6]], 10) == '|||||||...'
    assert render_w_text([[0, 1], [4, 6], [8, 8]], 10) == '||..|||.|.'
    print('test compllete')


def calculate_parts(_currently_playing):
    """
    :param _currently_playing: pointer to the part of the _objects_up_list
    :returns tuple of the ranges of each split list
    function that splits a range in 2 ranges"""
    # create a list from the ranges
    _list = list(range(_currently_playing[0], _currently_playing[1] + 1))
    length = len(_list)
    if len(_list) % 2 == 0:
        # if the list contains only 2 elements send instruction to delete the line
        if len(_list) == 2:
            return "del line"
        # split the list into two lists while removing the two middle elements as the list has an even count of elements
        part1 = _list[:length // 2 - 1]
        part2 = _list[length // 2 + 1:]
    else:
        # split the list into two lists while removing the middle elements as the list has an odd count of elements
        if random.getrandbits(1):
            part1 = _list[:length // 2 - 1]
            part2 = _list[length // 2 + 1:]
        else:
            part1 = _list[:length // 2]
            part2 = _list[length // 2 + 2:]
    return [part1[0], part1[-1]], [part2[0], part2[-1]]


def render_w_text(_objects_up_list, object_num):
    """Renders the game in the terminal in text form"""
    _render_list = ["."] * object_num  # initilise a list of "."
    # fill in the list with "|" in the indexes of the upwards facing objects
    for _range in _objects_up_list:
        for _index in range(_range[0], _range[1] + 1):
            _render_list[_index] = '|'
    print(f"Voici les quilles, il y a {len(_objects_up_list)} lignes")
    # convert list into string
    print("".join(_render_list))
    return "".join(_render_list)




unVar1 = 25
unVar2 = 100
unVar3 = 90
unVar4 = 150
unVar5 = -30
unVar6 = 75
unVar7 = 50

def polySquare(t, x, y, length):
    t.goto(x, y)
    t.setheading(270)

    t.begin_poly()

    for count in range(4):
        t.forward(length)
        t.left(90)

    t.end_poly()

    return t.get_poly()


def polyRectangle(t, x, y, length1, length2):
    t.goto(x, y)
    t.setheading(270)

    t.begin_poly()

    for count in range(2):
        t.forward(length1)
        t.left(90)
        t.forward(length2)
        t.left(90)

    t.end_poly()

    return t.get_poly()


def tankCursor():

    """
    Create the tank cursor.  An alternate solution is to toss the temporary turtle
    and use the commented out polygon assignments instead of the poly* function calls
    """

    temporary = turtle.Turtle()

    screen = turtle.getscreen()

    delay = screen.delay()

    screen.delay(0)

    temporary.hideturtle()
    temporary.penup()

    tank = turtle.Shape("compound")

    # bodyTank = ((20, unVar3), (20, unVar3 - 130), (20 + 110, unVar3 - 130), (20 + 110, unVar3))
    bodyTank = polyRectangle(temporary, 20, unVar3, 130, 110)
    tank.addcomponent(bodyTank, "black", "gray")


    turtle.addshape("tank", shape=tank)

    del temporary

    screen.delay(delay)

tankCursor()  # creates and registers the "tank" cursor shape

turtle.shape("tank")

turtle.up()  # get rid of the ink

# show our tank in motion

turtle.setheading(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)

turtle.done()