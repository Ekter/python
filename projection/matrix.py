"""matrix module made by me so i can make it the way i want"""

from typing import Union
from pandas import DataFrame

class Matrix():
    def __init__(self,lenght=3,height=3,values=None,type=int):
        assert len(values)==lenght*height
        self.lenght=lenght
        self.height=height
        self.values=[i for i in values]
        self.type=type

    def __iter__(self):
        yield from self.values

    def __getitem__(self,index : Union[int,tuple]) -> int:
        if type(index) is tuple:
            return self.values[index[0]*self.lenght+index[1]]
        else:
            return self.values[index]


    def t(self):
        i=0
        l=[]
        for i in range(len(self.values)):
            l.append(self.values[i])
            i+=self.lenght
            if i>=self.height:
                i-=self.height+1
        return Matrix(self.height,self.lenght,l)


    def __repr__(self) -> str:
        return "\n".join([" | ".join([str(j) for j in self.values[i:i+self.lenght]]) for i in range(0,len(self.values),self.lenght)])


if __name__=="__main__":
    a=Matrix(3,3,[1,2,3,4,5,6,7,8,9])
    print(a)
    print()
    print(a.t())
    print(a[0,0])
    print(a[0,1])
    print(a[2,2])
    print(Matrix(3,3,[1,2,3,4,5,6,7,8,9]))
    print()
    # print(Matrix(3,3,[1,2,3,4,5,6,7,8]))
    print(Matrix(3,3,[1,2,3,4,5,6,7,8,9]).t())
