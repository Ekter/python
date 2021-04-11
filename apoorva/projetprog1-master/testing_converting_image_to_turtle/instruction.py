import turtle

tu = turtle.Turtle()


def round_rectangle(center_x, center_y, width, height, cornersize):
    turtle.up()
    turtle.goto(center_x - width / 2 + cornersize, center_y - height / 2)
    turtle.down()
    for _ in range(2):
        turtle.fd(width - 2 * cornersize)
        turtle.circle(cornersize, 90)
        turtle.fd(height - 2 * cornersize)
        turtle.circle(cornersize, 90)


round_rectangle(0,0,100,100,10)