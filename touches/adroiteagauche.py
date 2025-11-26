from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
while True:
    # keyboard.release("d")
    sleep(2)
    keyboard.release("d")
    keyboard.press("a")
    sleep(2)
    keyboard.release("a")
    keyboard.press("d")

# while True:
#     keyboard.press(" ")
#     sleep(0.1)
#     keyboard.release(" ")


while True:
    keyboard.press("v")
    sleep(0.1)
    keyboard.release("v")

