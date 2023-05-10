from pynput import mouse
# import time
import tkinter as tk


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    mainApp().frame.line_next(x, y)


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    mainApp().frame.dot_here(x, y)


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


class MyFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.listener = mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll)
        self.listener.start()
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=1)

    def line_next(self, x, y):
        self.canvas.create_line(self.x, self.y, x, y,width=10)
        self.x = x
        self.y = y

    def dot_here(self, x, y):
        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Lines")
        self.frame = None

    def begin(self):
        self.frame = MyFrame()
        self.root.mainloop()




def mainApp(frame: App = App()) -> App:
    return frame

mainApp().begin()

# def main():
#     # create tk window fullscreen
#     root = tk.Tk()
#     root.attributes('-fullscreen',True)

#     # ex = mainFrame()
#     # root.geometry("400x250+300+300")
#     root.mainloop()


# if __name__ == '__main__':
#     main()