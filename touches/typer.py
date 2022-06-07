"""a module to type things."""

from dotenv import get_key
from pynput import keyboard
from time import time, sleep
# from typing import List, Tuple
from multiprocessing import Process, freeze_support


class Typer():
    """a class to type things. a class just because otherwise i need globals."""
    list_imputs = [(keyboard.Key.enter, "c", time())]
    listening = False
    # prosseses = []
    actions = []
    ct = keyboard.Controller()

    def __init__(self):
        for key, method in self:
            method(key)

    def on_press(self, key):
        print(key)
        if key == keyboard.Key.end:
            if self.listening:
                print("stop")
                self.listening = False
            else:
                # p1=Process(target=make_action)
                # self.prosseses.append(Process(target=self.make_action))
                # self.prosseses[-1].start()
                t = time()
                self.actions.extend([(i[0], i[1], t+i[2])
                                    for i in self.list_imputs])
                print("a")
        if self.listening:
            self.list_imputs.append((key, "p", time()-self.begintime))
        print(self.list_imputs)
        for key, method in self:
            method(key)

    def on_release(self, key):
        if self.listening:
            self.list_imputs.append((key, "r", time()-self.begintime))
        if key == keyboard.Key.home:
            print("start")
            self.list_imputs = []
            self.listening = True
            self.begintime = time()
        for key, method in self:
            method(key)

    # def make_action(self, n=1):
    #     print("b", self.list_imputs)
    #     for i in range(n):
    #         for i in range(len(self.list_imputs)-1):
    #             if self.list_imputs[i][1] == "p":
    #                 self.ct.press(self.list_imputs[i][0])
    #             elif self.list_imputs[i][1] == "r":
    #                 self.ct.release(self.list_imputs[i][0])
    #             elif self.list_imputs[i][1] == "c":
    #                 self.ct.press(self.list_imputs[i][0])
    #                 self.ct.release(self.list_imputs[i][0])
    #             else:
    #                 print("error")
    #             sleep(self.list_imputs[i+1][2]-self.list_imputs[i][2])

    def __iter__(self):
        print("a")
        while len(self.actions)>0:
            for i in self.actions:
                if i[2] < time():
                    yield (i[0], self.ct.press if i[1] == "p" else self.ct.release)
                    self.actions.remove(i)
            sleep(0.01)


if __name__ == '__main__':
    # freeze_support()
    typer = Typer()
    with keyboard.Listener(on_press=typer.on_press, on_release=typer.on_release) as listener:
        listener.join()
