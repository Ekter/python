from time import sleep
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener as KL, Key

mouse = Controller()
sleep(5)


def on_press(key):
    if key == Key.home:
        for i in range(1):
            mouse.click(Button.right, 1000)
            # sleep(0.0001)
            print("a")


kc = KL(on_press=on_press)
with kc:
    kc.join()
