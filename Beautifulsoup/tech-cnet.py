from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req5 = Request('https://www.cnet.com/news/', headers={'User-Agent': 'Mozilla/5.0'})
webpage5 = urlopen(req5).read()
page_soup5 = soup(webpage5, "html.parser")
containers51 = page_soup5.find("div", {"class": "col-12"})
p52 = containers51.find("div", {"section": "topStories|item-1"})
print(p52.h3.text)