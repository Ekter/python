#fonction...enfin regardez le nom quoi j'en ai marre(je crois qu'on doit faire juste des souschaines de longueur 1 mais c'est plus utile comme ça)
def occurences(chaine,sschaine):
    s=0
    for i in range(len(chaine)-len(sschaine)+1):
        if sschaine==chaine[i:i+len(sschaine)]:
            s+=1
    return s
#fin

print(occurences("abcdavbiuhsdoihaiuhzuydgxbhciusvhbiukdhsfuobzqsiucizdhbsqnhfiuezjzoirurgdfohdsn<csdhgbfyhuueofhdieushfnclsudohguicjo,renhc,oiejrsdoyrhiuj csd","a"))