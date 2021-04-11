dT=float(input("Distance totale:"))
dP=float(input("Distance déjà parcourue:"))
dAP=dT-dP
print("Il reste encore", dAP, "km à parcourir")
###tP=input("Temps de trajet déjà passé(en h m (heure minutes)):")
#a=0
#b=0
#for i in tP:
#    if i =="h":
#        a+=1
#    if i=="m":
#        b+=1
#tP2=tP.partition("h")
#tP4=tP2[2].partition("m")
#tP3=0
#if a>0:
#    tP3=float(tP2[0])*60+float(tP4[0])
#    tP2=tP2[2]
#if b>0:
#    tP2=tP.partition("m")
#    tP3=(float(tP4[0])+float(tP4[2])/60)+tP3
#tP=tP3
#tP=tP*0.016666666666666666666
tP=float(input("Temps parcouru en minutes:"))
v=dP/tP*60
print("Vitesse moyenne:",v)
print("Temps de trajet restant:",dAP/v*60)
heure=float(input("Heure actuelle(heure):"))
minute=float(input("Heure actuelle(min):"))
minute=60*heure+minute
minuteArrivee=minute+dAP/v*60
heureArrivee=minuteArrivee//60
print(heureArrivee,minuteArrivee%60)
