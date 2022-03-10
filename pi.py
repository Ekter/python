n=1
s=0
while n<100000000:
    s+=1/n**2
    n+=1
print(s)
print((s*6)**0.5)