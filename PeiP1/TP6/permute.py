#programme créé par Nino Mulac qui permute des listes de mots
import random
from lireListe import lireListeMot
#fonction permuteuse
def permutealea(mot):
    a=random.randint(0,len(mot)-1)
    return mot[a:]+mot[:a]
#fin

phrase=lireListeMot("Quelle phrase voulez vous tourner?")
for k in phrase:
    print(permutealea(k))