from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sports', views.sports, name='sports'),
    path('technology', views.technology, name='technology'),
    path('business', views.business, name='business'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('blog', views.blog, name='blog'),
    path('currency', views.currency, name='currency'),
    # path(r'^ckeditor/', include('ckeditor.urls')),
]