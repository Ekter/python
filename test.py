''''Entrée
Ligne 1 : un entier N, le nombre de survivants ayant accès à la salle commune

N lignes suivantes : une chaîne de caractères au format "hh:mm - hh:mm" représentant la plage horaire de présence d'un survivant.

Sortie
Le nombre de paires de survivants présentant un risque de contamination mutuelle.

Exemple'''


entree= ['10','09:00 - 09:10','09:10 - 09:20','09:15 - 09:25','09:30 - 09:40','09:35 - 09:45','09:40 - 09:50','10:00 - 10:10','10:05 - 10:15','10:10 - 10:20','10:25 - 10:35']
def test():
    
    N = int(entree[0])
    liste = []
    for i in range(1,N+1):
        liste.append(entree[i])
    liste.sort()
    compteur = 0
    for i in range(len(liste)-1):
        for j in range(i+1,len(liste)):
            if liste[i][-5:] > liste[j][:5]:
                compteur += 1
    return compteur