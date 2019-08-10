from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req6 = Request('https://www.ndtv.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage6 = urlopen(req6).read()
page_soup6 = soup(webpage6, "html.parser")
containers6 = page_soup6.find("div", {"class": "lhs_col_two"})

if __name__ == "__main__":
    print(containers61.h1.text)
