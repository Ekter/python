#programme codé par Nino Mulac qui crypte par alphabet désordoné.

#fonction qui génère la table en fonction de la clé
def table(cle):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    table=""
    for n in range(len(cle)):
        cbon1=0
        for pointeur in alphabet:
            if cle[n]==pointeur:
                cbon1+=1
        cbon=0
        for pointeur in table:
            if cle[n]==pointeur:
                cbon+=1
        if not(cbon) and cbon1:
            table+=cle[n]
            alphabet=alphabet.replace(cle[n],"")
    return table+alphabet
#fin

#fonction qui génère le dictionnaire associé à la table
def dico(table):
    dictionnaire={"a":table[0],"b":table[1],"c":table[2],"d":table[3],"e":table[4],"f":table[5],"g":table[6],"h":table[7],"i":table[8],"j":table[9],"k":table[10],"l":table[11],"m":table[12],"n":table[13],"o":table[14],"p":table[15],"q":table[16],"r":table[17],"s":table[18],"t":table[19],"u":table[20],"v":table[21],"w":table[22],"x":table[23],"y":table[24],"z":table[25],".":".",",":",",":":":","!":"!","'":"'","-":"-"," ":" ",">":">","<":"<","(":"(",")":")","=":"=","+":"+"}
    return dictionnaire
#fin

#fonction qui renvoie la phrase codée
def desordone(cle,mot):
    code=dico(table(cle))
    mot=mot.lower()
    nouveaumot=""
    for i in mot:
        nouveaumot+=code.get(i)
    return nouveaumot
#fin

print(desordone("j'aime les cerises qui piquent le nez","Plik est grand, de plus, il est divin! De meme son existence est infinie et intemporelle, donc lim(x->plik)=FI puisque la perfection n'est pas atteignable pour nous autres pauvres humains"))
