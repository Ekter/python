from pynput import keyboard
import random
import time

last_key = [keyboard.Key.space]


def on_press(key, last_key=last_key):
    ct = keyboard.Controller()
    # ct.press(keyboard.Key.f18)
    # time.sleep(0.1)
    # ct.release(keyboard.Key.f18)
    # time.sleep(0.1)
    # C'EST TROP PUISSANT PUTAIN
    try:
        print(f"alphanumeric key {key.char} pressed")
        if key.char == "l" and last_key[0].char == "n":
            print("newline")
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.type("newline")
            ct.press(keyboard.Key.enter)
            ct.release(keyboard.Key.enter)
        if key.char == "y" and last_key[0].char == "i":
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.type("infinity")
        """if key.char == "u" and last_key[0].char == "f":
            ct.press(keyboard.Key.shift)
            for _ in range(74):
                ct.press(keyboard.Key.alt)
                ct.press(keyboard.Key.tab)
                ct.press(keyboard.Key.delete)
                ct.release(keyboard.Key.alt)
                ct.release(keyboard.Key.ctrl_l)
                ct.release(keyboard.Key.delete)
                ct.press(keyboard.Key.esc)
                ct.release(keyboard.Key.esc)
            ct.release(keyboard.Key.shift)
            ct.release("\"")
            ct.type("le")
            ct.press("\"")
            ct.release("\"")"""
        if key.char=="s" and last_key[0].char=="c":
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.type("stack{CS # -> # n->+infinity}")
        if key.char=="n" and last_key[0].char=="f":
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.type("evaluate {f_n} from{t->t^n} to{setR ->setR}")

        last_key[0] = key
    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    print("{0} released".format(key))
    if key == keyboard.Key.end:
        # Stop listener
        print("closed listner")
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
