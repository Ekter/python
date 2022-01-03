import random

def id(n:int=24):
    s="61cd"
    while len(s)<n:
        s+=str(random.choice("0 1 2 3 4 5 6 7 8 9 a b c d e f".split(" ")))
    return s


print(id())