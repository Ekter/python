from random import randint
essais=0
nombre=randint(0,100)
n=-1
while essais<=6 and n!=nombre:
    n=int(input("Nombre entre 0 et 100:"))
    if n==nombre:
        print("Bravo! n="+str(n))
    if n<nombre:
        print("Essaye encore! n>"+str(n))
    if n>nombre:
        print("Essaye encore! n<"+str(n))
    essais+=1
    print("Il te reste",6-essais,"essais"+"."*essais)