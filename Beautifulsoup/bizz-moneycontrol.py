from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req2 = Request('https://www.moneycontrol.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage2 = urlopen(req2).read()
page_soup2 = soup(webpage2, "html.parser")
containers2 = page_soup2.find("div", {"class": "sub-col-left"})
containers21 = containers2.find("h1").text.strip()
print(containers21)