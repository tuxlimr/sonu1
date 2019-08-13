from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from ..models import News


def sports(request):
    try:
        try:
            req = Request('https://www.firstpost.com/firstcricket/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            page_soup = soup(webpage, "html.parser")
            containers12 = page_soup.find("div", {"class": "first-story"})
            containers13 = containers12.h1.text.strip()
            # news_instance = News.objects.create(news_headline=containers13, newspaper="Sports-Firstpost")
        except:
            return HttpResponse("We are trying to pull info from Sports-Firstpost Sources ")

        try:
            req2 = Request('https://timesofindia.indiatimes.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
            webpage2 = urlopen(req2).read()
            page_soup2 = soup(webpage2, "html.parser")
            containers21 = page_soup2.find("div", {"class": "top-section"})
            containers22 = containers21.find("span", {"class": "w_tle"})
            containers23 = containers22.find('a').get("title")
            # news_instance = News.objects.create(news_headline=containers23, newspaper="Sports-TOI")
        except:
            return HttpResponse("We are trying to pull info from Sports-TOI Sources ")

        try:
            req3 = Request('https://www.espncricinfo.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage3 = urlopen(req3).read()
            page_soup31 = soup(webpage3, "html.parser")
            containers32 = page_soup31.find("div", {"class": "contentItem__titleWrapper"})
            containers33 = containers32.h1.text.strip()
            # news_instance = News.objects.create(news_headline=containers33, newspaper="Sports-Cricinfo")
        except:
            return HttpResponse("We are trying to pull info from Sports-Cricinfo Sources ")

        try:
            req4 = Request('https://www.cricbuzz.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage4 = urlopen(req4).read()
            page_soup4 = soup(webpage4, "html.parser")
            containers41 = page_soup4.find("div", {"class": "big-crd-main cb-bg-white"})
            containers42 = containers41.h2.text.strip()
            # news_instance = News.objects.create(news_headline=containers42, newspaper="Sports-Cricbuzz")
        except:
            return HttpResponse("We are trying to pull info from Sports-Cricbuzz Sources ")

        try:
            req5 = Request('https://zeenews.india.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
            webpage5 = urlopen(req5).read()
            page_soup5 = soup(webpage5, "html.parser")
            containers51 = page_soup5.find("div", {"class": "left-section"})
            containers52 = containers51.h3.text.strip()
            # news_instance = News.objects.create(news_headline=containers52, newspaper="Sports-ZeeNews")

        except:
            return HttpResponse("We are trying to pull info from Sports-ZeeNews Sources ")

        return render(request, "sports.html",
                      {'sports_firstpost': containers13,
                       'sports_toi': containers23,
                       'espn': containers33,
                       'cricbuzz': containers42,
                       'sports_zee': containers52,
                       })
    except:
        return HttpResponse(" We are in the maintenance mode ")


