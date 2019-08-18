# from bs4 import BeautifulSoup as soup
# from urllib.request import Request, urlopen
# req2 = Request('https://trends24.in/india/', headers={'User-Agent': 'Mozilla/5.0'})
# webpage2 = urlopen(req2).read()
# page_soup2 = soup(webpage2, "html.parser")
# containers2 = page_soup2.find("div", {"class": "trend-card"})
# containers2 = page_soup2.find("ol", {"class": "trend-card__list"})
# # print(containers2.prettify())
# # print(containers2.title.name)
# for link in containers2.find_all("a"):
#     print(link.text)
#

import urllib
import urllib.request
from bs4 import BeautifulSoup


theurl = "https://twitter.com/realDonaldTrump"
thepage = urllib.request.urlopen(theurl)


soup = BeautifulSoup(thepage, "html.parser")


print(soup.title.text)
# print(soup.findAll('a'))
## To get href links
# for link in soup.findAll('a'):
# print(link.get('href'))
# print(link.text)

## to get profile
##FindAll will give all metadata
## Find will give first header for same


print(soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)
i=1
for tweets in soup.findAll('div',{"class":"content"}):
    print (i, "." , str(tweets.find("p").text))
    i=i+1