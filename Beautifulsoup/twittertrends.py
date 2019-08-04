from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req5 = Request('https://twitter.com/search?q=%22%20%22', headers={'User-Agent': 'Mozilla/5.0'})
webpage5 = urlopen(req5).read()
page_soup5 = soup(webpage5, "html.parser")
containers51 = page_soup5.find("div", {"class": "flex-module-inner"})
# containers52 = containers51.find("li", {"class": "trend-item js-trend-item  context-trend-item"})
containers52 = containers51.find("data-trend-name".text)
print(containers52)
