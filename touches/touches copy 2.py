from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
sleep(5)
def ecrireunmot(mot):
    for k in mot:
        keyboard.press(k)
        sleep(0.1)
        keyboard.release(k)
def miner():
    ecrireunmot(".equip pick")
    keyboard.press(Key.enter)
    sleep(0.2)
    keyboard.release(Key.enter)
    sleep(0.5)
    ecrireunmot(".mine")
    keyboard.press(Key.enter)
    sleep(0.2)
    keyboard.release(Key.enter)
    sleep(0.5)
def pecher():
    ecrireunmot(".equip rod")
    keyboard.press(Key.enter)
    sleep(0.2)
    keyboard.release(Key.enter)
    sleep(0.5)
    ecrireunmot(".fish")
    keyboard.press(Key.enter)
    sleep(0.2)
    keyboard.release(Key.enter)
    sleep(0.5)
def couper():
    ecrireunmot(".equip axe")
    keyboard.press(Key.enter)
    sleep(0.2)
    keyboard.release(Key.enter)
    sleep(0.5)
    ecrireunmot(".chop")
    keyboard.press(Key.enter)
    sleep(0.2)
    keyboard.release(Key.enter)
    sleep(0.5)
def fouiller():
    ecrireunmot(".loot")
    keyboard.press(Key.enter)
    sleep(0.2)
    keyboard.release(Key.enter)
miner()
miner()
fouiller()
fouiller()
pecher()
pecher()
couper()
couper()
