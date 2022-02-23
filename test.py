"""
blablabla"""


from random import randint
import math
import time
t=time.time()
s=0
n=1
while s<20:
    s+=1/n
    n+=1
    if n%1==0:   #43.177613973617554  #32.93029999732971   #91.33971166610718   #29.316272735595703
        print(s)
print(n)
print(math.log(n))
print(time.time()-t)
input()

print(math.gcd(5,4))
def circular(l2):
    print(l2)
    x=str(l2)
    return ', [...]' in x

def caca() -> int:
    "cette fonction ne sert à rien"
    print()

"""
class Client(object):
    "Cette classe représente un client"
    def __init__(self,age,genre,ageMin=-1,ageMax=-1,genreAim=["F","M","?"]):
        self.age=age
        self.genre=genre
        if ageMin!=-1:
            self.ageMin=ageMin
        else:
            self.ageMin=age-5
        if ageMax!=-1:
            self.ageMax=ageMax
        else:
            self.ageMax=age+5
        self.genreAim=genreAim
    def ageCorrespond(self,client2) -> bool:
        client1=self
        return (client1.age<=client2.ageMax and client1.age>=client2.ageMin) and (client2.age<=client1.ageMax and client2.age>=client1.ageMin)
    def genreCorrespond(self,client2) -> bool:
        client1=self
        return (client2.genre in client1.genreAim) and (client1.genre in client2.genreAim)
    def correspond(self,client2) -> bool:
        client1=self
        return client1.ageCorrespond(client2) and client1.genreCorrespond(client2) and not client1 is client2
    def toString(self) -> str:
        return "<Client, {} ans [{}-{}], {} {}>".format(self.age,self.ageMin,self.ageMax,self.genre,self.genreAim)
    def print(self) -> None:
        print(self.toString())
    def __repr__(self):
        return self.toString()

class Listing(object):
    "Cette classe, par contre, est un listing."
    def __init__(self,listeClients:list,yes={},no={}):
        self.listeClients=listeClients
        self.yes=yes
        self.no=no
    def numberCorrespond(self,c) ->int:
        n=0
        for i in [k for k in self.listeClients if not k is c]:
            if c.correspond(i):
                n+=1
        return n

    def next(self,c):
        for i in [k for k in self.listeClients if not k is c]:
            if c.correspond(i) and not(c in self.yes.get(i) or c in self.no.get(i)):
                return i
    def swipe(self,c,d,s):
        if s:
            self.yes[c].append(d)
        else:
            self.no[c].append(d)
c = Client(40, 'M')
d = Client(42, '?')
e = Client(47, 'F', genreAim = ['M'])
c = Client(30, 'F', ageMin = 28, genreAim = ['F'])
print(c.toString())
c.print()
print(c)
print(c.ageCorrespond(d))
print(d.ageCorrespond(e))
print(e.ageCorrespond(c))
print(c.genreCorrespond(d))
print(d.genreCorrespond(e))
print(e.genreCorrespond(c))
print(c.correspond(d))
print(d.correspond(e))
print(e.correspond(c))
c = Client(20, 'M', genreAim = ['F'])
d = Client(30, '?', 18, 80)
e = Client(27, 'F', genreAim = ['F'])
l = Listing([c, d, e, Client(25, 'F'), Client(22, 'M'), Client(27, '?'), Client(30, 'F'), Client(27, 'F', genreAim = ['F'])])
print(l.numberCorrespond(c))
c = Client(20, 'M', genreAim = ['F'])
d = Client(30, '?', 18, 80)
e = Client(27, 'F', genreAim = ['F'])
l = Listing([c, d, e, Client(25, 'F'), Client(22, 'M'), Client(27, '?'), Client(30, 'F'), Client(27, 'F', genreAim = ['F'])])
print(l.numberCorrespond(d))
print(l.numberCorrespond(e))
c = Client(20, 'M', genreAim = ['F'])
d = Client(29, '?', 18, 80)
e = Client(24, 'F', genreAim = ['F', '?'])
l = Listing([c, d, e])
print(l.next(c))
print(l.next(d))
print(l.next(e))
c = Client(20, 'M')
d = Client(21, 'F')
e = Client(22, '?')
f = Client(23, 'M')
l = Listing([c, d, e, f])
l.swipe(c, d ,True)
l.swipe(c, f, True)
l.swipe(d, c, False)
l.swipe(d, e, False)
print(l.yes)
print(l.no)
c = Client(20, 'M')
d = Client(21, 'F')
e = Client(22, '?')
f = Client(23, 'M')
l = Listing([c, d, e, f])
print(l.next(d))
l.swipe(d, c, False)
print(l.next(d))
l.swipe(e, d, True)
print(l.next(d))
l.swipe(d, e, True)
print(l.next(d))
l.swipe(f, d, False)
print(l.next(d))

input()"""
l=[2]
l.append(l)
l.pop(0)
print(l,circular(l))
l=[1]
l.append((l for i in range(37)))
print(l,circular(l))
print()
i,j=0,0
while True :
    if i >=2:
        break
    while j <2:
        j+=1
        print ( i * j )
        print ( j )
    j=0
    i+=2
l=[1,3,2]
l.sort()
print(l,l[::],max(l))
a=1
a+=1+2
if randint(0,2)==0:
    def fonctiontest(first_var=0):
        """:param first_var:"""
        print(first_var)
