import pandas as pd

_map="""
0|0|0|0|1|0|1|0|1|0|1|0|1|0|1
1|0|0|1|0|0|1|0|1|0|1|0|1|0|1
1|0|0|1|0|1|0|1|1|1|0|0|1|0|1
0|0|0|1|0|1|0|0|0|1|0|0|0|0|0
0|0|0|0|0|0|0|0|0|0|0|0|0|0|0"""


l=[line.split("|") for line in _map.split("\n")]
print(l)

l_act=[]
for x,line in enumerate(l):
    for y,value in enumerate(line):
        



dic={"x":[],"y":[],"value":[]}

for x,line in enumerate(l):
    for y,value in enumerate(line):
        dic["x"].append(y)
        dic["y"].append(x)
        dic["value"].append(value)

df=pd.DataFrame(dic)
print(df)
list_regions=[]
for k in df["value"].unique():
    dic={"coord":[]}
    for i in df.index:
        # print(df.iloc[i])
        a=df.iloc[i]
        if a["value"]==k:
            # print(a)
            dic["coord"].append((a["x"],a["y"]))
    print(dic)
    list_regions.append(dic["coord"])

for region in list_regions:
    print(region)