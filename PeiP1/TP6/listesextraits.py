l = ["fraise","kiwi",[12,34,56],5.34,"bonjour"]
"""
    'kiwi'
    [12,34,56]
    34
    ['kiwi', [12, 34, 56]]
    [5.34, 'bonjour']
    ['fraise', 'kiwi', 'pomme', [12, 34, 56], 5.34, 'bonjour']
    ['fraise', 'kiwi', 'pomme', [12, 34, 56], 5.34, 'bonjour', 'adieu']
"""
print(l[1])  #ici j'ai pas les ' autour de kiwi
print(l[2])
print(l[2][1])
print(l[1:3])
print(l[3:5])
l.insert(2,"pomme")
print(l)
l.append("adieu")
print(4/3000)
print(l)
#for i in range(len(l)):
#    print(l[i]) if i<len(l)