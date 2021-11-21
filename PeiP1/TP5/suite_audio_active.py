#programme codé par Nino Mulac qui donne le n-eme terme de la suite audio-active, par récurrence.
#fonction de récurrence
def suiteAudioActive(chn):
    sortie=""
    n=0
    while n<len(chn):
        k=1
        if len(chn)>n+1:
            if chn[n+1]==chn[n]:
                k+=1
                if len(chn)>n+2:
                    if chn[n+2]==chn[n]:
                        k+=1
        sortie=sortie+str(k)+chn[n]
        n+=k
    return sortie
#fin
resultat="1"
n=10
for i in range(n):
    print(resultat)
    resultat=suiteAudioActive(resultat)