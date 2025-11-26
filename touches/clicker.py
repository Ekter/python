from time import sleep
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener as KL, Key


mouse = Controller()
sleep(5)
print("launched")


def on_press(key):
    print(mouse.position)
    if key == Key.home:
        from gi.repository import Gdk

        window = Gdk.get_default_root_window()
        x, y, width, height = window.get_geometry()

        print("The size of the root window is {} x {}".format(width, height))

        # get_from_drawable() was deprecated. See:
        # https://developer.gnome.org/gtk3/stable/ch24s02.html#id-1.6.3.4.7
        pb = Gdk.pixbuf_get_from_window(window, x, y, width, height)

        if pb:
            pb.savev("screenshot.png", "png", (), ())
            print("Screenshot saved to screenshot.png.")
        else:
            print("Unable to get the screenshot.")
        # for i in range(30):
        #     for j in range(30):
        #         mouse.position = (37.4*i+969, 37.4*j+241)
        #         # mouse.click(Button.left, 1)
        #         mouse.release(Button.left)
        #         # sleep(1/900)
        #         print("a")



kc = KL(on_press=on_press)
with kc:
    kc.join()
