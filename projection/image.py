import numpy as np

class Image():
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.mat=[[(0,0,0) for _ in range(height)] for _ in range(width)]

    def __setitem__(self,key,value):
        self.mat[int(key.ord)][int(key.abs)]=value

    def __getitem__(self,key):
        return self.mat[int(key.ord)][int(key.abs)]

    def to_image(self,file_name):
        cv.imwrite(file_name,np.array(self.mat))
