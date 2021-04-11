from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
sleep(5)
for i in range(10):
    keyboard.type("Romain, je suis ton père")
    keyboard.press(Key.enter)
    sleep(0.1)
    keyboard.release(Key.enter)
    sleep(1)
