#fonction...enfin regardez le nom quoi j'en ai marre
def occurences(chaine,sschaine):
    s=0                                         #équivalent à i=0
    for i in range(len(chaine)-len(sschaine)):  #             while i<len(chaine)-len(sschaine)
        if sschaine==chaine[i:i+len(sschaine)]: #                if chaine[i]==sschaine
            s+=1                                #                    s+=1
                                                #                i+=1

    return s
#fin