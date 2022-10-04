from time import sleep
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener as KL, Key

mouse = Controller()
kc=KL()

def on_press(key):
    if key==Key.home:
        for i in range(100):
            mouse.click(Button.left, 1)
            sleep(0.01)
            print("a")
kc=KL(on_press=on_press)
with kc:
    kc.join()
