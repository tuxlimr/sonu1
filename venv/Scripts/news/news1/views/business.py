from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import datetime
from ..models import News

def business(request):
    try:
        try:
            req1 = Request('https://economictimes.indiatimes.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage1 = urlopen(req1).read()
            page_soup1 = soup(webpage1, "html.parser")
            containers1 = page_soup1.find("section", {"id": "pageContent"})
            containers12 = containers1.h1.img.get("alt").strip()
        except:
            return HttpResponse("We are trying to pull info from Economic_times")

        try:
            req2 = Request('https://www.moneycontrol.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage2 = urlopen(req2).read()
            page_soup2 = soup(webpage2, "html.parser")
            containers2 = page_soup2.find("div", {"class": "sub-col-left"})
            containers21 = containers2.find("h1").text.strip()
        except:
            return HttpResponse("We are trying to pull info from Money Control")

        try:
            req3 = Request('https://www.livemint.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage3 = urlopen(req3).read()
            page_soup3 = soup(webpage3, "html.parser")
            containers3 = page_soup3.find("section", {"class": "cardHolder expandObject page-view-candidate"})
            containers31 = containers3.find("h1").text.strip()
        except:
            return HttpResponse("We are trying to pull info from Live_Mint ")

        try:
            req4 = Request('https://www.business-standard.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage4 = urlopen(req4).read()
            page_soup4 = soup(webpage4, "html.parser")
            containers4 = page_soup4.find("div", {"class": "coutent-panel bs-new-top-story-image-block"})
            containers41 = containers4.find("h1").text.strip()
        except:
            return HttpResponse("We are trying to pull info from Business Standard")

        return render(request, "business.html",
                      {"bizz_eco": containers12,
                       "bizz_money": containers21,
                       "bizz_livemint": containers31,
                       "bizz_business": containers41})
    except:
        return HttpResponse(" We are in the maintenance mode")







