#Programme écrit par Nino Mulac qui met la première lettre de chaque mot en majuscule. Par rapport au votre, il gère en plus les minuscules non-ASCII, comme les voyelles accentuées.
#fonction majusculise
def majusculise(chn,sep=" .;,?:/!%^-~+=*()_{[}]"):
    chn=sep[0]+chn
    for i in range(len(chn)-1):
        if sep.find(chn[i])>=0:
            chn=chn[:i+1]+chn[i+1].upper()+chn[i+2:]
    return chn[1:]
#fin

#mais comme vous demandez une procédure
def majusculiseprocedure(chn,sep=" .;,?:/!%^-~+=*()_{[}]"):
    return majusculise(chn,sep)
#c'est nul les procédures

#exemples d'utilisation:
chn1="""Un long texte en minuscules 
        Les 14 gendarmes à Saint Tropez"""
print(majusculise(chn1))
majusculiseprocedure(chn1)
