from pynput import keyboard
import sys
import os
import threading
import time
# from PySide6.QtWidgets import QApplication

# import viewer

print("Launching listener", end="", flush=True)

# print(" in 3s.")
# for i in range(3,0,-1):
#     print(f"{i} seconds remaining...")
#     time.sleep(1)

print("")



ct = keyboard.Controller()
states = {}
last_pause: list[int] = [time.time()]

def on_press(key) -> None:
    """
    Function to handle key press events.
    
    Args:
        key: The key that was pressed.
    """
    states[str(key).replace("'","")] = True
    print(str(key))
    if str(key)=="Key.media_play_pause":
        print("pause")
        if time.time()-last_pause[0]<4:
            print(time.time()-last_pause[0]>4)

        last_pause[0] = time.time()
        print("restarting spotify")
        def helper():
            os.system("pkill spotify; sleep 1; spotify > /dev/null &")
        threading.Thread(target=helper).start()
        time.sleep(1.5)
        time.sleep(0.1)
        ct.press(keyboard.Key.alt)
        time.sleep(0.1)
        ct.tap(keyboard.Key.tab)
        time.sleep(0.1)
        ct.release(keyboard.Key.alt)
        time.sleep(3)
        ct.tap(keyboard.Key.media_play_pause)

    if str(key)=="Key.space":
        print(states)
        if states.get("2"):
            open_window("é")
            ct.tap(keyboard.Key.backspace)
            ct.tap(keyboard.Key.backspace)
            ct.type("é")
        if states.get("7"):
            ct.tap(keyboard.Key.backspace)
            ct.tap(keyboard.Key.backspace)
            ct.type("è")
        if states.get("0"):
            ct.tap(keyboard.Key.backspace)
            ct.tap(keyboard.Key.backspace)
            ct.type("à")
        if states.get("9"):
            ct.tap(keyboard.Key.backspace)
            ct.tap(keyboard.Key.backspace)
            ct.type("ç")
        if states.get("'"):
            ct.tap(keyboard.Key.backspace)
            ct.tap(keyboard.Key.backspace)
            ct.type("ù")
        if states.get("e") and states.get("["):
            ct.tap(keyboard.Key.backspace)
            ct.tap(keyboard.Key.backspace)
            ct.tap(keyboard.Key.backspace)
            ct.type("ê")
        if states.get(str(keyboard.Key.home)):
            ct.tap(keyboard.Key.media_previous)
        if states.get(str(keyboard.Key.end)):
            ct.tap(keyboard.Key.media_next)
        if states.get(str(keyboard.Key.delete)):
            ct.tap(keyboard.Key.media_play_pause)




def on_release(key) -> None:
    """
    Function to handle key release events.
    
    Args:
        key: The key that was released.
    """
    states[str(key).replace("'","")] = False


def open_window(char: str):
    return
    app = QApplication(sys.argv)

    window = viewer.IMainWindow()
    window.show()

    print("launching")
    app.exec()



# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
