from typing import Dict, List


graphe={"A":[("B",4),("D",1)],"B":[("A",4),("E",1),("C",2)],"C":[("G",2),("B",2),("F",3)],"D":[("A",1),("E",1)],"E":[("B",1),("D",1),("F",2)],"F":[("E",2),("C",3)],"G":[("C",2)]}
def dijkstra(graph : Dict, elements : List) -> List:
    lres=[]
    i=elements[0]
    li=graph.get(i)
    continuer=True
    for k in range(len(elements)):
        lt=[]
        for k in elements:
            if k in []:
                n=li[k]
                lt.append(n)
                






dijkstra(graphe,["A","B","C","D","E","F","G"])