# from django.shortcuts import render
# from django.shortcuts import HttpResponse
# from bs4 import BeautifulSoup as soup
# from urllib.request import Request, urlopen
# import sys
# sys.path.append("..")
# from ..models import TechnologyHeadlines
# import threading
#
# def technology(request):
#         tech_mobiles91 = TechnologyHeadlines.objects.all()
#         tech_mobiles91 = TechnologyHeadlines.objects.all()[len(tech_mobiles91) - 1:]
#         # tech_cnet = TechnologyHeadlines.objects.all()
#         # tech_cnet = TechnologyHeadlines.objects.all()[len(tech_cnet) - 1:]
#         # tech_ndtv = TechnologyHeadlines.objects.all()
#         # tech_ndtv = TechnologyHeadlines.objects.all()[len(tech_ndtv) - 1:]
#         # tech_verge = TechnologyHeadlines.objects.all()
#         # tech_verge = TechnologyHeadlines.objects.all()[len(tech_verge) - 1:]
#         # techradar = TechnologyHeadlines.objects.all()
#         # techradar = TechnologyHeadlines.objects.all()[len(techradar) - 1:]
#
#         return render(request, "technology.html",
#                       {'91mobiles': tech_mobiles91,
#                        # 'tech_cnet': tech_cnet,
#                        # 'tech_ndtv': tech_ndtv,
#                        # 'tech_verge': tech_verge,
#                        # 'techradar': techradar
#                        })
#
# def r2():
#         threading.Timer(900.0,r2).start()
#         req1 = Request('https://www.91mobiles.com/hub/category/news-2/', headers={'User-Agent': 'Mozilla/5.0'})
#         webpage1 = urlopen(req1).read()
#         page_soup1 = soup(webpage1, "html.parser")
#         containers1 = page_soup1.find("div", {"class": "td-module-thumb img_height"})
#         p1 = containers1.find("img", {"class": "entry-thumb lazyload"})
#         p11 = p1.get("title")
#
#         req5 = Request('https://www.cnet.com/news/', headers={'User-Agent': 'Mozilla/5.0'})
#         webpage5 = urlopen(req5).read()
#         page_soup5 = soup(webpage5, "html.parser")
#         containers51 = page_soup5.find("div", {"class": "col-12"})
#         p52 = containers51.find("div", {"section": "topStories|item-1"})
#         p53 = p52.h3.text.strip()
#
#         req2 = Request('https://gadgets.ndtv.com/news', headers={'User-Agent': 'Mozilla/5.0'})
#         webpage2 = urlopen(req2).read()
#         page_soup2 = soup(webpage2, "html.parser")
#         containers2 = page_soup2.find("div", {"class": "story_list row margin_b30"})
#         p21 = containers2.find("span", {"class": "news_listing"})
#         p22 = p21.text.strip()
#
#         req4 = Request('https://www.theverge.com/tech', headers={'User-Agent': 'Mozilla/5.0'})
#         webpage4 = urlopen(req4).read()
#         page_soup4 = soup(webpage4, "html.parser")
#         containers4 = page_soup4.find("div", {"class": "l-col__main"})
#         p4 = containers4.find("div", {"class": "c-entry-box--compact__body"})
#         p41 = p4.h2.text.strip()
#
#         req3 = Request('https://www.techradar.com/', headers={'User-Agent': 'Mozilla/5.0'})
#         webpage3 = urlopen(req3).read()
#         page_soup3 = soup(webpage3, "html.parser")
#         containers3 = page_soup3.find("div", {"id": "Item1"})
#         p3 = containers3.find("figure", {"class": "feature-block-item"})
#         p31 = p3.find("span", {"class": "article-name"}).text.strip()
#         technologyheadlines_instance = TechnologyHeadlines.objects.create(Mobiles91=p11, CNET=p53, NDTV=p22, Verge=p41, TechRadar=p31)
#         print("Data Sent")
#
# r2()
#
#
#
#
