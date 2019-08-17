from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req2 = Request('https://www.moneycontrol.com/stocks/marketstats/bsegainer/index.php', headers={'User-Agent': 'Mozilla/5.0'})
webpage2 = urlopen(req2).read()
page_soup2 = soup(webpage2, "html.parser")
containers2 = page_soup2.find("div", {"class": "brdmeet MT10"})
containers21 = containers2.find("td", {"align": "right"})
data=[b.string for b in containers21.findAll('b')]
print("Sensex rates today" +" "+ data[0])
