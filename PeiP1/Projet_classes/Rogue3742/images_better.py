"""script to include all images from the folder images"""

import os
import sys
from tkinter import PhotoImage
from typing import Union

class Image64(PhotoImage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Image32(PhotoImage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def to_64(self):
        return self.zoom(2)

def get_dictionaries():
    folders = os.listdir("PeiP1/Projet_classes/Rogue3742/images/")

    dic_images = {}
    for folder in folders:
        files = os.listdir(f"PeiP1/Projet_classes/Rogue3742/images/{folder}")
        for file in files:
            name = file.split(".")[0]
            if name not in dic_images:
                dic_images[name] = {}
            dic_images[name][folder] = f"PeiP1/Projet_classes/Rogue3742/images/{folder}/{file}"

