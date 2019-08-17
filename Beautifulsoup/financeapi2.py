from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import pandas as pd
name =[]
# value =[]
# change =[]

req4 = Request('https://www.moneycontrol.com/stocks/marketstats/bsegainer/index.php', headers={'User-Agent': 'Mozilla/5.0'})
webpage4 = urlopen(req4).read()
page_soup4 = soup(webpage4, "html.parser")
table = page_soup4.find('div', {"class": "brdmeet MT10"})
rows = table.find_all('tr')
for row in rows:
    print(row)
    # print(row.find_all('th').text)
    # value.append(str(row.find_all('td')[0].text))
    # change.append(str(row.find_all('td')[1].text))
