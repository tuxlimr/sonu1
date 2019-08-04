from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.ndtv.com/entertainment/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "ins_left_rhs"})
p = containers3.find("div",{"class":"nstory_header"})
print(p.text)