#!../venv/bin/python3

from pynput import mouse
import time
import tkinter as tk
import shapes3D
import math


def on_move(x, y):
    # print('Pointer moved to {0}'.format(
    #     (x, y)))
    if (x!=mainApp().scene.default_position[0] or y!=mainApp().scene.default_position[1]) and mainApp().scene.block:
        mainApp().scene.x = x
        mainApp().scene.y = y
        if mainApp().scene.block:
            # mainApp().scene.ctrl.position = mainApp().scene.default_position
            # mainApp().scene.ctrl.move(1200, 700)
            print("blocked")

    # mainApp().frame.line(x, y, x+1, y+1)


def on_click(x, y, button, pressed):
    print('{0} at {1} with button {2}'.format(
        'Pressed' if pressed else 'Released',
        (x, y), button))
    mainApp().scene.block = pressed
    if pressed:
        #m.x-m.offset const
        #m.x <= x
        mainApp().scene.x_offset += x-mainApp().scene.x
        mainApp().scene.y_offset += y-mainApp().scene.y
        mainApp().scene.x = x
        mainApp().scene.y = y


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    mainApp().scene.norm *=(1.1)** dy


class MyFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.listener = mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll)
        self.listener.start()
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        # self.objs = []

    def line(self, x1, y1, x2, y2, color="black"):
        self.canvas.create_line(x1, y1, x2, y2, fill="black")

    def fill_triangle(self, x1, y1, x2, y2, x3, y3, color="grey"):
        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)
        # self.objs.append(obj)


class Scene:
    def __init__(self) -> None:
        self.default_position = (1200,700)
        self.x = self.default_position[0]
        self.y = self.default_position[1]
        self.x_offset = self.default_position[0]
        self.y_offset = self.default_position[1]
        self.norm = 1
        self.block = False
        self.ctrl = mouse.Controller()
        self.ctrl.position=(self.x, self.y)
        self.objects : list[shapes3D.Drawable] = []
        self.vertexes : list[shapes3D.Drawable] = []
        self.update_project()

    def add(self, obj):
        self.objects.append(obj)

    def draw(self, frame: MyFrame):
        frame.canvas.delete("all")
        for obj in self.objects:
            obj.draw(frame, plan=self.plan)
            obj.draw_lines(frame, plan=self.plan)

    def update_project(self):
        self.plan = shapes3D.OrthoPlan(shapes3D.Coord3(0, 0, 0),
                    shapes3D.Vector3(math.cos((self.x - self.x_offset)/500), 0, math.sin((self.x - self.x_offset)/500))*self.norm,
                    shapes3D.Vector3(0, math.cos((self.y - self.y_offset)/500), math.sin((self.y - self.y_offset)/500))*self.norm)


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("2400x1400")
        # self.root.attributes('-fullscreen', True)
        self.root.title("Lines")
        self.frame = MyFrame()
        self.scene = Scene()

    def begin(self):
        self.frame.update_idletasks()
        self.frame.update()
        # self.frame.mainloop()

    def update(self):
        t = time.time()
        self.scene.update_project()
        self.scene.draw(self.frame)
        self.frame.update_idletasks()
        self.frame.update()
        print(time.time()-t)
        self.frame.after(30, self.update)


def mainApp(app: App = App()) -> App:
    return app


mainApp().begin()


def main():
    t = time.time()
    # parelo = shapes3D.Parallelepidedon(
    #     shapes3D.Coord3(0, 0, 0), shapes3D.Coord3(10, 10, 10))
    # parelo.drawlines(mainApp().frame)
    for x in range(-2, 2):
        for y in range(-2, 2):
            for z in range(-2, 2):
                parelo = shapes3D.Cube(shapes3D.Coord3(x*100, y*100, z*100), 75)
                # parelo.drawlines(mainApp().frame)
                # parelo.draw(mainApp().frame)
                mainApp().scene.add(parelo)
                # mainApp().update()
                print('a')
    print(f"main: parallelepipedon:{time.time()-t:.4f}s")


if __name__ == '__main__':
    main()

    while True:
        mainApp().update()
