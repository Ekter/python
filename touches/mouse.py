from time import sleep, time
from pynput.mouse import Controller

mouse = Controller()

_time=time()
# sleep(1)
# mouse.press(Button.right)
# sleep(100)
# mouse.release(Button.left)
while time()-_time<60*60:
    mouse.move(-10, 0)
    sleep(0.3)
    mouse.move(10, 0)
    sleep(0.3)
