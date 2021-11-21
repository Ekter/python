from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
while True:
    keyboard.press("d")
    sleep(0.5)
    keyboard.release("d")
    keyboard.press("a")
    sleep(0.5)
    keyboard.release("a")