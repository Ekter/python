#/usr/bin/python3
from math import sqrt

r=int(input("Nombre max:"))
n=1
lprem=[]
p=1
while p<r:
    # print(p)
    o=2
    f=0
    while o<=int(sqrt(p)) and f==0:
        if p/o==int(p/o):
            f=1
            # print(f"pas premier: {p}/{o}")
        o+=1
    if f==0:
        lprem.append(p)
        n+=1
        print(p)
    p+=1

liste=[]
# with file as open("listepremiers.txt"):
#     liste.append(int(file.readline()))
# file=open("listepremiers.txt")
# file.readline()

# print(lprem,file="listepremiers.txt")
