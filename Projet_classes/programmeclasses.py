class Etre_vivant(object):
    "Cette classe est un être vivant fondamental, avec des PVs"
    def __init__(self,pvmax,name,type="Animal",loot=[],description=""):
        self.pv=pvmax
        self.pvmax=pvmax
        self.name=name
        self.type=type
        self.loot=loot
        self.description=description
    def __repr__(self):
        return """Nom: {}
Type:{}
PVs:{}/{}
{}
""".format(self.name,self.type,self.pv,self.pvmax,self.description)
    def perdredespvs(self,pvsperdus: int)->int:
        "Si on pert des pvs, c'est là"
        self.pv=self.pv-pvsperdus
        if self.pv<=0:
            print(self,"est mort!")
            return "mort",self.loot
        else:
            return self.pv
    def tuer(self)->bool:
        "Cette fonction tue instantanément n'importe quoi. Elle revoie les résultat (si la créature est bel et bien morte) en tant que booléen."
        a=self.perdredespvs(self.pv)
        return type(a) is str


listeetresvivants=[]
plik=Etre_vivant(37,"Plik","Univers",[],"L'entité univers, représentant l'ordre, le nature, et la vérité.")
listeetresvivants.append(plik)
mouton1=Etre_vivant(10,"Mouton",loot=[("viande",100,1,5),("laine",100,1,2)])
print(listeetresvivants)
