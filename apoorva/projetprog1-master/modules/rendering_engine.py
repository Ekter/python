from turtle import Turtle, Screen, mainloop

from modules import background, gateau, sapin, table


class RenderingEngine:
    """ RenderingEngine is used to handle all elements connected to the graphical interface
    including all objects drawn on screen"""

    def __init__(self, _object_num, resolution=None):
        self._object_num = _object_num

        # init screen
        self.screen = Screen()
        self.screen.clear()
        self.screen.tracer(0)

        # Setting up screen
        self.screen.setup(width=1.0, height=1.0, startx=0, starty=0)
        self.screen.update()

        # getting screensize
        canvas = self.screen.getcanvas()
        root = canvas.winfo_toplevel()
        if not resolution:
            root.attributes('-fullscreen', True)
        if not resolution:
            self.screensize = root.winfo_width(), root.winfo_height()
        else:
            self.screensize = resolution
            self.screen.setup(resolution[0], resolution[1])
        self.scale = self.screensize[0] / 1366, self.screensize[1] / 768

        # hide base turtle
        for turtle_object in self.screen.turtles():
            turtle_object.ht()

        # Init objects
        self.gateau = gateau.Gateau(self._object_num, (0, -180 * self.scale[1]),
                                    scale=(3 * self.scale[0], 0.6 * self.scale[1]))
        self.table_object = table.Table(self.screen,
                                        scale=(1 * self.screensize[0] / 1366, 1.3 * self.scale[1]),
                                        start_pos=(0, -160))
        self.tree = sapin.Tree(scale=(1 * self.scale[0], 0.6 * self.scale[1]),
                               start_pos=(400, -200))

        self.tree2 = sapin.Tree(scale=(1 * self.scale[0], 0.6 * self.scale[1]),
                                start_pos=(-400, -200))

        self.background = background.Background(self.screen, scale=(
            1.52 * self.scale[0], 1.52 * self.scale[1]), start_pos=(-2.2, 0))

        # init text turtles
        self.drawing_turtles = {
            'player_name': Turtle(),
            'percentage': Turtle(),
        }
        self.drawing_turtles['player_name'].ht()
        self.drawing_turtles['player_name'].up()
        self.drawing_turtles['percentage'].ht()
        self.drawing_turtles['percentage'].up()

        self.screen.update()

    def initialise_turtles(self):
        """ draw all object for the first time"""
        self.background.draw()
        self.tree.draw(10)
        self.tree2.draw(10)
        self.table_object.draw()
        self.gateau.draw_init()
        self.screen.update()

    def refresh_screen_background(self):
        """ redraw every object except the cake"""
        self.background.tu.clear()
        self.tree.tu.clear()
        self.tree2.tu.clear()
        self.background.draw_sides()
        self.tree.tu.clear()
        self.tree.draw(10)
        self.tree2.draw(10)

    def update(self, _render_list, playing_index):
        """ update the cake"""
        # changing animation points
        if playing_index:
            self.gateau.middle_pos = self.table_object.plate.center_pos[0], self.table_object.plate.center_pos[
                1] + 500 * self.scale[1]
            self.gateau.end_point = self.table_object.plate.center_pos
        else:
            self.gateau.middle_pos = self.table_object.plate2.center_pos[0], self.table_object.plate2.center_pos[
                1] + 500 * self.scale[1]
            self.gateau.end_point = self.table_object.plate2.center_pos
        # running the update in gateau object
        self.gateau.update(_render_list)
        self.screen.update()

    def write_text(self, pos, text, percentage=None):
        """takes a position a string and a bool(to get which turtle to target)
            and writes text at a certain pos on screen"""
        self.drawing_turtles['player_name'].clear()
        self.drawing_turtles['player_name'].goto(int(pos[0] * self.scale[0]), int(pos[1] * self.scale[1]))
        # self.drawing_turtles['player_name'].color('deep pink')
        style = ('Courier', 30 * int((self.scale[0] + self.scale[1]) / 2), 'normal')
        self.drawing_turtles['player_name'].write(text, font=style, align='center')
        if percentage:
            self.drawing_turtles['percentage'].clear()
            self.drawing_turtles['percentage'].goto(int(pos[0] * self.scale[0]), int(pos[1] * self.scale[1]))
            # self.drawing_turtles['percentage'].color('deep pink')
            style = ('Courier', 30 * int((self.scale[0] + self.scale[1]) / 2), 'normal')
            self.drawing_turtles['percentage'].write(text, font=style, align='center')

    def get_input(self, text=None):
        """ takes input from user, can in a text to show to user  """
        if text:
            return self.screen.textinput(text[0], text[1])
        else:
            return self.screen.textinput("Input", "format {ligne}:{tirer})")

    def show_winner(self, winner):
        """ draws winner name"""
        self.write_text((0, -350), 'The winner is ' + winner)
        self.screen.update()
        # self.drawing_turtles['player_name'].clear()

    def reset(self, object_num):
        """ reset the rendering engine to prepare for next game"""
        self._object_num = object_num
        self.gateau = gateau.Gateau(self._object_num, (0, -180 * self.scale[1]),
                                    scale=(3 * self.scale[0], 0.6 * self.scale[1]))


if __name__ == '__main__':
    rendering = RenderingEngine(10, resolution=(500, 500))
    rendering.initialise_turtles()
    rendering.show_winner('asdasds')
    mainloop()
