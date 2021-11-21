#programme écrit par Nino Mulac qui rajoute un entier à sa place dans une liste.
#la fonction en question
def insert(listeAAgrandir,entierAMettreDedans):
    listeAAgrandir.append(entierAMettreDedans)
    listeAAgrandir.sort()
    return listeAAgrandir
print(insert([1,2,5],3))