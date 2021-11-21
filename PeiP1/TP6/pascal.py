#programme créé par Nino Mulac qui donne le triangle de pascal

#fonction de récurrence
def recurrencePascal(elementprecedant):
    elementprecedant.append(0)
    nouvelelement=[elementprecedant[i]+elementprecedant[i-1] for i in range(0,len(elementprecedant))]
    return nouvelelement
#fin

#procedure d'affichage
def pascal(n):
    l=[1]
    for _ in range(n):
        l=recurrencePascal(l)
        print(l)
pascal(37)