from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Служебные адреса — вне языковых префиксов
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]

# Страницы сайта: /ky/…, /ru/…, /en/…; корень перенаправляет на язык браузера
urlpatterns += i18n_patterns(
    path('', include('apps.base.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
