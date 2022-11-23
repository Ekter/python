from time import sleep
from pynput.mouse import Controller

mouse = Controller()

# sleep(1)
# mouse.press(Button.right)
# sleep(100)
# mouse.release(Button.left)
for i in range(100):
    mouse.move(-10, 0)
    sleep(0.03)
