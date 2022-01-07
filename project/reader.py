"""
Program to read data from chr files and create Character objects.
"""
import random
import sys

class Character():
    """
    Class to create Character objects.
    """
    def __init__(self, name: str,description:str,**kwargs):
        """
        Initialize Character object.
        """
        self.name = name
        self.description = description
        self.__dict__ = {**kwargs,**self.__dict__}

    def __str__(self) -> str:
        """
        Return string representation of Character object.
        """
        return f"{self.name} : {self.description}"

    def meet(self, other, *args) -> None:
        """
        Prints the meet dialog
        """
        list_meeters=[i.name for i in [self,other,*args]]
        list_possible_dialogs=[]
        for i in list_meeters:
            if list_meeters[~i] in i.meet_dialog:
                list_possible_dialogs.append(i.meet_dialog[list_meeters[~i]])
        print(random.choice(list_possible_dialogs))

def read_file(file_name: str)-> Character:
    """
    Reads a file and returns a Character object.
    """
    attributes={"name":"","description":""}
    previous=""
    with open(file_name, "r") as file:
        for line in file:
            if line[:2] == "//" or line=="":
                continue
            if line[0]=="|":
                target=attributes.copy()
                while "|" in line:
                    target=target[previous.partition("|")[0]]
                    line=line[1:]
                target[previous]+="\n"+line[1:].strip()
            else:
                res=line.partition("=")
                previous=res[0].strip().lower()
                if "[" in previous:
                    previous+="|"+previous.replace("[","").replace("]","")[1]
                attributes[previous]=res[2].strip()
    print("\n".join([f"#{key}# : #{value}#" for key,value in attributes.items()]))
    return Character(**attributes)

test=read_file("characters/test.chr")
person=read_file("characters/person.chr")

print(test.__dict__,"\n",person.__dict__)

dicttest={"name":"test","description":"test","meet_dialog":{"person":"test"}}
testeuh=dicttest["meet_dialog"]
testeuh["abc"]=":)"
print(testeuh)
print(dicttest)

def editsometimesnested(dictionary :dict,target:str,newvalue)-> None:
    """
    Edits a nested dictionary.
    """
    listtarget=target.split("|")
    for i in listtarget:
        dictionary=dictionary[i]
        #TO#DO à finir
