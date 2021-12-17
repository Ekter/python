from pynput import keyboard

last_key = [keyboard.Key.space]


def on_press(key, last_key=last_key):
    try:
        print("alphanumeric key {0} pressed".format(key.char))
        if key.char == "l" and last_key[0].char == "n":
            ct = keyboard.Controller()
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.type("newline")
            ct.press(keyboard.Key.enter)
            ct.release(keyboard.Key.enter)
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
