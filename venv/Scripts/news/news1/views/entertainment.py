from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import sys
sys.path.append("..")
from ..models import EntHeadlines
import threading


def entertainment(request):
                hover = EntHeadlines.objects.all()
                return render(request, "entertainment.html", {"pinkvilla": hover,
                                                              # "ent_firstpost": ent_firstpost,
                                                              # "ent_ibtimes": ent_ibtimes,
                                                              # "ent_ndtv": ent_ndtv,
                                                              # "ent_indiatoday": ent_indiatoday,
                                                              })
def r2():
        threading.Timer(900.0,r2).start()
        req1 = Request('https://www.firstpost.com/category/entertainment', headers={'User-Agent': 'Mozilla/5.0'})
        webpage1 = urlopen(req1).read()
        page_soup1 = soup(webpage1, "html.parser")
        containers1 = page_soup1.find("div", {"class": "main-content"})
        p1 = containers1.find("h2", {"class": "main-title"})
        p12 = p1.text.strip()
        req2 = Request('https://www.ibtimes.co.in/entertainment', headers={'User-Agent': 'Mozilla/5.0'})
        webpage2 = urlopen(req2).read()
        page_soup2 = soup(webpage2, "html.parser")
        containers2 = page_soup2.find("div", {"class": "area wrap-left"})
        p2 = containers2.find("h2", {"class": "headline-main"})
        p21 = p2.text.strip()
        req3 = Request('https://www.indiatoday.in/movies', headers={'User-Agent': 'Mozilla/5.0'})
        webpage3 = urlopen(req3).read()
        page_soup3 = soup(webpage3, "html.parser")
        containers3 = page_soup3.find("div", {"class": "col-md-8"})
        p31 = containers3.h2.text.strip()
        req4 = Request('https://www.ndtv.com/entertainment/', headers={'User-Agent': 'Mozilla/5.0'})
        webpage4 = urlopen(req4).read()
        page_soup4 = soup(webpage4, "html.parser")
        containers4 = page_soup4.find("div", {"class": "ins_left_rhs"})
        p4 = containers4.find("div", {"class": "nstory_header"})
        p41 = p4.text.strip()
        req5 = Request('https://www.pinkvilla.com/entertainment', headers={'User-Agent': 'Mozilla/5.0'})
        webpage5 = urlopen(req5).read()
        page_soup5 = soup(webpage5, "html.parser")
        containers5 = page_soup5.find("div", {"class": "view-content"})
        p5 = containers5.find("a", {"class": "section-title"})
        p51 = p5.text.strip()
        entheadlines_instance = EntHeadlines.objects.create(PinkVilla=p51, NDTV=p41, FirstPost=p12, IndiaToday=p31, IBTimes=p21)
        print("Data Sent")

r2()




