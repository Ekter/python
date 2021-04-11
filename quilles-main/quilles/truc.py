def afficheQuilles (q,n):
    fin = q[-1][-1] + 1
    nbListe=len(q)
    Quilles=""
    i=0

    if nbListe > 1 :
        while i  < nbListe :
            p=i+1

            if p!= nbListe :
                p=i+1
            elif p == nbListe :
                p= nbListe - 1

            debout = q[i][-1]+1 - q[i][0]
            tombe = q[p][0] - q[i][-1]-1

            for k in range (debout):
                Quilles = Quilles + "|"
            for k in range (tombe) :
                Quilles = Quilles + "."
            if q[i][0] > q[i][-1] :
                nbListe = nbListe - 1

            i = i+1

        for i in range (n-fin) :
            Quilles += "."

    else:
        if fin == n - 1 :
            for i in range (n ):
                Quilles += "|" 

        elif fin != n - 1 :
            for i in range (fin):
                Quilles += "|" 
            for i in range (n - fin) :
                Quilles += "."



    print("Voici les quilles, il y'a" , nbListe , "lignes")
    print( Quilles)
afficheQuilles([[3,4],[7,10]],15)