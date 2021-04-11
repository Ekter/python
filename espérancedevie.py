#/usr/bin/python3
esp=85
a=int(input("Est ce que tu fumes(0-1)?"))
if a:
    esp-=10
pression=int(input("quelle est ta pression artérielle en mm"))
pression-=120
pression= pression//20
esp-=2*pression
bleuet=int(input("est ce que tu manges plus de 2kg de bleuets par an?(0-1)"))
esp+=2*bleuet
print("éspérance de vie:",esp)
