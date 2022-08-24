#programme codé par Nino Mulac, qui code par le code césar
#fonction qui transforme une lettre
def cesarlettre(lettre,rang):
    dict={ "a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", "g":"h", "h":"i", "i":"j", "j":"k", "k":"l", "l":"m", "l":"m", "m":"n", "n":"o", "o":"p", "p":"q", "q":"r", "r":"s", "s":"t", "t":"u", "u":"v", "v":"w", "w":"x", "x":"y", "y":"z", "z":"a"}
    for k in range(rang):
        lettre=dict.get(lettre)
    return lettre
#fin

#fonction qui code le mot
def cesar(chaine,rang):
    nchaine=""
    for abcd in range(0,len(chaine)):
        nchaine=nchaine+cesarlettre(chaine[abcd],rang)
    return nchaine
#fin

#exemples:
print(cesar(cesar("plik",37),-37%26))

for i in range(26):
    print(cesar("GPQQXITMEDHTPVGTTXCIPRI".lower(),i))
