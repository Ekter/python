import re
from numpy import nan
import copy

exSerieList = []
intermediateList = []
A0 = 0
serList =  ['Série 1', 'Série 2', 'Série 3', 'Série 4', 'Série 1', 'Série 2', 'Série 3', 'Série 4', 'Série 1', 'Série 2', 'Série 3', 'Série 4', 'Série 1', 'Série 2', 'Série 3', 'Série 4', nan, 'Série 1', 'Série 2', 'Série 3', 'Série 4', 'Série 1', 'Série 2', 'Série 3', 'Série 4', 'Série 1', 'Série 2', 'Série 3', 'Série 4', 'Série 1', 'Série 2', 'Série 3', 'Série 4', 'Série 1', 'Série 2', 'Série 3', 'Série 4', 'Série 1', 'Série 2', 'Série 3', 'Série 4', nan]


#transformer les nan en SEPARE

"""for index,serie in enumerate(serList):
    if str(serie) == "nan":
        serList[index] = "SEPARE"""

"""print(serList)

for serie in serList:
    a = int(re.search(r'\d+', serie).group())"""

    

for serie in serList:

    if str(serie)!="nan":
        a = int(re.search(r'\d+', serie).group())
        if a > A0:
            intermediateList.append(serie)
            A0 = a
        else:
            intermediateList.insert(0, serie)
            exSerieList.append(intermediateList)
            intermediateList = []
            A0 = 0
    else:
        intermediateList.append("SEPARE")
        exSerieList.append(copy.copy(intermediateList))
        # intermediateList = []
        #exSerieList.append("SEPARE")"""

exSerieList[0].pop(0)
#exSerieList.pop(len(exSerieList)-1)
exSerieList[-1].insert(0, "Série 1")
# print(exSerieList)


import pandas as pd

df= pd.read_excel("Sport2.xlsx")

index = []
for name in df["Exercices"]:
    index.append(name)
df["Séries"].fillna(inplace=True)
print(df)
