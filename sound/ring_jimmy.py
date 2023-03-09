from pynput import keyboard
import winsound

import pyaudio
import wave
frequency = 880  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


def on_press(key):

    # C'EST TROP PUISSANT PUTAIN
    try:
        print(f"alphanumeric key {key.char} pressed")
        if key.char == "a":
            # winsound.Beep(frequency, duration)
            # define stream chunk
            chunk = 1024

            # open a wav format music
            f = wave.open(r"sound.wav", "rb")
            # instantiate PyAudio
            p = pyaudio.PyAudio()
            # open stream
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)
            # read data
            data = f.readframes(chunk)

            # play stream
            while data:
                stream.write(data)
                data = f.readframes(chunk)

            # stop stream
            stream.stop_stream()
            stream.close()

            # close PyAudio
            p.terminate()

    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    print("{0} released".format(key))
    if key.char == "q":
        # Stop listener
        print("closed listner")
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
