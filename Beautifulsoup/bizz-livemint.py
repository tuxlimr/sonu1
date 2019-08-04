from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req3 = Request('https://www.livemint.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage3 = urlopen(req3).read()
page_soup3 = soup(webpage3, "html.parser")
containers3 = page_soup3.find("section", {"class": "cardHolder expandObject page-view-candidate"})
containers31 = containers3.find("h1").text.strip()
print(containers31)