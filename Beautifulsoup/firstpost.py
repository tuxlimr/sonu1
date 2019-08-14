from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.firstpost.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "main"})
containers4 = containers3.find("div", {"class": "news-item"})
print(containers4.h1.text)