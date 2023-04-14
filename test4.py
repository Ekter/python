from threading import Thread
import time

string = "La commu Rust ne cesse de m'impressionner"

def print_async(l=[0,""]):
    print(string[l[0]],end = "\n")
    l[1] += string[l[0]]
    l[0] += 1
    # print(l[1])



t = Thread(target=print_async)
for i in range(len(string)):
    t = Thread(target=print_async)
    t.start()

a="""L
a
 
 
c
o
m
u
u
 
R
u
s
t
u
n
n
 
e
c
 
e
e
e
 
 
s
s
 
m
m
e
d
e
'
i
m

r
e
p
r""".split('\n')
time.sleep(1)
print(''.join(a))


