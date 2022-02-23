
import pygame
import pygame.font
import pygame.event
import pygame.draw
from pygame.locals import *


def quel_niveau(num):  # 13 colonnes 14 lignes
    print(num)
    if num == 1:
        niveau = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 9, 9, 9,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2,
                   2, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0,
                   0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                   4, 4, 4, 4, 4, 4, 6, 6, 4, 4, 4, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50]]
    elif num == 2:
        niveau = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9,
                   9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 9, 50],
                  [0, 0, 0, 0, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 9, 50],
                  [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 9, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 9, 50],
                  [0, 0, 0, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 9, 50],
                  [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                   4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50]]
    elif num == 3:
        niveau = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9,
                   0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
                   0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
                   0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 2,
                   0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 9, 2, 0, 0, 0, 0, 2,
                   0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 9, 2, 2, 0, 0, 0, 0, 2,
                   0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 50],
                  [0, 0, 0, 0, 0, 9, 2, 2, 2, 0, 0, 0, 0, 2,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 9, 2, 2, 2, 2, 0, 0, 0, 0, 2,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 9, 2, 2, 2, 2, 2, 6, 6, 6, 6, 2,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                   4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50]]
    elif num >= 4:
        niveau = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                   4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50]]
    elif num == 0:
        niveau = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                   4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50]]
    return niveau


def display_text(message, x_box, y_box, taille, R1, G1, B1):
    global fenetre
    font = pygame.font.Font(None, taille)
    text = font.render(message, 1, (R1, G1, B1))
    textpos = text.get_rect(x=x_box, y=y_box)
    fenetre.blit(text, textpos)


def collage_du_fond():
    ligne = 0
    while ligne < 20:
        colonne = 0
        while colonne < 25:
            if niveau[ligne][colonne] == 1:
                fenetre.blit(mur, (colonne*40, ligne*35))
            if niveau[ligne][colonne] == 2:
                fenetre.blit(brique, (colonne*40, ligne*35))
            if niveau[ligne][colonne] == 4:
                fenetre.blit(sol, (colonne*40, ligne*35))
            if niveau[ligne][colonne] == 5:
                fenetre.blit(ciel, (colonne*40, ligne*35))
            if niveau[ligne][colonne] == 9:
                fenetre.blit(piece, (colonne*40, ligne*35))
            if niveau[ligne][colonne] == 6:
                fenetre.blit(piques, (colonne*40, ligne*35))
            colonne = colonne+1
        ligne = ligne+1


