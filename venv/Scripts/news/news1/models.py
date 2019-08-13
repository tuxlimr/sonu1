from django.db import models
import datetime
from ckeditor.fields import RichTextField


class News(models.Model):

    news_headline = models.CharField(max_length=300)
    newspaper = models.CharField(max_length=50)
    news_time = models.DateTimeField(auto_now_add=True)

class NewsHeadlines (models.Model):

    Firstpost = models.CharField(max_length=300)
    scroll = models.CharField(max_length=300)
    NDTV = models.CharField(max_length=300)
    IndiaToday = models.CharField(max_length=300)
    HindustanTimes = models.CharField(max_length=300)
    Toi = models.CharField(max_length=300)
    news_time = models.DateTimeField(auto_now_add=True)

class BusinessHeadlines (models.Model):

    EconomicTimes = models.CharField(max_length=300)
    MoneyConrol = models.CharField(max_length=300)
    LiveMint= models.CharField(max_length=300)
    BusinessStandard= models.CharField(max_length=300)
    news_time = models.DateTimeField(auto_now_add=True)

class TechnologyHeadlines (models.Model):

    Mobiles91 = models.CharField(max_length=300)
    CNET = models.CharField(max_length=300)
    NDTV = models.CharField(max_length=300)
    Verge = models.CharField(max_length=300)
    TechRadar = models.CharField(max_length=300)
    news_time = models.DateTimeField(auto_now_add=True)

class SportsHeadlines (models.Model):

    FirstPost = models.CharField(max_length=300)
    Toi = models.CharField(max_length=300)
    ESPN = models.CharField(max_length=300)
    Cricbuzz = models.CharField(max_length=300)
    ZeeSports = models.CharField(max_length=300)
    news_time = models.DateTimeField(auto_now_add=True)

class EntHeadlines (models.Model):

    FirstPost = models.CharField(max_length=300)
    IBTimes = models.CharField(max_length=300)
    PinkVilla = models.CharField(max_length=300)
    IndiaToday = models.CharField(max_length=300)
    NDTV = models.CharField(max_length=300)
    news_time = models.DateTimeField(auto_now_add=True)

class Blog (models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title


