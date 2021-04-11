def eratosthene_slice(n):
    crible=[False,False]+[True]*(n-1)
    for d in range(int(n**0.5)+1):
        if crible[d]:
            crible[d*d::d]=[False]*(n//d -d+1)
    return crible

c=eratosthene_slice(500000)
for i in range(len(c)):
    if c[i]:
        print(i, end= ' ')
print()
