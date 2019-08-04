from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.indiatoday.in/movies', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "col-md-8"})
# p = containers3.find("div", {"class": "featured-post featured-post-first "})
print(containers3.h2.text)