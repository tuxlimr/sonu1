from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req1 = Request('https://economictimes.indiatimes.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage1 = urlopen(req1).read()
page_soup1 = soup(webpage1, "html.parser")
containers1 = page_soup1.find("section", {"id": "pageContent"})
print(containers1.h1.img.get("alt").strip())