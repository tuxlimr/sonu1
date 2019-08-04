from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.theverge.com/tech', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "l-col__main"})
p = containers3.find("div",{"class":"c-entry-box--compact__body"})
print(p.h2.text)