elif randint(0,1)==0:
    def fonctiontest(first_var=0,second_var=0):
        """:param first_var:
        :param second_var:"""
        print(first_var,second_var)
else:
    def fonctiontest(first_var=0,second_var=0,third_var=0):
        """:param first_var:
        :param second_var:
        :param third_var:"""
        print(first_var,second_var,third_var)
fonctiontest(*[randint(0,10) for i in range(randint(0,3))])
class Point():
    "Ceci est un point."
    def __init__(self,abscisse,ordonnee):
        self.abs=abscisse
        self.ord=ordonnee

    def affiche_point(self):
        """
        Affiche un point"""
        print("coord. horizontale =", self.abs, "coord. verticale =", self.ord)

    def __repr__(self):
        return "Point({},{})".format(self.abs,self.ord)


p9=Point()
p9.abs=3
p9.ord=4
class Time(object):
    "classe de temps"
    def __init__(self,heure=12,minute=0,seconde=0):
        self.heure =heure
        self.minute =minute
        self.seconde =seconde
instant=Time(11,34,25)
#instant.heure=11
#instant.minute=34
#instant.seconde=25

def affich_heure(t):
    print(str(t.heure)+":"+str(t.minute)+":"+str(t.seconde))
affich_heure(instant)
class Domino(object):
    "Cette classe est un domino en fait vous saviez pas?"
    def __init__(self,num1,num2) -> None:
        self.faceA=num1
        self.faceB=num2
    def affiche_points(self) -> None:
        print("face A:{}; face B:{}".format(self.faceA,self.faceB))
    def valeur(self) -> int:
        return self.faceA+self.faceB
def puissance(x,n):
    if n==0 :
        return 1
    return x*puissance(x,n-1)

print(puissance(3,2))
def compteLettre(c,s):
    if s=="":
        return 0
    a=compteLettre(c,s[:-1])
    return a+1 if c==s[-1] else a
print(compteLettre("a","ahgajjajgagajjjgaa"))
def maximum(l):
    if len(l)==1:
        return l[0]
    a=maximum(l[:-1])
    return l[-1] if a<=l[-1] else a
print(maximum([1,2,3,4,10,2,8]))
def palindrome(m):
    if len(m)<=1:
        return True
    a=palindrome(m[1:-1])
    return a and m[0]==m[-1]
print(palindrome("mflerkfkrelfm"))
def racine(n,x):
    if n==0:
        return 1
    a=racine(n-1,x)
    return ((x/a)+a)/2
print(racine(100,2))
def fibonacci(n):
    if n==1:
        return 1
    if n==0:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(11))
def tableFibonacci(n):
    if n==0:
        return [1]
    if n==1:
        return [1,1]
    l=tableFibonacci(n-1)
    l.append(l[-2]+l[-1])
    return l
print(tableFibonacci(100))
def deuxFibonacci(n):
    if n==1:
        return (1,1)
    a,b=deuxFibonacci(n-1)
    return b,a+b
print(deuxFibonacci(10))
def deuxFibonacci(n,f0=1,f1=1):
    if n==0:
        return (f1-f0,f0)
    a,b=deuxFibonacci(n-1)
    return b,a+b
def f(n,f0=1,f1=1):
    return deuxFibonacci(n,f0,f1)[1]
def hanoi(n,t1,t2,t3):
    if n==0:
        return ""
    if n==1:
        print("Déplace le disque supérieur de "+t1+" sur "+t3)
        return ""
    hanoi(n-1,t1,t3,t2)
    hanoi(1,t1,t2,t3)
    hanoi(n-1,t2,t1,t3)
hanoi(5,"A","B","C")
def permutations(l1):
    if l1==[]:
        return [[]]
    ltemp=permutations(l1[:-1])
    lt2=[]
    for k in ltemp:
        for i in range(len(k)+1):
            j=k[:]
            j.insert(i,l1[-1])
            lt2.append(j)
    return lt2
def hanoiv2(n,t1,t2,t3):
    if n==0:
        return [3,2,1],[],[]
    l1,l3,l2=hanoiv2(n-1,t1,t3,t2)
    l3.append(l1[-1])
    l1.pop(-1)
    print(l1, l2, l3, '##############', sep='\n')
    hanoiv2(n-1,t2,t1,t3)
    return l1,l2,l3
hanoiv2(3,[3,2,1],[],[])
def afficherParties(n,joueur=True,nbpos=[1,2,3]):
    dicjoueur={True:"Blanc",False:"Noir"}
    if n<=0:
        if n==0:
            print(dicjoueur.get(not(joueur))+" a gagné")
        return
    for i in nbpos:
        if n>=i:
            print("Il reste",n,"allumettes")
            print(dicjoueur.get(joueur),"prend",i,"allumettes")
            afficherParties(n-i,not(joueur))
afficherParties(3)
def couleurcourt(n,joueur,k):
    return joueur if n%(k+1)!=0 else not(joueur)
def couleur(n,j,k):
    if n!=0:
        for i in range(1,k+1):
            if n-i>=0:
                color= couleur(n-i,not j,k)
                if color == j:
                    return j
                return not(j)
    return not j
for j in range(1,10):
    print("---------------------",j,"---------------------")
    for i in range(100):
        a=couleurcourt(i,True,j)
        b=couleur(i,True,j)
        if a!=b:
            print(i,a,b)
