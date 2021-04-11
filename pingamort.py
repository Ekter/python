from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
sleep(5)
for i in range(1):
    for i in range(7):
        keyboard.type("""from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
sleep(5)
for i in range(2):     #nombre de séries
    for i in range(5): #nombre de répétitions: pour envoyer des petits messages sur discord il vaut mieux le faire par séries qu'en continu
        keyboard.type("là tu vois tu mets ce que tu veux et ça l'envoie")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
    sleep(5)


sleep(1)""")
        keyboard.press(Key.enter)
        sleep(0.1)
        keyboard.release(Key.enter)
    sleep(5)


sleep(1)