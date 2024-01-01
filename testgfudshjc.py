
from tkinter import *

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Feuille de calcul")

class Feuille:
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.label = Label(self.frame, text="Feuille de calcul")
        self.label.grid(row=0, column=0, columnspan=2)

        self.champ_de_texte = ChampDeTexte(self.frame, "nombre à calculer", command=self.calculer) #à compléter (on peut réutiliser un ChampDeTexte
        # fait la dernière fois, sinon il faut mettre un label puis une Entry et
        # un bouton pour valider)
        self.champ_de_texte.afficher()
        

        self.label_resultats = Label(self.frame, text="Résultats")
        self.label_resultats.grid(row=2, column=0, columnspan=2)
        self.resultats = Resultats(self.frame)

    def afficher(self):
        self.frame.pack()

    def calculer(self):
        # à compléter (il faut appeler la méthode nombre_premiers et faire une
        # boucle pour ajouter les résultats à la frame)
        self.resultats.ajouter_resultat("Résultat à remplacer par le calcul de nombre_premiers")


class Resultats:
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.liste = []

    def ajouter_resultat(self, texte):
        a=Label(self.frame, text=texte)
        a.pack()
        self.liste.append(a)
        # à compléter (il faut créer un label et l'ajouter à la frame, on peut
        # utiliser la méthode pack pour que ce soit plus simple)
        print(texte)
        return a


class ChampDeTexte:
    def __init__(self, fenetre, texte, command=None):
        self.frame = Frame(fenetre, bg="grey")
        self.label = Label(self.frame, text=texte)
        self.entrée = Entry(self.frame)
        self.bouton = Button(self.frame, text="Valider", command=command)
        self.label.grid(row=0, column=0)
        self.entrée.grid(row=0, column=1)
        self.bouton.grid(row=0, column=2)

    def afficher(self):
        self.frame.grid(row=1, column=0)



feuille = Feuille(fenetre)

feuille.afficher()


fenetre.mainloop()
