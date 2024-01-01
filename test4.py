from tkinter import *
fenetre = Tk()

fenetre.title('FEUILLE DE CALCUL')
fenetre.geometry('800x400+400+200')  # Largeur, Hauteur, décalage X, décalage Y
fenetre.resizable(False, False)


label = Label(fenetre, text="Nombre 1", padx=10).grid(column=0, row=0, padx=20)  # texte = Nombre1, colonne 1, ligne 1

# saisie du nombre 1 (width = largeur fenêtre)
#value1 = StringVar()
n1 = Entry(fenetre,  width=22).grid(column=1, row=0)  # fenêtre, colonne 2, ligne 1
#value1.set(n1)

label2 = Label(fenetre, text="Nombre 2", padx=10).grid(column=0, row=1, padx=20)  # texte = Nombre 2, colonne 1, ligne 2

# saisie du nombre 2
#value2 = StringVar()
n2 = Entry(fenetre,  width=22).grid(column=1, row=1)  # fenêtre : colonne 2, ligne 2
#value2.set(n2)

#r = "n1 + n2"
#print(n1)
label4 = Label(fenetre, text=" ").grid(column=1, row=2)  # Résultat : colonne 2, ligne 2


def ajouter(event=None):
    nombre1 = int(n1.get())
    nombre2 = int(n2.get())
    print(nombre1, nombre2)
    label4.config(text=nombre1+nombre2)


bouton = Button(fenetre, text="+ =", padx=10, font=('arial', 30, 'bold'), command=ajouter).grid(column=0, row=2,)  #Bouton "+" : colonne 1, ligne 3





fenetre.mainloop()