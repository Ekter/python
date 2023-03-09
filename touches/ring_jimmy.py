from pynput import keyboard
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second



def on_press(key):
    ct = keyboard.Controller()
    # C'EST TROP PUISSANT PUTAIN
    try:
        print(f"alphanumeric key {key.char} pressed")
        if key.char == "a":
            winsound.Beep(frequency, duration)

            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.press(keyboard.Key.backspace)
            ct.release(keyboard.Key.backspace)
            ct.type("newline")
            ct.press(keyboard.Key.enter)
            ct.release(keyboard.Key.enter)
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
