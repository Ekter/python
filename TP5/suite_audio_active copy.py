#programme codé par Nino Mulac qui donne le n-eme terme de la suite audio-active, par récurrence.
#fonction de récurrence
def suiteAudioActive(chn):
    chn=chn.replace("111","ca").replace("222","cb").replace("333","cc").replace("11","ba").replace("22","bb").replace("33","bc").replace("1","aa").replace("2","ab").replace("3","ac")
    chn=chn.replace("a","1").replace("b","2").replace("c","3")
    return chn

#fin
resultat="1"
n=80
for i in range(n):
    resultat=suiteAudioActive(resultat)
print(resultat)