from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import time
req = Request('https://techcrunch.com/gadgets/', headers={'User-Agent': 'Mozilla/5.0'})
time.sleep(2)
webpage = urlopen(req).read()
time.sleep(2)
page_soup = soup(webpage, "html.parser")
time.sleep(2)
containers3 = page_soup.find("div", {"class": "content"})
time.sleep(2)
p = containers3.find("h2", {"class": "post-block__title"})
time.sleep(2)
print(containers3)

