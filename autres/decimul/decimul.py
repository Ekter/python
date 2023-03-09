"""code to find if a situation is good, and make decisions accordingly"""

from math import sqrt
from abc import ABC, abstractmethod



class Situation(ABC):
    "situation class"

    @abstractmethod
    def __init__(self,value1:int,value2:int) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"({','.join([str(self.__dict__[i]) for i in self.__dict__])})"

    @abstractmethod
    def potential(self) -> float:
        "return the potential of the situation"
        raise NotImplementedError

    @abstractmethod
    def next_steps(self) -> list["Situation"]:
        "return the list of next steps"
        raise NotImplementedError

    def find_best_next(self, depht=1) -> "Situation":         #,l:List["Situation"]=None
        "find the best next step"
        if depht==0:
            return self
        list_future_sit=self.next_steps()
        lpot=[]
        for future_sit in list_future_sit:
            lpot.append((future_sit,future_sit.find_best_next(depht-1)))
        return max(lpot,key=lambda x:x[1].potential())[0]
