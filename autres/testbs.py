from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen("https://fr.wikipedia.org/wiki/Hom%C3%A8re") as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, "html.parser")
    print(soup)
    sousoup = soup.prettify()
    print(sousoup)

    for anchor in soup.find_all("p"):
        print(anchor.get_text())
    num2 = soup.find("div", {"class": "mw-parser-output"})
    for i in num2:
        if str(i)[:3]=="<p>":
            print(i.get_text())
            break
    a = soup.find_all("p")
    print(a, type(a))
    for i in range(10):
        p = a[i].get_text()
        print(f"#{p}#", i)
        pas_bon = [
            "Pages pour les éditeurs déconnectés en savoir plus",
            "Pour les articles homonymes,",
            "modifier - modifier le code",
            "Pour les articles ayant des titres homophones,",
            "Vous lisez un",
            " redirige ici. Pour ",
        ]
        n = 0
        for i in pas_bon:
            if i in p or p == "\n" or p in num2:
                n += 1
        if n == 0:
            print(f"#{p}#")
            break
        # input()
