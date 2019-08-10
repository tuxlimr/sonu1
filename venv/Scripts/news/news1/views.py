from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import datetime
from.models import News
from .models import Blog
import requests
import json
cuurency_url = requests.get('https://api.ratesapi.io/api/latest')
cuurency_url_2015 = requests.get('https://api.ratesapi.io/api/2015-01-1')
cuurency_url_2010 = requests.get('https://api.ratesapi.io/api/2010-01-1')

# def index(request):
#     # news_instance = News.objects.create(news_headline='text',newspaper = "NDTV")
#     return render(request, "index.html")


def index(request):

    try:
        try:
                req6 = Request('https://www.ndtv.com/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage6 = urlopen(req6).read()
                page_soup6 = soup(webpage6, "html.parser")
                containers6 = page_soup6.find("div", {"class": "lhs_col_two"})
                p6 = containers6.h1.text
                # news_instance = News.objects.create(news_headline=p6,newspaper = "NDTV")
        except: return HttpResponse("We are trying to pull info from NDTV Sources ")

        try:
                req5 = Request('https://timesofindia.indiatimes.com/home/headlines', headers={'User-Agent': 'Mozilla/5.0'})
                webpage5 = urlopen(req5).read()
                page_soup5 = soup(webpage5, "html.parser")
                containers5 = page_soup5.find("div", {"class": "top-newslist"})
                p51 = containers5.find("span", {"class": "w_tle"})
                p5 = p51.text
                # news_instance = News.objects.create(news_headline=p5, newspaper="Times Of India")
        except: return HttpResponse("We are trying to pull info from TOI Sources ")

        try:
                req4 = Request('https://scroll.in/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage4 = urlopen(req4).read()
                page_soup4 = soup(webpage4, "html.parser")
                containers4 = page_soup4.find("div", {"class": "featured-story column scroll-box scroll-box-3"})
                p41 = containers4.find("div", {"class": "row-story"})
                p4 = p41.h1.text
                # news_instance = News.objects.create(news_headline=p4, newspaper="Scroll")
        except: return HttpResponse("We are trying to pull info from Scroll Sources ")

        try:
                req1 = Request('https://www.hindustantimes.com/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage1 = urlopen(req1).read()
                page_soup1 = soup(webpage1, "html.parser")
                containers1 = page_soup1.find_all("div", {"class": "big-middlenews"})
                for container1 in containers1:
                    Product_container1 = container1.find("div", {"class": "bigstory-h2"})
                    Product_Name1 = Product_container1.text.strip()
                    # news_instance = News.objects.create(news_headline=Product_Name1, newspaper="Hindustan Times")
        except: return HttpResponse("We are trying to pull info from Hindustan Times Sources ")

        try:
                    req = Request('https://www.firstpost.com/', headers={'User-Agent': 'Mozilla/5.0'})
                    webpage = urlopen(req).read()
                    page_soup = soup(webpage, "html.parser")
                    containers = page_soup.find("div", {"class": "featured-news"})
                    for container in containers:
                        Product_container = container.find("div", {"class": "overlay-content"})
                        Product_Name = Product_container.text.strip()
                        # news_instance = News.objects.create(news_headline=Product_Name, newspaper="Firstpost")
        except: return HttpResponse("We are trying to pull info from Firstpost Sources ")

        try:
                    req3 = Request('https://www.indiatoday.in/news.html', headers={'User-Agent': 'Mozilla/5.0'})
                    webpage3 = urlopen(req3).read()
                    page_soup3 = soup(webpage3, "html.parser")
                    containers3 = page_soup3.find("div", {"class": "col-md-12 col-sm-12"})
                    Product_Name3 = containers3.h3.text
                    # news_instance = News.objects.create(news_headline=Product_Name3, newspaper="IndiaToday")
        except:return HttpResponse("We are trying to pull info from TOI Sources ")

        return render(request, "index.html",
                                  {'firstpostnews':Product_Name,
                                  'htnews':Product_Name1,
                                  'itoday':Product_Name3,
                                  'scroll': p4,
                                  'TOI': p5,
                                  'NDTV': p6})
    except: return HttpResponse("We are in the maintenance mode ")

def sports(request):
    try:
            try:
                req = Request('https://www.firstpost.com/firstcricket/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
                page_soup = soup(webpage, "html.parser")
                containers12 = page_soup.find("div", {"class": "first-story"})
                containers13 = containers12.h1.text.strip()
                # news_instance = News.objects.create(news_headline=containers13, newspaper="Sports-Firstpost")
            except: return HttpResponse("We are trying to pull info from Sports-Firstpost Sources ")

            try:
                req2 = Request('https://timesofindia.indiatimes.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
                webpage2 = urlopen(req2).read()
                page_soup2 = soup(webpage2, "html.parser")
                containers21 = page_soup2.find("div", {"class": "top-section"})
                containers22 = containers21.find("span", {"class": "w_tle"})
                containers23 = containers22.find('a').get("title")
                # news_instance = News.objects.create(news_headline=containers23, newspaper="Sports-TOI")
            except: return HttpResponse("We are trying to pull info from Sports-TOI Sources ")


            try:
                req3 = Request('https://www.espncricinfo.com/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage3 = urlopen(req3).read()
                page_soup31 = soup(webpage3, "html.parser")
                containers32 = page_soup31.find("div", {"class": "contentItem__titleWrapper"})
                containers33 = containers32.h1.text.strip()
                # news_instance = News.objects.create(news_headline=containers33, newspaper="Sports-Cricinfo")
            except:return HttpResponse("We are trying to pull info from Sports-Cricinfo Sources ")

            try:
                req4 = Request('https://www.cricbuzz.com/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage4 = urlopen(req4).read()
                page_soup4 = soup(webpage4, "html.parser")
                containers41 = page_soup4.find("div", {"class": "big-crd-main cb-bg-white"})
                containers42 = containers41.h2.text.strip()
                # news_instance = News.objects.create(news_headline=containers42, newspaper="Sports-Cricbuzz")
            except:return HttpResponse("We are trying to pull info from Sports-Cricbuzz Sources ")

            try:
                req5 = Request('https://zeenews.india.com/sports', headers={'User-Agent': 'Mozilla/5.0'})
                webpage5 = urlopen(req5).read()
                page_soup5 = soup(webpage5, "html.parser")
                containers51 = page_soup5.find("div", {"class": "left-section"})
                containers52 = containers51.h3.text.strip()
                # news_instance = News.objects.create(news_headline=containers52, newspaper="Sports-ZeeNews")

            except: return HttpResponse("We are trying to pull info from Sports-ZeeNews Sources ")

            return render(request, "sports.html",
                          {'sports_firstpost': containers13,
                           'sports_toi': containers23,
                           'espn': containers33,
                           'cricbuzz': containers42,
                           'sports_zee': containers52,
                           })
    except: return HttpResponse(" We are in the maintenance mode ")

def technology(request):
    try:
            try:
                req1 = Request('https://www.91mobiles.com/hub/category/news-2/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage1 = urlopen(req1).read()
                page_soup1 = soup(webpage1, "html.parser")
                containers1 = page_soup1.find("div", {"class": "td-module-thumb img_height"})
                p1 = containers1.find("img", {"class": "entry-thumb lazyload"})
                p11 = p1.get("title")
                # news_instance = News.objects.create(news_headline=p11, newspaper="Tech-91mobiles")

            except: return HttpResponse("We are trying to pull info from Tech-91mobiles ")

            try:
                req5 = Request('https://www.cnet.com/news/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage5 = urlopen(req5).read()
                page_soup5 = soup(webpage5, "html.parser")
                containers51 = page_soup5.find("div", {"class": "col-12"})
                p52 = containers51.find("div", {"section": "topStories|item-1"})
                p53 = p52.h3.text.strip()
                # news_instance = News.objects.create(news_headline=p53, newspaper="Tech-CNET")

            except: return HttpResponse("We are trying to pull info from Tech-CNET ")

            try:   
                req2 = Request('https://gadgets.ndtv.com/news', headers={'User-Agent': 'Mozilla/5.0'})
                webpage2 = urlopen(req2).read()
                page_soup2 = soup(webpage2, "html.parser")
                containers2 = page_soup2.find("div", {"class": "story_list row margin_b30"})
                p21 = containers2.find("span", {"class": "news_listing"})
                p22 = p21.text.strip()
                # news_instance = News.objects.create(news_headline=p22, newspaper="Tech-NDTVgadgets")

            except: return HttpResponse("We are trying to pull info from Tech-NDTVgadgets ")

            try:
                req4 = Request('https://www.theverge.com/tech', headers={'User-Agent': 'Mozilla/5.0'})
                webpage4 = urlopen(req4).read()
                page_soup4 = soup(webpage4, "html.parser")
                containers4 = page_soup4.find("div", {"class": "l-col__main"})
                p4 = containers4.find("div", {"class": "c-entry-box--compact__body"})
                p41 = p4.h2.text.strip()
                # news_instance = News.objects.create(news_headline=p41, newspaper="Tech-Verge")

            except: return HttpResponse("We are trying to pull info from Tech-Verge ")

            try:
                req3 = Request('https://www.techradar.com/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage3 = urlopen(req3).read()
                page_soup3 = soup(webpage3, "html.parser")
                containers3 = page_soup3.find("div", {"id": "Item1"})
                p3 = containers3.find("figure", {"class": "feature-block-item"})
                p31 = p3.find("span", {"class": "article-name"}).text.strip()
                # news_instance = News.objects.create(news_headline=p31, newspaper="Tech-Techradar")
            except: return HttpResponse("We are trying to pull info from Tech-Techradar ")


            return render(request, "technology.html",
             {'91mobiles': p11, 
                'tech_cnet': p53,
                'tech_ndtv': p22,
                'tech_verge': p41,
                'techradar' : p31
                })
    except:return HttpResponse(" We are in the maintenance mode ")


def entertainment(request):
    try:
            try:
                req1 = Request('https://www.firstpost.com/category/entertainment', headers={'User-Agent': 'Mozilla/5.0'})
                webpage1 = urlopen(req1).read()
                page_soup1 = soup(webpage1, "html.parser")
                containers1 = page_soup1.find("div", {"class": "main-content"})
                p1 = containers1.find("h2", {"class": "main-title"})
                p12 = p1.text.strip()
                # news_instance = News.objects.create(news_headline=p12, newspaper="Ent_firstpost")
            except: return HttpResponse("We are trying to pull info from firstpost")

            try:
                req2 = Request('https://www.ibtimes.co.in/entertainment', headers={'User-Agent': 'Mozilla/5.0'})
                webpage2 = urlopen(req2).read()
                page_soup2 = soup(webpage2, "html.parser")
                containers2 = page_soup2.find("div", {"class": "area wrap-left"})
                p2 = containers2.find("h2", {"class": "headline-main"})
                p21 = p2.text.strip()
                # news_instance = News.objects.create(news_headline=p21, newspaper="Ent_IBTimes")
            except: return HttpResponse("We are trying to pull info from IBTimes ")

            try:
                req3 = Request('https://www.indiatoday.in/movies', headers={'User-Agent': 'Mozilla/5.0'})
                webpage3 = urlopen(req3).read()
                page_soup3 = soup(webpage3, "html.parser")
                containers3 = page_soup3.find("div", {"class": "col-md-8"})
                p31 = containers3.h2.text.strip()
                # news_instance = News.objects.create(news_headline=p31, newspaper="Ent_Indiatoday")
            except: return HttpResponse("We are trying to pull info from Indiatoday ")

            try:
                req4 = Request('https://www.ndtv.com/entertainment/', headers={'User-Agent': 'Mozilla/5.0'})
                webpage4 = urlopen(req4).read()
                page_soup4 = soup(webpage4, "html.parser")
                containers4 = page_soup4.find("div", {"class": "ins_left_rhs"})
                p4 = containers4.find("div", {"class": "nstory_header"})
                p41 = p4.text.strip()
                # news_instance = News.objects.create(news_headline= p41, newspaper="Ent_NDTV")
            except: return HttpResponse("We are trying to pull info from NDTV ")

            try:
                req5 = Request('https://www.pinkvilla.com/entertainment', headers={'User-Agent': 'Mozilla/5.0'})
                webpage5 = urlopen(req5).read()
                page_soup5 = soup(webpage5, "html.parser")
                containers5 = page_soup5.find("div", {"class": "view-content"})
                p5 = containers5.find("a", {"class": "section-title"})
                p51 = p5.text.strip()
                # news_instance = News.objects.create(news_headline=p51, newspaper="Ent_pinkvilla")
            except: return HttpResponse("We are trying to pull info from pinkvilla ")

                
            return render(request, "entertainment.html",
                              {"ent_firstpost": p12,
                                "ent_ibtimes": p21,
                                "ent_indiatoday": p31,
                                "ent_ndtv": p41,
                                "ent_pinkvilla": p51})
    except:return HttpResponse(" We are in the maintenance mode")

def business(request):
    try:
        try:
            req1 = Request('https://economictimes.indiatimes.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage1 = urlopen(req1).read()
            page_soup1 = soup(webpage1, "html.parser")
            containers1 = page_soup1.find("section", {"id": "pageContent"})
            containers12 = containers1.h1.img.get("alt").strip()
        except: return HttpResponse("We are trying to pull info from Economic_times")

        try:
            req2 = Request('https://www.moneycontrol.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage2 = urlopen(req2).read()
            page_soup2 = soup(webpage2, "html.parser")
            containers2 = page_soup2.find("div", {"class": "sub-col-left"})
            containers21 = containers2.find("h1").text.strip()
        except: return HttpResponse("We are trying to pull info from Money Control")

        try:
            req3 = Request('https://www.livemint.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage3 = urlopen(req3).read()
            page_soup3 = soup(webpage3, "html.parser")
            containers3 = page_soup3.find("section", {"class": "cardHolder expandObject page-view-candidate"})
            containers31 = containers3.find("h1").text.strip()
        except: return HttpResponse("We are trying to pull info from Live_Mint ")

        try:
            req4 = Request('https://www.business-standard.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage4 = urlopen(req4).read()
            page_soup4 = soup(webpage4, "html.parser")
            containers4 = page_soup4.find("div", {"class": "coutent-panel bs-new-top-story-image-block"})
            containers41 = containers4.find("h1").text.strip()
        except: return HttpResponse("We are trying to pull info from Business Standard")

        return render(request, "business.html",
                      {"bizz_eco": containers12,
                       "bizz_money": containers21,
                       "bizz_livemint": containers31,
                       "bizz_business": containers41})
    except:return HttpResponse(" We are in the maintenance mode")

def currency(request):
    try:

        currency = json.loads(cuurency_url.text)
        currency_2015 = json.loads(cuurency_url_2015.text)
        currency_2010 = json.loads(cuurency_url_2010.text)
        GBP = str(currency['rates']['GBP'])
        HKD = str(currency['rates']['HKD'])
        INR = str(currency['rates']['INR'])
        SGD = str(currency['rates']['SGD'])
        CNY = str(currency['rates']['CNY'])
        USD = str(currency['rates']['USD'])
        AUD = str(currency['rates']['AUD'])
        CAD = str(currency['rates']['CAD'])
        MYR = str(currency['rates']['MYR'])
        BGN = str(currency['rates']['BGN'])
        THB = str(currency['rates']['THB'])
        PHP = str(currency['rates']['PHP'])
        RUB = str(currency['rates']['RUB'])
        GBP_2015 = str(currency_2015['rates']['GBP'])
        INR_2015 = str(currency_2015['rates']['INR'])
        SGD_2015 = str(currency_2015['rates']['SGD'])
        USD_2015 = str(currency_2015['rates']['USD'])
        AUD_2015 = str(currency_2015['rates']['AUD'])
        CAD_2015 = str(currency_2015['rates']['CAD'])
        RUB_2015 = str(currency_2015['rates']['RUB'])
        GBP_2010 = str(currency_2010['rates']['GBP'])
        INR_2010 = str(currency_2010['rates']['INR'])
        SGD_2010 = str(currency_2010['rates']['SGD'])
        USD_2010 = str(currency_2010['rates']['USD'])
        AUD_2010 = str(currency_2010['rates']['AUD'])
        CAD_2010 = str(currency_2010['rates']['CAD'])
        RUB_2010 = str(currency_2010['rates']['RUB'])

        INR_USD = round((1 / float(INR) * float(USD)), 4)
        INR_GBP = round((1 / float(INR) * float(GBP)), 4)
        INR_HKD = round((1 / float(INR) * float(HKD)), 4)
        INR_SGD = round((1 / float(INR) * float(SGD)), 4)
        INR_AUD = round((1 / float(INR) * float(AUD)), 4)
        INR_CAD = round((1 / float(INR) * float(CAD)), 4)
        INR_RUB = round((1 / float(INR) * float(RUB)), 4)
        INR_USD_2010 = round((1 / float(INR_2010) * float(USD_2010)), 4)
        INR_GBP_2010 = round((1 / float(INR_2010) * float(GBP_2010)), 4)
        INR_SGD_2010 = round((1 / float(INR_2010) * float(SGD_2010)), 4)
        INR_AUD_2010 = round((1 / float(INR_2010) * float(AUD_2010)), 4)
        INR_CAD_2010 = round((1 / float(INR_2010) * float(CAD_2010)), 4)
        INR_RUB_2010 = round((1 / float(INR_2010) * float(RUB_2010)), 4)
        INR_USD_2015 = round((1 / float(INR_2015) * float(USD_2015)), 4)
        INR_GBP_2015 = round((1 / float(INR_2015) * float(GBP_2015)), 4)
        INR_SGD_2015 = round((1 / float(INR_2015) * float(SGD_2015)), 4)
        INR_AUD_2015 = round((1 / float(INR_2015) * float(AUD_2015)), 4)
        INR_CAD_2015 = round((1 / float(INR_2015) * float(CAD_2015)), 4)
        INR_RUB_2015 = round((1 / float(INR_2015) * float(RUB_2015)), 4)

        USD_INR = round((1 / float(USD) * float(INR)), 4)
        USD_USD = round((1 / float(USD) * float(USD)), 4)
        USD_GBP = round((1 / float(USD) * float(GBP)), 4)
        USD_SGD = round((1 / float(USD) * float(SGD)), 4)
        USD_AUD = round((1 / float(USD) * float(AUD)), 4)
        USD_CAD = round((1 / float(USD) * float(CAD)), 4)
        USD_RUB = round((1 / float(USD) * float(RUB)), 4)
        USD_INR_2015 = round((1 / float(USD_2015) * float(INR_2015)), 4)
        USD_USD_2015 = round((1 / float(USD_2015) * float(USD_2015)), 4)
        USD_GBP_2015 = round((1 / float(USD_2015) * float(GBP_2015)), 4)
        USD_SGD_2015 = round((1 / float(USD_2015) * float(SGD_2015)), 4)
        USD_AUD_2015 = round((1 / float(USD_2015) * float(AUD_2015)), 4)
        USD_CAD_2015 = round((1 / float(USD_2015) * float(CAD_2015)), 4)
        USD_RUB_2015 = round((1 / float(USD_2015) * float(RUB_2015)), 4)
        USD_INR_2010 = round((1 / float(USD_2010) * float(INR_2010)), 4)
        USD_USD_2010 = round((1 / float(USD_2010) * float(USD_2010)), 4)
        USD_GBP_2010 = round((1 / float(USD_2010) * float(GBP_2010)), 4)
        USD_SGD_2010 = round((1 / float(USD_2010) * float(SGD_2010)), 4)
        USD_AUD_2010 = round((1 / float(USD_2010) * float(AUD_2010)), 4)
        USD_CAD_2010 = round((1 / float(USD_2010) * float(CAD_2010)), 4)
        USD_RUB_2010 = round((1 / float(USD_2010) * float(RUB_2010)), 4)


        return render(request, 'currency.html',
                      {'GBP': GBP, "HKD" : HKD, "INR": INR, "SGD": SGD, "CNY": CNY, "USD": USD, "AUD": AUD, "CAD": CAD,"MYR": MYR,
                        "BGN": BGN, "THB": THB, "PHP": PHP, "RUB": RUB,  "INR_USD": INR_USD,
                       "INR_GBP": INR_GBP, "INR_SGD": INR_SGD, "INR_AUD": INR_AUD, "INR_CAD": INR_CAD, "INR_RUB": INR_RUB,
                       "USD_INR": USD_INR, "USD_USD": USD_USD, "USD_GBP": USD_GBP,"USD_SGD": USD_SGD,"USD_AUD":USD_AUD, "USD_CAD": USD_CAD, "USD_RUB": USD_RUB,

                       'GBP_2010': GBP_2010,  "INR_2010": INR_2010, "SGD_2010": SGD_2010
                        , "USD_2010": USD_2010, "AUD_2010": AUD_2010, "CAD_2010": CAD_2010,
                         "RUB_2010": RUB_2010, "INR_USD_2010": INR_USD_2010,"INR_GBP_2010": INR_GBP_2010, "INR_SGD_2010": INR_SGD_2010, "INR_AUD_2010": INR_AUD_2010,
                        "INR_CAD_2010": INR_CAD_2010, "INR_RUB_2010": INR_RUB_2010, "USD_INR_2010": USD_INR_2010, "USD_USD_2010": USD_USD_2010, "USD_GBP_2010": USD_GBP_2010,
                        "USD_SGD_2010": USD_SGD_2010, "USD_AUD_2010": USD_AUD_2010, "USD_CAD_2010": USD_CAD_2010,
                        "USD_RUB_2010": USD_RUB_2010,

                       'GBP_2015': GBP_2015,  "INR_2015": INR_2015, "SGD_2015": SGD_2015,
                         "USD_2015": USD_2015, "AUD_2015": AUD_2015, "CAD_2015": CAD_2015,
                         "RUB_2015": RUB_2015, "INR_USD_2015": INR_USD_2015,
                        "INR_GBP_2015": INR_GBP_2015, "INR_SGD_2015": INR_SGD_2015, "INR_AUD_2015": INR_AUD_2015,
                        "INR_CAD_2015": INR_CAD_2015, "INR_RUB_2015": INR_RUB_2015, "USD_INR_2015": USD_INR_2015,
                        "USD_USD_2015": USD_USD_2015, "USD_GBP_2015": USD_GBP_2015,
                        "USD_SGD_2015": USD_SGD_2015, "USD_AUD_2015": USD_AUD_2015, "USD_CAD_2015": USD_CAD_2015,
                        "USD_RUB_2015": USD_RUB_2015,
                       })

    except: return HttpResponse(" We are trying to fetch currency rates")

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})




