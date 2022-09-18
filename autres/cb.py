from urllib.request import urlopen
import pyperclip
from time import sleep
from pynput import keyboard
from urllib.parse import quote_plus

with urlopen("http://fileszfhjsdbn.alwaysdata.net/cb.php") as response:
    # print(response)
    print(response.read().decode("utf-8"))
    # pyperclip.copy(response.read().decode("utf-8"))
# sleep(1)
# s = pyperclip.paste()
# pyperclip.copy(s)
# print(type(s))
# print(s)


last_key = [keyboard.Key.space]

def on_press(key, last_key=last_key):
    ct = keyboard.Controller()
    try:
        print(f"alphanumeric key {key} pressed")
        if key == keyboard.Key.ctrl_l and last_key[0] == keyboard.Key.ctrl_r:
            with urlopen("http://fileszfhjsdbn.alwaysdata.net/cb.php") as response:
                rep=response.read().decode("utf-8").strip()
                print("#"+rep+"#")
                pyperclip.copy(rep)
                print("receive")
                # ct.type(response.read().decode("utf-8").strip())
        if key == keyboard.Key.ctrl_r and last_key[0] == keyboard.Key.ctrl_l:
            s = pyperclip.paste()
            with urlopen("http://fileszfhjsdbn.alwaysdata.net/cb.php?cb="+quote_plus(s)) as response:
                print("##"+response.read().decode("utf-8").strip()+"##")
                print("send")
                # ct.type("OK!")
                # sleep(10)
                # for _ in range(2):
                #     ct.tap(keyboard.Key.backspace)
        last_key[0] = key
    except Exception as e:
        print(e)


def on_release(key):
    print("{0} released".format(key))
    if key == keyboard.Key.end:
        # Stop listener
        print("closed listener")
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()