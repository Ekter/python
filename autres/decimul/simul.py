"""simulation of a situation"""


from math import sqrt
from decimul import Situation

class StepSituation(Situation):
    "situation class"
    def __init__(self,value1:int,value2:int) -> None:
        self.v_1=value1
        self.v_2=value2

    def potential(self) -> float:
        "return the potential of the situation"
        return sqrt(self.v_1**2+self.v_2**2)

    def next_steps(self) -> list["Situation"]:
        "return the list of next steps"
        return [StepSituation(self.v_1+1,self.v_2),StepSituation(self.v_1,self.v_2+1)]

situ = StepSituation(0,0)
print(situ)
print(situ.potential())

print(situ.next_steps())

print(situ.find_best_next(3))
