from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import URLopener

manga="one-piece"
chapter=1
page=1
url = f"http://www.scan-fr.cc/manga/{manga}/{chapter}/{page}"
print(url)
with urlopen(url) as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    page = soup.find("img", {"class": "img-responsive scan-page"})
    print(page)
    print(page.get("src").strip().replace(" ", "%20"))