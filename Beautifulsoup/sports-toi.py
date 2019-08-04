from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://timesofindia.indiatimes.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "top-section"})
containers4 = page_soup.find("span", {"class": "w_tle"})
print(containers4.find('a').get("title"))


req2 = Request('https://timesofindia.indiatimes.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
webpage2 = urlopen(req2).read()
page_soup2 = soup(webpage2, "html.parser")
containers21 = page_soup2.find("div", {"class": "top-section"})
containers22 = containers21.find("span", {"class": "w_tle"})
containers23 = containers22.find('a').get("title")
print(containers23)
