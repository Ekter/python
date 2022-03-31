from time import sleep
from pynput.mouse import Button, Controller

mouse = Controller()

sleep(1)
mouse.press(Button.right)
sleep(100)
mouse.release(Button.left)
