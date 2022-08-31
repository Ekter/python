from bs4 import BeautifulSoup
from urllib.request import urlopen


# manga="one-piece"
# chapter=1
# page=1
# url = f"http://www.scan-fr.cc/manga/{manga}/{chapter}/{page}"
# print(url)
# with urlopen(url) as response:
#     webpage = response.read()
#     soup = BeautifulSoup(webpage, 'html.parser')
#     page = soup.find("img", {"class": "img-responsive scan-page"})
#     print(page)
#     print(page.get("src").strip().replace(" ", "%20"))

def extract_img(file, chap, page):
    # with urlopen(f"http://www.scan-fr.cc/manga/one-piece/{chap}/{page}") as response:
    with urlopen(f"http://www.scan-fr.cc/manga/one-piece/22/{page+1}") as response:
        print(f"http://www.scan-fr.cc/manga/one-piece/{chap}/{page}")
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        img = soup.find("img", {"class": "img-responsive scan-page"})
        print(img)
        res=img.get("src").strip().replace(" ", "%20")
        print(res)
        file.write(res+"\n")
        file.flush()

with open("links.txt","w") as file:
    try:
        chap=1
        while chap<1000:
            page = 65
            try:
                while True:
                    extract_img(file, chap, page)
                    page+=1
                    print(page)
            except Exception as e:
                page=1
                chap+=1
                print(chap)
    except KeyboardInterrupt:
        print("ok")
        file.close()
        exit()
