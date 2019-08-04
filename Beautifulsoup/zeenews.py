from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req5 = Request('https://zeenews.india.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage5 = urlopen(req5).read()
page_soup5 = soup(webpage5, "html.parser")
containers51 = page_soup5.find("div", {"class": "left-section"})
print(containers51.h1.text)
