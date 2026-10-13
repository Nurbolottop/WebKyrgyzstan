"""
Статьи живут в трёх разделах: «Открой Кыргызстан», «Культура и традиции»,
«Современный Кыргызстан». Здесь собираются их адреса для core/urls.py.
"""
from django.urls import path

from apps.learn import views as learn_views

from . import views


def article_patterns(section_key):
    return [
        path('<slug:category>/', views.category_detail, {'section_key': section_key}, name='category'),
        path('<slug:category>/<slug:slug>/', views.article_detail, {'section_key': section_key}, name='article'),
    ]


def section_patterns(section_key):
    return [
        path('', views.section_index, {'section_key': section_key}, name='index'),
        path('play/<slug:slug>/', learn_views.game_detail, {'section_key': section_key}, name='game'),
        *article_patterns(section_key),
    ]


culture_patterns = (section_patterns('culture'), 'culture')
modern_patterns = (section_patterns('modern'), 'modern')
