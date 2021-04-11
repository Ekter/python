#!/usr/bin/python3
# coding: utf-8 
import random
import string
def random_string(n):
    strings=''
    random_list=list(string.ascii_letters)+list('''0123456789&é"'(-è_çà)=~#{[|^@]}œ1234567890°+/*-+.\n\t''')
    for loop in range(n):
        strings+=random.choice(random_list)
    return ''.join(strings)
while True:
    print(random_string(100))
