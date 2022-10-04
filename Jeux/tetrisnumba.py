from numba import njit
import numpy as np
from random import choice
"""
Structure : le tableau de jeu est un tableau de 10 par 22, représenté par un array de uint32.
Chaque bit représente une case. 0 est vide, 1 est pleine.
"""
game=np.zeros(22,dtype=np.uint32)
current_piece=np.array([0,7,0,0],dtype=np.uint32)
location_current_piece=np.array([0,0],dtype=np.uint8)
list_pieces=np.zeros
@njit
def create_random_piece():
    """
    Crée une pièce aléatoire.
    """
    piece=np.zeros(4,dtype=np.uint32)
    piece[0]=1
    piece[1]=1
    piece[2]=1
    piece[3]=1
    return piece
