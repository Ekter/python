from pynput.keyboard import Key, Controller
from time import sleep
from random import randint
keyboard = Controller()
sleep(5)
def ecrireunmotaleatoire(lon):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in range(lon):
        keyboard.press(alphabet[randint(0,25)])
    keyboard.press(Key.enter)
    sleep(0.2)
    keyboard.release(Key.enter)
    sleep(0.5)
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

tcoup=0
tpech=0
tmine=0
tfoui=0
tparl=0
dcoup=15
dpech=26
dmine=9

while True:
    sleep(1)
    tcoup-=1
    tpech-=1
    tmine-=1
    tfoui-=1
    tparl-=1
    if tcoup<0:
        couper()
        tcoup=4*60+15
        dcoup-=8
    if tpech<0:
        pecher()
        tpech=4*60+15
        dpech-=8
    if tmine<0:
        miner()
        tmine=5*60+17
        dmine-=8
    if tfoui<0:
        fouiller()
        tfoui=5*60+2
    if tparl<0:
        ecrireunmotaleatoire(randint(2,10))
        tparl=40
    if dmine<0:
        ecrireunmot(".unequip pick")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        ecrireunmot("yes")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        ecrireunmot(".market buy pick")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        dmine=40
    if dpech<0:
        ecrireunmot(".unequip rod")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        ecrireunmot("yes")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        ecrireunmot(".market buy rod")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        dpech=40
    if dcoup<0:
        ecrireunmot(".unequip axe")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        ecrireunmot("yes")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        ecrireunmot(".market buy axe")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
        dcoup=40
