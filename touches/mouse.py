from time import sleep, time
from pynput.mouse import Controller, Button

mouse = Controller()

# _time=time()
sleep(3)    
# mouse.press(Button.right)
# sleep(100)
# mouse.release(Button.left)
# while time()-_time<30:

for _ in range(500):
    mouse.move(0, 30)
    sleep(0.2)
    mouse.click(Button.left, 1)
    sleep(0.9)
    mouse.move(0,-30)
    sleep(0.2)
    mouse.click(Button.left, 1)
    sleep(0.9)
