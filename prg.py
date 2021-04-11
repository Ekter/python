#!/usr/bin/python3
from random import randint
def complexe():
	return str(randint(-10,10))+"+"+str(randint(-10,10))+"i"
for i in range(0,10):
    print(complexe())
