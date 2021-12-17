from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('https://en.wikipedia.org/wiki/Union_between_Sweden_and_Norway') as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    for anchor in soup.find_all('p'):
        print(anchor.get_text())

