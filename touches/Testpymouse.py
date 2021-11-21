#/usr/bin/python
from pymouse import PyMouse
import random
import time
m=PyMouse()
q=(0,0)
for i in range(300):
    position=m.position()
    m.move(position[0]+random.randint(-5,5),position[1]+random.randint(-5,5))
    print(m.position())
    time.sleep(0.03)
