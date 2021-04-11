#def de la fonction "affine" non modifiée
def affine(a,b,x):
    return a*x+b
#fin

temp=int(input("température: "))
unite=input("unité: ")
if unite=="F":
    print(affine(1/1.8,-32/1.8,temp))
if unite=="C":
    print(affine(1.8,32,temp))
