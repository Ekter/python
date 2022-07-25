from ntpath import join
from pynput import mouse

dim_screen=(2560*2,1440)
MAP=[["∎" for i in range(100)] for j in range(50)]
dim_map=(len(MAP[0]),len(MAP))
is_pressed=False

def switch(x,y):
    if MAP[y][x]=="∎":
        MAP[y][x]=" "
    else:
        MAP[y][x]="∎"

def on_move(x, y):
    # print(f"Pointer moved to ({x},{y})")
    if is_pressed:
        switch(int(x/dim_screen[0]*dim_map[0]),int(y/dim_screen[1]*dim_map[1]))


def on_click(x, y, button, pressed):
    # print(f"{button} {'Pressed' if pressed else 'Released'} at {(x,y)}")
    if pressed:
        switch(int(x/dim_screen[0]*dim_map[0]),int(y/dim_screen[1]*dim_map[1]))
    print("\n".join(["".join(i) for i in MAP])+"\n")
    global is_pressed
    is_pressed=pressed
    # if not pressed:
        # Stop listener
        # return False

def on_scroll(x, y, dx, dy):
    # print('Scrolled {0} at {1},other:{2}'.format(
    #     'down' if dy < 0 else 'up',
    #     (x, y),(dx, dy)))

    pass

# Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
while MAP!=[[" " for i in range(10)] for j in range(10)]:
    pass