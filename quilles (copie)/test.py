def rotate(l) :
    l.append(l[0])
    l.pop(0)

def exchange(l, m):
    c=l.copy()
    l.clear()
    l.extend(m)
    m.clear()
    m.extend(c)

def filterIn(l, x):
    while x in l:
        l.remove(x)

def separate(l):
    alphabet="aeiouy"
    l1=[]
    for i in l:
        if i in alphabet:
            l1.append(i)
    for i in l1:
        l.remove(i)
        l.append(i)

def double(l):
    return([2*i for i in l])

def filtre(l, x):
    l1=l.copy()
    while x in l1:
        l1.remove(x)
    return(l1)

def refer(l,m):
    for i in m:
        if i is l:
            return True
    for i in l:
        if i is m:
            return True
    return False

def circular(l):
    for i in l:
        if type(i) is int:
            if i is l:
                return True
        elif type(i) is list:
            for k in i:
                if k is l:
                    return True
    return False

l=[2]
l.append(l)
print(l)