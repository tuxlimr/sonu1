from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://gadgets.ndtv.com/news', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "story_list row margin_b30"})
p = containers3.find("span",{"class":"news_listing"})
print(p.text)