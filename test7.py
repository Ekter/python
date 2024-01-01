lines = [5,
"12:00 - 12:30",
"15:30 - 16:00",
"17:30 - 19:00",
"15:30 - 18:30",
"17:00 - 18:00"]
import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def to_min(line):
    a, b = line.split(" - ")
    a1, a2 = a.split(":")
    b1, b2 = b.split(":")
    return [int(a1)*60+int(a2), int(b1)*60+int(b2)]

def to_minr(line):
    a, b = line.split(" - ")
    a1, a2 = a.split(":")
    b1, b2 = b.split(":")
    return range(int(a1)*60+int(a2), int(b1)*60+int(b2))


def tempsEnCommun(r1,r2):
    return min(r1[1],r2[1])-max(r1[0],r2[0])



i=0
for p1, p2 in findsubsets(lines[1:], 2):
    l1 = to_min(p1)
    l2 = to_min(p2)
    if tempsEnCommun(l1,l2)>=15:
        i+=1
        print(p1,p2)

print(i)
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import re


# lines = []
# for line in sys.stdin:
#     lines.append(line.rstrip('\n'))

lines = [
    "4",
    "ce",
    "tri",
    "bar",
    "banc",
    "t"
]


lines.sort()

def up_until_not(index_start,match):
    r=re.compile(match)
    i=index_start

    while index_start<len(lines) and re.match(r,lines[index_start]):
        index_start+=1
    return index_start


def is_winning(size_f, beg, end):
    if beg==end-1 or beg==end:
        return size_f-len(lines[beg]) % 2 ==0
    n = 0
    tot=0
    ind=beg

    while ind<end:
        tot+=1
        dec = up_until_not(ind, lines[ind][:size_f+1])
        if dec == ind:
            dec+=1
        if not(is_winning(size_f+1,ind,dec)):
            n+=1
        ind=dec
    return n==tot


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()

ind = 1
good = False

for l in alphabet:
    dec = up_until_not(ind, l)
    if dec>ind and is_winning(1,ind,dec):
        print(l)
        good = True
    ind=dec

if not good:
    print("impossible")

