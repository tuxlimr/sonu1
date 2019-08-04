from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
# req = Request('https://www.firstpost.com/firstcricket/', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# page_soup = soup(webpage, "html.parser")
# containers13 = page_soup.find("div", {"class": "first-story"})
# print(containers13.h1.text)

req = Request('https://www.firstpost.com/firstcricket/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers12 = page_soup.find("div", {"class": "first-story"})
containers13 = containers12.h1.text
print(containers13)