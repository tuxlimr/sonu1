from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req5 = Request('https://zeenews.india.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
webpage5 = urlopen(req5).read()
page_soup5 = soup(webpage5, "html.parser")
containers51 = page_soup5.find("div", {"class": "left-section"})
containers51 = containers51.h3.text