from multiprocessing import Process
from time import sleep
rocket = [0]
alphabet = "abcdefghijklmnopqrstuvwxyz"


def fnum():
    print('start fnum')
    l=0
    while l<200:
        filr = open("input.txt", "r")
        l=len(filr.readlines())
        fila = open("input.txt", "a")
        fila.write(f"1:{l} -> {l}\n")
        # sleep(0.01)
        fila.close()
    print('end fnum')


def fchar():
    print('start fchar')
    l=0
    while l< 200:
        filr = open("input.txt", "r")
        l=len(filr.readlines())
        fil2 = open("input.txt", "a")
        fil2.write(f"2:{l} -> {alphabet[l%26]}\n")
        # sleep(0.01)
        fil2.close()
    print('end fchar')


def fbool():
    print('start fbool')
    l=0
    while l < 200:
        filr = open("input.txt", "r")
        l=len(filr.readlines())
        fil3 = open("input.txt", "a")
        fil3.write(f"3:{l} -> {bool(l%2)}\n")
        # sleep(0.01)
        fil3.close()
    print('end fbool')


if __name__ == '__main__':
    print("debut")
    file=open("input.txt", "w")
    file.close()
    p1 = Process(target=fnum)
    sleep(0.02)
    p1.start()
    p2 = Process(target=fbool)
    sleep(0.02)
    p2.start()
    sleep(0.02)
    print("debut?")
    fchar()
    print("fin?")