adroit = 0
agauche = 0
compteur = 0
score = 0
mort = 0
vie = 3
anim_saut_panda, anim_saut_raton = 0, 0
bouton_gauche_appuyé_panda, bouton_droit_appuyé_panda = 0, 0
bouton_gauche_appuyé_raton, bouton_droit_appuyé_raton = 0, 0
bouton_haut_appuyé_panda, bouton_haut_appuyé_raton = 0, 0
double_saut_panda, double_saut_raton = 0, 0
mur_droite_panda, mur_droite_raton = 1, 1
mur_gauche_panda, mur_gauche_raton = 1, 1
gravitation_panda, gravitation_raton = 0, 0
x_panda, x_raton = 4, 4
y_panda, y_raton = 0, 0
niv = 1
BOUCLE = 1
menu = 1
scene = 0
inertie_gauche_panda, inertie_gauche_raton = 0, 0
inertie_droite_panda, inertie_droite_raton = 0, 0
v_panda, v_raton = 0, 0
saut_lancé_panda, saut_lancé_raton = 0, 0
gravite_panda, gravite_raton = 2, 2
continuer = 1
pygame.init()
fenetre = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('NewSuperUgo')
sol = pygame.image.load("Sol.png").convert()
ciel = pygame.image.load("Ciel.png").convert()
gameover = pygame.image.load("GameOver.jpg").convert()
detect = pygame.image.load("ROUGE.png").convert()
detect2 = pygame.image.load("BLEU.png").convert()
panda = pygame.image.load("Panda.png").convert_alpha()
raton = pygame.image.load("Raton.png").convert_alpha()
saut1 = pygame.image.load("saut1.png").convert_alpha()
saut2 = pygame.image.load("saut2.png").convert_alpha()
saut3 = pygame.image.load("saut3.png").convert_alpha()
brique = pygame.image.load("brique.png").convert()
mur = pygame.image.load("mur.png").convert()
montre = pygame.image.load("montre.jpg").convert()
piece = pygame.image.load("piece.png").convert_alpha()
piques = pygame.image.load("piques.png").convert_alpha()
monstre = pygame.image.load("monstre.png").convert_alpha()
niveau = quel_niveau(niv)
position_panda = panda.get_rect()
position_raton = raton.get_rect()
position_monstre = monstre.get_rect()
collage_du_fond()
position_panda = position_panda.move(0, 455)
position_raton = position_raton.move(0, 455)
fenetre.blit(panda, position_panda)
fenetre.blit(raton, position_raton)
clock = pygame.time.Clock()
while BOUCLE:
    dt = clock.tick(60)
    for event in pygame.event.get():
        # Quitter
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            BOUCLE = 0
            continuer = 0
        if menu == 1:
            fond = pygame.image.load("fondMenu.jpg").convert()
            fenetre.blit(fond, (0, 0))
            message1 = "1- Commencer une nouvelle Partie"
            display_text(message1, 20, 20, 32, 255, 255, 255)
            message2 = "2- Reprendre une sauvegarde  "
            display_text(message2, 20, 60, 32, 255, 255, 255)
            message3 = "3- Quitter"
            display_text(message3, 20, 100, 32, 255, 255, 255)
            pygame.display.flip()
            menu = 0
            BOUCLE = 0
            if event.type == KEYDOWN:

                if event.key == K_KP1:
                    menu = 0
                    BOUCLE = 0
                if event.key == K_KP2:
                    menu = 0
                    scene = 2
                if event.key == K_KP3:
                    BOUCLE = 0
                    continuer = 0
        elif scene == 2:
            fond2 = pygame.image.load("fondForet.jpg").convert()
            fenetre.blit(fond2, (0, 0))
            pygame.display.flip()
