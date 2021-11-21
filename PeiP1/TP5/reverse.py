#fonction qui renverse une chaine
def reverse(chn):
    nhc=""
    for i in chn:
        nhc=i+nhc
    return nhc
#fin

print(reverse("abcdefg"))
print(reverse(reverse("abcde")))