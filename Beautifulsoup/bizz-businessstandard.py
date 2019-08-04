from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req4 = Request('https://www.business-standard.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage4 = urlopen(req4).read()
page_soup4 = soup(webpage4, "html.parser")
containers4 = page_soup4.find("div", {"class": "coutent-panel bs-new-top-story-image-block"})
containers41 = containers4.find("h1").text.strip()
print(containers41)