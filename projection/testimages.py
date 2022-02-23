from PIL import Image
import numpy as np
imgpil = Image.open("image.jpg")  
img = np.array(imgpil) # Transformation de l'image en tableau numpy
print(img.shape)
print(img.dtype)
print(tuple(img[0,0]))

img2= np.array(Image.open("image.jpg"))

for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        a=img2[i,j,0]
        print(a)
        img2[i,j,0] = a

img2.tofile("image2.jpg")
