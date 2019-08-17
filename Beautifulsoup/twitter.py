from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req2 = Request('https://trends24.in/india/', headers={'User-Agent': 'Mozilla/5.0'})
webpage2 = urlopen(req2).read()
page_soup2 = soup(webpage2, "html.parser")
containers2 = page_soup2.find("div", {"class": "trend-card"})
containers2 = page_soup2.find("ol", {"class": "trend-card__list"})
# print(containers2.prettify())
# print(containers2.title.name)
for link in containers2.find_all("a"):
    print(link.text)

