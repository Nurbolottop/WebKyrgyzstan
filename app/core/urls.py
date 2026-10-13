from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.decorators.cache import cache_page

from apps.articles.urls import culture_patterns, modern_patterns
from apps.base.sitemaps import sitemaps
from apps.base.views import robots_txt

# Служебные адреса — вне языковых префиксов
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('sitemap.xml', cache_page(60 * 60)(sitemap), {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots'),
]

# Страницы сайта: /ky/…, /ru/…, /en/…; корень перенаправляет на язык браузера
urlpatterns += i18n_patterns(
    path('', include('apps.base.urls')),
    path('discover/', include('apps.discover.urls')),
    path('culture/', include(culture_patterns)),
    path('learn/', include('apps.learn.urls')),
    path('try/', include('apps.practice.urls')),
    path('modern/', include(modern_patterns)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
