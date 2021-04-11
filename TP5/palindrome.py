#fonction palindrome qui renvoie un boolean
def isPalindrome(chaine):
    for i in range(0,int((1+len(chaine))/2)):
        if chaine[i]!=chaine[-i-1]:
            return False
    return True
#fin
#Exemples d'utilisation:
#print(isPalindrome("ABCDCBA"))
#print(isPalindrome("ABCDDCBA"))
#print(isPalindrome("ABCD"))
mot="Bienvenue"
while mot!="arreter" and mot!="stop" and mot!="STOP" and mot!="fin":
    if isPalindrome(mot):
        print(mot,"est un palindrome.")
    else:
        print(mot,"n'est pas un palindrome")
    mot=input("Quel mot voulez vous tester? ")
