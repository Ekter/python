a=1
l=[1]
for i in range(1,100000):
    l.append(l[-1]*i)
print(l)
