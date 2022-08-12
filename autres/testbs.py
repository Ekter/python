from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen("https://lms.univ-cotedazur.fr/2021/course/view.php?id=13672&section=0#tabs-tree-start") as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, "html.parser")
    print(soup)
    sousoup = soup.prettify()
    print(sousoup)

    for anchor in soup.find_all("p"):
        print(anchor.get_text())
    num2 = soup.find("a", {"class": "aalink"})
    print(num2)
    for i in num2:
        print(i.get_text())
