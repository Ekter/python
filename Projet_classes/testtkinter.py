from tkinter import * 
from tkinter.messagebox import *
fenetre = Tk()
canvas = Canvas(fenetre)
filename = PhotoImage(file = "ground.png")
image = canvas.create_image(50, 50, anchor=NE, image=filename)
canvas.pack()
label = Label(fenetre, text="Hello World")
label.pack()
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
label = Label(fenetre, text="Texte par défaut", bg="yellow")
label.pack()
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable="Test", width=30)
entree.pack()

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

Button(text='Action', command=callback).pack()
fenetre.mainloop()
