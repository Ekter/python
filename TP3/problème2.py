def chgmtbase(nb10,barr=2):
    alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i=0
    while barr**i<nb10:
        i+=1
    n2=""
    print(i)
    while i>0:
        i-=1
        k=nb10//(barr**i)
        nb10=nb10%(barr**i)
        n2=n2+alphabet[k]
    return n2
print(chgmtbase(232,2))