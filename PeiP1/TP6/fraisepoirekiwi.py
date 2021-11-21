#programme créé par Nino Mulac qui transforme une liste de fruits en un panier, via un dictionnaire.
#la fonction en question
def fruits(listeFruits,dictionnaireFruits={"F":"*","K":"%","P":"@"}):
    panier=""
    for fruit in listeFruits:
        panier+=dictionnaireFruits.get(fruit[0])*fruit[1]
    return panier
#fin

listeDesCourses=[["F",2],["K",6],["F",1],["P",3]]
equivalentsFruits={"F":"^","K":"~","P":"&","GC":"@"}#attribution d'un équivalent à chacun des fruits: fraise, poire, kiwi et GoldenClémentine
print(fruits(listeDesCourses))
print(fruits([["F",2],["GC",37],["F",1],["P",25],["GC",2],["K",0],["F",25],["GC",37]],equivalentsFruits))