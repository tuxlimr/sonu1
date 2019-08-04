from django.db import models
import datetime
from ckeditor.fields import RichTextField


class News(models.Model):

    news_headline = models.CharField(max_length=300)
    newspaper = models.CharField(max_length=50)
    news_time = models.DateTimeField(auto_now_add=True)


class Blog (models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title


