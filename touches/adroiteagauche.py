from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
# while True:
#     # keyboard.release("d")
#     sleep(2)
#     keyboard.release("d")
#     keyboard.press("q")
#     sleep(2)
#     keyboard.release("q")
#     keyboard.press("d")

# while True:
#     keyboard.press(" ")
#     sleep(0.1)
#     keyboard.release(" ")


while True:
    keyboard.press("d")
    sleep(5)
    keyboard.release("d")
 
