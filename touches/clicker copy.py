from time import sleep, time
from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Listener as KL, Key, Controller as KC
from queue import Queue

mouse = Controller()
keyboard = KC()
actions = []
id_ = [1]

q = Queue(1)

def add_to_actions(item):
    try:
        q.get_nowait()
        actions.append(item)
        q.put(1)
    except:
        print("not saving this!")

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Pressed at ({x}, {y}) with {button} at {time()}")
        add_to_actions((x, y, button, time()))
    else:
        print(f"Released at {x}, {y} with {button}")

def on_press(key):
    if key == Key.esc:
        print("exiting")
        return False
    if key not in [Key.home, Key.end]:
        add_to_actions((key, time()))
        print(f"typing {key} at {time()}")
    if key == Key.home:
        print("reset")
        actions.clear()
            # path = /home/ekter/Documents/codaj/python/autres/images/img71.png
    if key == Key.end:
        q.get()
        print("executing")
        print(actions)
        time_ = time()
        time_ref = actions[0][-1]
        for action in actions:
            if len(action) == 4:
                mouse.position = (action[0], action[1])
                mouse.click(action[2])
            else:
                if action[0] == Key.space:
                    keyboard.type(f"/home/ekter/Documents/codaj/python/autres/images/img{id_[0]}.png")
                elif action[0] == Key.caps_lock:    
                    keyboard.type(f"ground_maya_{id_[0]}.png")
                    id_[0] += 2
                else:
                    keyboard.tap(action[0])
                    print(action[0])
                sleep(0.1)
            while time() - time_ < action[-1] - time_ref:
                sleep(0.01)
        print("done")
        q.put(1)

for i in range(3):
    print(f"launching in {3-i}...")
    sleep(1)

listener = Listener(on_click=on_click)
kc = KL(on_press=on_press)
with listener:
    with kc:
        q.put(1)
        listener.join()
        kc.join()