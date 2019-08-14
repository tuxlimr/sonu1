from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import sys
sys.path.append("..")
from ..models import BusinessHeadlines
import threading

def business(request):
    x = len(BusinessHeadlines.objects.all())
    hover = BusinessHeadlines.objects.values('EconomicTimes')[(x - 1):x]
    hover1 = BusinessHeadlines.objects.values('MoneyControl')[(x - 1):x]
    hover2 = BusinessHeadlines.objects.values('LiveMint')[(x - 1):x]
    hover3 = BusinessHeadlines.objects.values('BusinessStandard')[(x - 1):x]
    return render(request, "business.html", {"bizz_eco": hover,
                                             "bizz_money": hover1,
                                             "bizz_livemint": hover2,
                                             "bizz_business": hover3
                                             })

def r2():
    threading.Timer(900.0, r2).start()
    req1 = Request('https://economictimes.indiatimes.com/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage1 = urlopen(req1).read()
    page_soup1 = soup(webpage1, "html.parser")
    containers1 = page_soup1.find("section", {"id": "pageContent"})
    c12 = containers1.h1.img.get("alt").strip()

    req2 = Request('https://www.moneycontrol.com/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage2 = urlopen(req2).read()
    page_soup2 = soup(webpage2, "html.parser")
    containers2 = page_soup2.find("div", {"class": "sub-col-left"})
    c21 = containers2.find("h1").text.strip()

    req3 = Request('https://www.livemint.com/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage3 = urlopen(req3).read()
    page_soup3 = soup(webpage3, "html.parser")
    containers3 = page_soup3.find("section", {"class": "cardHolder expandObject page-view-candidate"})
    c31 = containers3.find("h1").text.strip()

    req4 = Request('https://www.business-standard.com/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage4 = urlopen(req4).read()
    page_soup4 = soup(webpage4, "html.parser")
    containers4 = page_soup4.find("div", {"class": "coutent-panel bs-new-top-story-image-block"})
    c41 = containers4.find("h1").text.strip()
    businessheadlines_instance = BusinessHeadlines.objects.create(EconomicTimes=c12,
                                                                  MoneyControl=c21,
                                                                  LiveMint=c31,
                                                                  BusinessStandard=c41
                                                                  )
r2()






