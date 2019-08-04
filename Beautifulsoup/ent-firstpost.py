from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.firstpost.com/category/entertainment', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "main-content"})
p = containers3.find("h2", {"class": "main-title"})
print(p.text)