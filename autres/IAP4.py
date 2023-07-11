import enum

class P4(object):
    class Player(enum.Enum):
        player1 = 1
        player2 = 2
    def __init__(self) -> None:
        self.grid: list[list[P4.Player]] = [[0 for _ in range(7)] for _ in range(6)]
        self._player: P4.Player = P4.Player.player1

    def __str__(self) -> str:
        tmp:str = "---------------"
        for k1 in self.grid:
            tmp+="\n|"+"|".join([str(k2) for k2 in k1])+"|"
        tmp+="\n---------------"
        return tmp

    def play(self,column: int) -> None:
        if self.grid[0][column]==0:
            k1:int = 0
            while k1<5 and self.grid[k1+1][column]==0:
                k1+=1
            self.grid[k1][column] = self._player
            self._player = P4.Player.player1 if self._player == P4.Player.player2 else P4.Player.player2
        else:
            raise TypeError("full colummn")

    def test_winner(self):
        




def testgagnelong(a):
    for x in range(6):
        for y in range(7):
            j=a[x][y]
            if True:#j
                longueur=0
                mongueur=0
                nongueur=0
                oongueur=0
                pongueur=0
                qongueur=0
                rongueur=0
                songueur=0
                print("il y a un pion",j,"en",x+1,y+1)
                if x>=3:
                    longueur=0
                    for k in range(x,x-3,-1):
                        if a[k][y]==j:
                            longueur+=1
                if x<=3:
                    mongueur=0
                    for k in range(x,x+3):
                        if a[k][y]==j:
                            mongueur+=1
                if y>=3:
                    nongueur=0
                    for k in range(y,y-3,-1):
                        if a[x][k]==j:
                            nongueur+=1
                if y<=2:
                    oongueur=0
                    for k in range(y,y+3):
                        if a[x][k]==j:
                            oongueur+=1
                if y<=2 and x>=3:
                    pongueur=0
                    for k in range(0,3):
                        if a[x-k][y+k]==j:
                            pongueur+=1
                if y>=3 and x>=3:
                    qongueur=0
                    for k in range(0,3):
                        if a[x-k][y-k]==j:
                            qongueur+=1
                if y>=2 and x<=3:
                    rongueur=0
                    for k in range(0,3):
                        if a[x+k][y-k]==j:
                            rongueur+=1
                if y<=2 and x<=3:
                    songueur=0
                    for k in range(0,3):
                        if a[x+k][y+k]==j:
                            songueur+=1
                if longueur==4 or mongueur==4 or nongueur==4 or oongueur==4 or pongueur==4 or qongueur==4 or rongueur==4 or songueur==4:
                    return "gagné",j
def testgagnerapide(a,x,y,j):
    if j:
        longueur=0
        mongueur=0
        nongueur=0
        oongueur=0
        pongueur=0
        qongueur=0
        rongueur=0
        songueur=0
        #print("il y a un pion",j,"en",(x+1,y+1))
        if x>=3:
            longueur=0
            for k in range(0,-3,-1):
                print(k)
                if a[x+k][y]==j:
                    longueur+=1
        if x<=3:
            mongueur=0
            for k in range(x,x+3):
                if a[k][y]==j:
                    mongueur+=1
        if y>=3:
            nongueur=0
            for k in range(y,y-3,-1):
                if a[x][k]==j:
                    nongueur+=1
        if y<=2:
            oongueur=0
            for k in range(y,y+3):
                if a[x][k]==j:
                    oongueur+=1
        if y<=2 and x>=3:
            pongueur=0
            for k in range(0,3):
                if a[x-k][y+k]==j:
                    pongueur+=1
        if y>=3 and x>=3:
            qongueur=0
            for k in range(0,3):
                if a[x-k][y-k]==j:
                    qongueur+=1
        if y>=2 and x<=3:
            rongueur=0
            for k in range(0,3):
                if a[x+k][y-k]==j:
                    rongueur+=1
        if y<=2 and x<=3:
            songueur=0
            for k in range(0,3):
                if a[x+k][y+k]==j:
                    songueur+=1
        if longueur==4 or mongueur==4 or nongueur==4 or oongueur==4 or pongueur==4 or qongueur==4 or rongueur==4 or songueur==4:
            return "gagné"
        else:
            return "pas gagné"
def play(a,colonne,j):
    if j and a[0][colonne]==0:
        k1=0
        while a[k1+1][colonne]==0 and k1<4:
            k1+=1
        if k1==4:
            if a[5][colonne]==0:
                k1+=1
        a[k1][colonne]=j
        return a,k1
    else:
        return "pas bon"
def printp4(a):
    print("---------------")
    for k1 in a:
        ligne="|"
        for k2 in k1:
            ligne=ligne+str(k2)+"|"
        print(ligne)
    print("---------------")
def testcoupssuivantgagne(a,j):
    listecoupsgagnants=[]
    for col in range(7):
        ilfsdjg=play(a,col,j)
        if not type(ilfsdjg) is str:
            a1,y=ilfsdjg
        if testgagnerapide(a1,col,y,j)=="gagné":
            listecoupsgagnants+=col
    return listecoupsgagnants
def joueurjoue(a,j)-> int:
    lcoups=[]
    for k in range(7):
        ilfsdjg=play(a,k,j)
        if not type(ilfsdjg) is str:
            a1,y=ilfsdjg
            if testgagnerapide(a1,k,y,j)=="gagné":
                lcoups.append((k,1))
            else:
                mldfigj=joueurjoue(a1,j)
                if not(type(mldfigj) is str):
                    lcoups.append(k,1-joueurjoue(a1,-j)[1])
    return lcoups[lcoups.index(max(lcoups[k][1] for k in lcoups))]




k=[[0 ,0 ,0 ,0 ,0 ,0 ,0 ],
   [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
   [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
   [0 ,0 ,0 ,1 ,0 ,0 ,0 ],
   [0 ,0 , 0,1 ,0 ,-1,0 ],
   [0 ,0 ,0 ,1 ,1 ,1 ,0 ]]





print("début")
for i in range(10):
    printp4(k)
    play(k,1,1)
#printp4(k)
#print(testgagnelong(k))
print(testgagnerapide(k,0,0,1))
#print(testcoupssuivantgagne(k,1))
print("fin")
#print(joueurjoue(k,1))