clock = pygame.time.Clock()
pygame.key.set_repeat(5, 20)
# musique_jeu=pygame.mixer.Sound("Musique_geniale.wav")
# musique_jeu.play()
while continuer:
    clock.tick(60)
    gravitation_panda = 0
    y = y_panda
    ligne_panda = int(position_panda.y/35)+2
    y = y_raton
    ligne_raton = int(position_raton.y/35)+2
    x = x_panda
    colonne_panda = int(position_panda.x/40)
    x = x_raton
    colonne_raton = int(position_raton.x/40)
    touche = pygame.key.get_pressed()
    for event in pygame.event.get():
        pygame.event.pump()
        # Panda Haut
        if event.type == KEYDOWN and touche[K_UP] == 1 and saut_lancé_panda == 0:
            if niveau[ligne_panda][colonne_panda] != 0 or niveau[ligne_panda][colonne_panda+1] != 0:
                gravite_panda = -gravite_panda
                saut_lancé_panda = 1
                bouton_haut_appuyé_panda = 1
                position_panda = position_panda.move(0, -3)
        elif event.type == KEYUP and bouton_haut_appuyé_panda == 1:
            bouton_haut_appuyé_panda = 0
            double_saut_panda = 1
        if event.type == KEYDOWN and event.key == K_UP and double_saut_panda == 1:
            saut_lancé_panda = 10
            double_saut_panda = 0
            anim_saut_panda = 1
            if 0 < gravite_panda:
                gravite_panda = -gravite_panda
       # Raton Haut
        if event.type == KEYDOWN and touche[K_z] == 1 and saut_lancé_raton == 0:
            if niveau[ligne_raton][colonne_raton] != 0 or niveau[ligne_raton][colonne_raton+1] != 0:
                gravite_raton = -gravite_raton
                saut_lancé_raton = 1
                bouton_haut_appuyé_raton = 1
                position_raton = position_raton.move(0, -3)
        elif event.type == KEYUP and bouton_haut_appuyé_raton == 1:
            bouton_haut_appuyé_raton = 0
            double_saut_raton = 1
        if event.type == KEYDOWN and touche == [K_z] and double_saut_raton == 1:
            saut_lancé_raton = 10
            double_saut_raton = 0
            anim_saut_raton = 1
            if 0 < gravite_raton:
                gravite_raton = -gravite_raton
       # Panda Droite
        if event.type == KEYDOWN and touche[K_RIGHT] == 1 and mur_droite_panda == 1:
            x_panda = x_panda+0.4
            v_panda = 10-(40/x_panda)
            if v_panda < 3:
                v_panda = 3
            position_panda = position_panda.move(int(v_panda), 0)
            bouton_droit_appuyé_panda = 1
            inertie_droite_panda = 0
            inertie_gauche_panda = 0
        elif event.type == KEYUP and bouton_droit_appuyé_panda == 1:
            inertie_droite_panda = 1
            bouton_droit_appuyé_panda = 0
       # Raton Droite
        if event.type == KEYDOWN and touche[K_d] == 1 and mur_droite_raton == 1:
            x_raton = x_raton+0.4
            v_raton = 10-(40/x_raton)
            if v_raton < 3:
                v_raton = 3
            position_raton = position_raton.move(int(v_raton), 0)
            bouton_droit_appuyé_raton = 1
            inertie_droite_raton = 0
            inertie_gauche_raton = 0
        elif event.type == KEYUP and bouton_droit_appuyé_raton == 1:
            inertie_droite_raton = 1
            bouton_droit_appuyé_raton = 0
       # Panda Gauche
        if event.type == KEYDOWN and touche[K_LEFT] == 1 and mur_gauche_panda == 1:
            x_panda = x_panda+0.4
            v_panda = (10-(40/x_panda))*-1
            if v_panda > -3:
                v_panda = -3
            position_panda = position_panda.move(int(v_panda), 0)
            bouton_gauche_appuyé_panda = 1
            inertie_gauche_panda = 0
            inertie_droite_panda = 0
        elif event.type == KEYUP and bouton_gauche_appuyé_panda == 1:
            inertie_gauche_panda = 1
            bouton_gauche_appuyé_panda = 0
       # Raton Gauche
        if event.type == KEYDOWN and touche[K_q] == 1 and mur_gauche_raton == 1:
            x_raton = x_raton+0.4
            v_raton = (10-(40/x_raton))*-1
            if v_raton > -3:
                v_raton = -3
            position_raton = position_raton.move(int(v_raton), 0)
            bouton_gauche_appuyé_raton = 1
            inertie_gauche_raton = 0
            inertie_droite_raton = 0
        elif event.type == KEYUP and bouton_gauche_appuyé_raton == 1:
            inertie_gauche_raton = 1
            bouton_gauche_appuyé_raton = 0
        if event.type == MOUSEMOTION and event.buttons[1] == 1:
            continuer = 0
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = 0
    if gravite_panda < 0:
        saut_lancé_panda = saut_lancé_panda+1
        if saut_lancé_panda >= 46:
            gravite_panda = -gravite_panda
            saut_lancé_panda = 0
            double_saut_panda = 0
    if gravite_raton < 0:
        saut_lancé_raton = saut_lancé_raton+1
        if saut_lancé_raton >= 46:
            gravite_raton = -gravite_raton
            saut_lancé_raton = 0
            double_saut_raton = 0
    if niveau[ligne_panda-1][colonne_panda+1] == 50 or niveau[ligne_raton-1][colonne_raton+1] == 50:
        niv = niv+1
        niveau = quel_niveau(niv)
        x_panda = 4
        x_raton = 4
        position_panda = position_panda.move(
            colonne_panda*-40, -35*ligne_panda+490)
        position_raton = position_raton.move(
            colonne_raton*-40, -35*ligne_raton+490)
        position_panda = position_panda.move(
            colonne_panda*-40, -35*ligne_panda+490)
        position_raton = position_raton.move(
            colonne_raton*-40, -35*ligne_raton+490)
    if niv == 0:
        vie = 3
    if (niveau[ligne_panda][colonne_panda+0] == 0 or niveau[ligne_panda][colonne_panda+0] == 9) and (niveau[ligne_panda][colonne_panda+1] == 0 or niveau[ligne_panda][colonne_panda+1] == 9):
        position_panda = position_panda.move(0, gravite_panda)
        print(gravite_panda)
    if ((niveau[ligne_panda-2][colonne_panda+0] != 0 and niveau[ligne_panda-2][colonne_panda+0] != 9) and (niveau[ligne_panda-1][colonne_panda+0] == 0 or niveau[ligne_panda-1][colonne_panda+0] == 9)) or (niveau[ligne_panda-2][colonne_panda+1] != 0 and niveau[ligne_panda-2][colonne_panda+1] != 9) and (niveau[ligne_panda-1][colonne_panda+1] == 0 or niveau[ligne_panda-1][colonne_panda+1] == 9):
        saut_lancé_panda = 46
        if gravite_panda > 0:
            gravite_panda = -gravite_panda
    if (niveau[ligne_panda-2][colonne_panda-0] != 0 and niveau[ligne_panda-2][colonne_panda-0] != 9 and niveau[ligne_panda-2][colonne_panda-0] != 50) or niveau[ligne_panda-1][colonne_panda-0] != 0 and niveau[ligne_panda-1][colonne_panda-0] != 50 and niveau[ligne_panda-1][colonne_panda-0] != 9:
        x_panda = 4
        v_panda = 0
        mur_gauche_panda = 0
    else:
        mur_gauche_panda = 1
    if (niveau[ligne_panda-0][colonne_panda-0] != 0 and niveau[ligne_panda-0][colonne_panda-0] != 9 and niveau[ligne_panda-0][colonne_panda-0] != 50) and (niveau[ligne_panda-0][colonne_panda+1] == 0 or niveau[ligne_panda-0][colonne_panda+1] == 9 or niveau[ligne_panda-0][colonne_panda+1] == 50):
        position_panda = position_panda.move(0, -3)
        y = y_panda
        ligne_panda = int(position_panda.y/35)+2
        x = x_panda
        colonne_panda = int(position_panda.x/40)
        if (niveau[ligne_panda-0][colonne_panda-0] != 0 and niveau[ligne_panda-0][colonne_panda-0] != 50 and niveau[ligne_panda-0][colonne_panda-0] != 9) and (niveau[ligne_panda-0][colonne_panda+1] == 0 or niveau[ligne_panda-0][colonne_panda+1] == 9 or niveau[ligne_panda-0][colonne_panda+1] == 50):
            x_panda = 4
            v_panda = 0
            mur_gauche_panda = 0
        else:
            mur_gauche_panda = 1
        position_panda = position_panda.move(0, 3)
        ligne_panda = int(position_panda.y/35)+2
        x = x_panda
        colonne_panda = int(position_panda.x/40)
    if (niveau[ligne_panda-2][colonne_panda+1] != 0 and niveau[ligne_panda-2][colonne_panda+1] != 50 and niveau[ligne_panda-2][colonne_panda+1] != 9) or (niveau[ligne_panda-1][colonne_panda+1] != 0 and niveau[ligne_panda-1][colonne_panda+1] != 50 and niveau[ligne_panda-1][colonne_panda+1] != 9):
        x_panda = 4
        v_panda = 0
        mur_droite_panda = 0
    else:
        mur_droite_panda = 1
    if (niveau[ligne_panda-0][colonne_panda+1] != 0 and niveau[ligne_panda-0][colonne_panda+1] != 50 and niveau[ligne_panda-0][colonne_panda+1] != 9) and (niveau[ligne_panda-0][colonne_panda+0] == 0 or niveau[ligne_panda-0][colonne_panda+0] == 9 or niveau[ligne_panda-0][colonne_panda+0] == 50):
        position_panda = position_panda.move(0, -3)
        y = y_panda
        ligne_panda = int(position_panda.y/35)+2
        x = x_panda
        colonne_panda = int(position_panda.x/40)
        if (niveau[ligne_panda-0][colonne_panda+1] != 0 and niveau[ligne_panda-0][colonne_panda+1] != 9 and niveau[ligne_panda-0][colonne_panda+1] != 50) and (niveau[ligne_panda-0][colonne_panda+0] == 0 or niveau[ligne_panda-0][colonne_panda+0] == 9 or niveau[ligne_panda-0][colonne_panda+0] == 50):
            x_panda = 4
            v_panda = 0
            mur_droite_panda = 0
        else:
            mur_droite_panda = 1
        position_panda = position_panda.move(0, 3)
        y = y_panda
        ligne_panda = int(position_panda.y/35)+2
        x = x_panda
        colonne_panda = int(position_panda.x/40)
    if inertie_droite_panda == 1:
        x_panda = x_panda-3
        if x_panda <= 4:
            x_panda = 4
            inertie_droite_panda = 0
        v_panda = 10-(40/x_panda)
        position_panda = position_panda.move(int(v_panda), 0)
    if inertie_gauche_panda == 1:
        x_panda = x_panda-3
        if x_panda <= 4:
            x_panda = 4
            inertie_gauche_panda = 0
        v_panda = -(10-(40/x_panda))
        pygame.time.delay(20)
        position_panda = position_panda.move(int(v_panda), 0)
    if niveau[ligne_panda-1][colonne_panda+0] == 9:
        score = score+100
        niveau[ligne_panda-1][colonne_panda+0] = 0
    if niveau[ligne_panda-2][colonne_panda] == 9:
        score = score+100
        niveau[ligne_panda-2][colonne_panda] = 0
    if niveau[ligne_panda-1][colonne_panda+1] == 9:
        score = score+100
        niveau[ligne_panda-1][colonne_panda+1] = 0
    if niveau[ligne_panda-2][colonne_panda+1] == 9:
        score = score+100
        niveau[ligne_panda-2][colonne_panda+1] = 0
     # Vies
    if niveau[ligne_panda][colonne_panda] == 6:
        position_panda = position_panda.move(0, 2)
        y = y_panda
        ligne_panda = int(position_panda.y/35)+2
        x = x_panda
        colonne_panda = int(position_panda.x/40)
        if niveau[ligne_panda][colonne_panda] != 6:
            vie = vie-1
            x_panda = 4
            position_panda = position_panda.move(
                colonne_panda*-40, -35*ligne_panda+490)
        else:
            position_panda = position_panda.move(0, -2)
            y = y_panda
            ligne_panda = int(position_panda.y/35)+2
            x = x_panda
            colonne_panda = int(position_panda.x/40)
    if niveau[ligne_panda-2][colonne_panda+1] == 6 or niveau[ligne_panda-1][colonne_panda+1] == 6 or niveau[ligne_panda-2][colonne_panda] == 6:
        vie = vie-1
        x_panda = 4
        position_panda = position_panda.move(
            colonne_panda*-40, -35*ligne_panda+490)
    collage_du_fond()
    if vie <= 0:
        buff = niv
        fenetre.blit(gameover, (0, 0))
        niv = 0
        niveau = quel_niveau(niv)
        print("CBON")
        niv = buff
    # if niv==1:
    #
    #display_text("score : " +str(score),0,0,24,0,0,0)
    display_text("score : " + str(score), 200, 150, 24, 0, 0, 0)
    display_text("Vies : "+str(vie), 200, 100, 24, 0, 0, 0)
    display_text("Tigrou : "+str(saut_lancé_panda), 200, 200, 24, 0, 0, 0)
    # fenetre.blit(detect,((colonne_panda+0)*40,ligne_panda*35))
    # fenetre.blit(detect2,((colonne_panda+1)*40,ligne_panda*35))
    # fenetre.blit(detect2,((colonne_panda+0)*40,(ligne_panda-3)*35))
    # fenetre.blit(detect,((colonne_panda+0)*40,(ligne_panda-2)*35))
    # fenetre.blit(detect,((colonne_panda+1)*40,(ligne_panda-3)*35))
    # fenetre.blit(detect2,((colonne_panda+1)*40,(ligne_panda-2)*35))
    # fenetre.blit(detect2,((colonne_panda+0)*40,(ligne_panda-2)*35))
    # fenetre.blit(detect2,((colonne_panda+0)*40,(ligne_panda-1)*35))
    # fenetre.blit(detect2,((colonne_panda+0)*40,(ligne_panda-0)*35))
    fenetre.blit(panda, position_panda)
    fenetre.blit(raton, position_raton)
    if anim_saut_panda == 1:
        compteur = compteur+1
        if compteur == 1:
            x_saut = colonne_panda*40-20
            y_saut = ligne_panda*35
        if compteur <= 5:
            fenetre.blit(saut1, (x_saut, y_saut))
        elif compteur <= 10:
            fenetre.blit(saut2, (x_saut, y_saut))
        elif compteur <= 15:
            fenetre.blit(saut3, (x_saut, y_saut))
        elif compteur == 20:
            compteur = 0
            anim_saut_panda = 0
    pygame.display.flip()
pygame.quit()
