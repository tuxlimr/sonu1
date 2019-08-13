from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import datetime
from ..models import News
from ..models import Blog


def index(request):
    try:
        try:
            req6 = Request('https://www.ndtv.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage6 = urlopen(req6).read()
            page_soup6 = soup(webpage6, "html.parser")
            containers6 = page_soup6.find("div", {"class": "lhs_col_two"})
            p6 = containers6.h1.text
            # news_instance = News.objects.create(news_headline=p6,newspaper = "NDTV")
        except:
            return HttpResponse("We are trying to pull info from NDTV Sources ")

        try:
            req5 = Request('https://timesofindia.indiatimes.com/home/headlines', headers={'User-Agent': 'Mozilla/5.0'})
            webpage5 = urlopen(req5).read()
            page_soup5 = soup(webpage5, "html.parser")
            containers5 = page_soup5.find("div", {"class": "top-newslist"})
            p51 = containers5.find("span", {"class": "w_tle"})
            p5 = p51.text
            # news_instance = News.objects.create(news_headline=p5, newspaper="Times Of India")
        except:
            return HttpResponse("We are trying to pull info from TOI Sources ")

        try:
            req4 = Request('https://scroll.in/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage4 = urlopen(req4).read()
            page_soup4 = soup(webpage4, "html.parser")
            containers4 = page_soup4.find("div", {"class": "featured-story column scroll-box scroll-box-3"})
            p41 = containers4.find("div", {"class": "row-story"})
            p4 = p41.h1.text
            # news_instance = News.objects.create(news_headline=p4, newspaper="Scroll")
        except:
            return HttpResponse("We are trying to pull info from Scroll Sources ")

        try:
            req1 = Request('https://www.hindustantimes.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage1 = urlopen(req1).read()
            page_soup1 = soup(webpage1, "html.parser")
            containers1 = page_soup1.find_all("div", {"class": "big-middlenews"})
            for container1 in containers1:
                Product_container1 = container1.find("div", {"class": "bigstory-h2"})
                Product_Name1 = Product_container1.text.strip()
                # news_instance = News.objects.create(news_headline=Product_Name1, newspaper="Hindustan Times")
        except:
            return HttpResponse("We are trying to pull info from Hindustan Times Sources ")

        try:
            req = Request('https://www.firstpost.com/', headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            page_soup = soup(webpage, "html.parser")
            containers = page_soup.find("div", {"class": "featured-news"})
            for container in containers:
                Product_container = container.find("div", {"class": "overlay-content"})
                Product_Name = Product_container.text.strip()
                # news_instance = News.objects.create(news_headline=Product_Name, newspaper="Firstpost")
        except:
            return HttpResponse("We are trying to pull info from Firstpost Sources ")

        try:
            req3 = Request('https://www.indiatoday.in/news.html', headers={'User-Agent': 'Mozilla/5.0'})
            webpage3 = urlopen(req3).read()
            page_soup3 = soup(webpage3, "html.parser")
            containers3 = page_soup3.find("div", {"class": "col-md-12 col-sm-12"})
            Product_Name3 = containers3.h3.text
            # news_instance = News.objects.create(news_headline=Product_Name3, newspaper="IndiaToday")
        except:
            return HttpResponse("We are trying to pull info from TOI Sources ")

        return render(request, "index.html",
                      {'firstpostnews': Product_Name,
                       'htnews': Product_Name1,
                       'itoday': Product_Name3,
                       'scroll': p4,
                       'TOI': p5,
                       'NDTV': p6})
    except:
        return HttpResponse("We are in the maintenance mode ")


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})




