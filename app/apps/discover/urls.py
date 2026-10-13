from django.urls import path

from apps.articles.urls import article_patterns

from . import views

app_name = 'discover'

urlpatterns = [
    path('', views.index, name='index'),
    path('regions/<slug:slug>/', views.region_detail, name='region'),
    path('places/', views.place_list, name='places'),
    path('places/<slug:slug>/', views.place_detail, name='place'),
    *article_patterns('discover'),
]
