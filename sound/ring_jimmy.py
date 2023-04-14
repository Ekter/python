from pynput import keyboard

import pyaudio
import wave


def plauy(filename):
    chunk = 1024
    f = wave.open(filename, "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)
    while data:
        stream.write(data)
        data = f.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()


def on_press(key):
    try:
        print(f"alphanumeric key {key.char} pressed")
        if key.char == "b":
            plauy(r"sound.wav")
        if key.char == "k":
            plauy(r"kahoot.wav")

    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    print("{0} released".format(key))
    try:
        if key.char == "q":
            print("closed listner")
            return False
    except AttributeError:
        pass
    finally:
        return True


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
