n=10
l=[i for i in range(n)]
print(l)
tot=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            tot+=1 if (i+j+k==n and i!=0 and j!=0 and k!=0) else 0


print(f"{n} : {tot}")