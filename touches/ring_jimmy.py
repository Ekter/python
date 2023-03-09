from pynput import keyboard
# import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
amen = True


def on_press(key):
    # C'EST TROP PUISSANT PUTAIN
    try:
        print(f"alphanumeric key {key.char} pressed")
        if key.char == "a":
            # winsound.Beep(frequency, duration)
            print("a")

    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    print("{0} released".format(key))
    try:
        if key.char == "q":
            # Stop listener
            print("closed listner")
            return False
    except AttributeError:
        pass



# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
