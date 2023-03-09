from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
# while True:
#     keyboard.press(" ")
#     sleep(0.1)
#     keyboard.release(" ")
sleep(3)
keyboard.press("d")
sleep(300)
keyboard.release("d")
