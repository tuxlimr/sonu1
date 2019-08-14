from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from ..models import SportsHeadlines
import threading
import sys
sys.path.append("..")

def sports(request):
    x = len(SportsHeadlines.objects.all())
    hover = SportsHeadlines.objects.values('FirstPost')[(x - 1):x]
    hover1 = SportsHeadlines.objects.values('Toi')[(x - 1):x]
    hover2 = SportsHeadlines.objects.values('ESPN')[(x - 1):x]
    hover3 = SportsHeadlines.objects.values('Cricbuzz')[(x - 1):x]
    hover4 = SportsHeadlines.objects.values('ZeeSports')[(x - 1):x]
    return render(request, "sports.html", {"sports_firstpost": hover,
                                                  "sports_toi": hover1,
                                                  "espn": hover2,
                                                  "cricbuzz": hover3,
                                                  "sports_zee": hover4,
                                                  })
def r2():
    threading.Timer(900.0, r2).start()
    req = Request('https://www.firstpost.com/firstcricket/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    containers12 = page_soup.find("div", {"class": "first-story"})
    p13 = containers12.h1.text.strip()

    req2 = Request('https://timesofindia.indiatimes.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
    webpage2 = urlopen(req2).read()
    page_soup2 = soup(webpage2, "html.parser")
    containers21 = page_soup2.find("div", {"class": "top-section"})
    containers22 = containers21.find("span", {"class": "w_tle"})
    p23 = containers22.find('a').get("title")

    req3 = Request('https://www.espncricinfo.com/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage3 = urlopen(req3).read()
    page_soup31 = soup(webpage3, "html.parser")
    containers32 = page_soup31.find("div", {"class": "contentItem__titleWrapper"})
    p33 = containers32.h1.text.strip()

    req4 = Request('https://www.cricbuzz.com/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage4 = urlopen(req4).read()
    page_soup4 = soup(webpage4, "html.parser")
    containers41 = page_soup4.find("div", {"class": "big-crd-main cb-bg-white"})
    p42 = containers41.h2.text.strip()

    req5 = Request('https://zeenews.india.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
    webpage5 = urlopen(req5).read()
    page_soup5 = soup(webpage5, "html.parser")
    containers51 = page_soup5.find("div", {"class": "left-section"})
    p52 = containers51.h3.text.strip()
    sportsheadlines_instance = SportsHeadlines.objects.create(FirstPost=p13, Toi=p23, ESPN=p33, Cricbuzz=p42,
                                                        ZeeSports=p52)
r2()



