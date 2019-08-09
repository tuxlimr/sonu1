from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import datetime
from.models import News
from .models import Blog


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

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


