#programme écrit par Nino Mulac qui fusionne 2 listes et les trie.
#fonction:
def fusion(liste1,liste2):
    liste1+=liste2
    liste1.sort()
    return liste1
#fin

print(fusion([1,3,5,7],[2,4,6,8]))
