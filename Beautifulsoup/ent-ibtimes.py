from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.ibtimes.co.in/entertainment', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "area wrap-left"})
p = containers3.find("h2", {"class": "headline-main"})
print(p.text.strip())