from pynput import keyboard
import random

last_key = [keyboard.Key.space]


def on_press(key, last_key=last_key):
    ct = keyboard.Controller()
    # ct.release(key)
    # C'EST TROP PUISSANT PUTAIN
    try:
        print("alphanumeric key {0} pressed".format(key.char))
        if key.char == "l" and last_key[0].char == "n":
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
        if key.char == "u" and last_key[0].char == "f":
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
            ct.release("\"")
        last_key[0] = key
    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    print("{0} released".format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
